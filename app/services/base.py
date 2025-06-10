from dataclasses import dataclass, field
from typing import Optional
from xml.etree import ElementTree

import cloudscraper
from bs4 import BeautifulSoup
from fastapi import HTTPException
from lxml import etree
from requests import Response, TooManyRedirects

from app.utils.utils import trim 
#from app.utils.xpath import pagination


@dataclass
class HLTVBase:
    """
    Base class for making HTTP requests to HLTV and extracting data from the web pages.

    Args:
        URL (str): The URL for the web page to be fetched.
    Attributes:
        response (dict): A dictionary to store the response data.
    """

    URL: str = field(init = False)
    response: dict = field(default_factory= lambda: {}, init= False)
    
    def make_request(self,url: Optional[str] = None) -> Response:
        """
        Make an HTTP GET request to the specified URL.

        Args:
            url (str, optional): The URL to make the request to. If not provided, the class's URL
                attribute will be used.

        Returns:
            Response: An HTTP Response object containing the server's response to the request.

        Raises:
            HTTPException: If there are too many redirects, or if the server returns a client or
                server error status code.
        """
        url = self.URL if not url else url
        scraper = cloudscraper.create_scraper()
        try:
            response: Response= scraper.get(
                url = url,
                headers ={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
                },   
            )
        except TooManyRedirects:
            raise HTTPException(status_code = 404, detail= f"Not found for url: {url}")
        except ConnectionError:
            raise HTTPException(status_code= 500, detail= f"Connection error for url: {url}")
        except Exception as e:
            raise HTTPException(status_code = 500, detail=f"Error for url: {url}. {e}")
        if 400 <= response.status_code < 500:
            raise HTTPException(
                status_code=response.status_code,
                detail = f"Client Error. {response.reason} for url: {url}"
            )
        return response
    
    def request_url_bsoup(self, url:Optional[str] = None) -> BeautifulSoup:
        """
        Fetch the web page content and parse it using BeautifulSoup.

        Returns:
            BeautifulSoup: A BeautifulSoup object representing the parsed web page content.

        Raises:
            HTTPException: If there are too many redirects, or if the server returns a client or
                server error status code.
        """

        response: Response = self.make_request(url)
        return BeautifulSoup(markup=response.content, features="html.parser")
    
    @staticmethod
    def convert_bsoup_to_page(bsoup: BeautifulSoup) -> ElementTree:
        """
        Convert a BeautifulSoup object to an ElementTree.

        Args:
            bsoup (BeautifulSoup): The BeautifulSoup object representing the parsed web page content.

        Returns:
            ElementTree: An ElementTree representing the parsed web page content for further processing.
        """

        return etree.HTML(str(bsoup))
    
    def request_url_page(self, url: Optional[str] = None) -> ElementTree:
        """
        Fetch the web page content, parse it using BeautifulSoup, and convert it to an ElementTree.

        Returns:
            ElementTree: An ElementTree representing the parsed web page content for further
                processing.

        Raises:
            HTTPException: If there are too many redirects, or if the server returns a client or
                server error status code.
        """
        bsoup: BeautifulSoup = self.request_url_bsoup(url)
        return self.convert_bsoup_to_page(bsoup=bsoup)
    
    def get_all_by_xpath(self,xpath: str, element = None) -> list[str]:
        """
    Extract all text elements from the web page using the specified XPath expression.

    Args:
        xpath (str): The XPath expression used to locate the desired elements on the web page.
        element: Optional HTML element to scope the XPath search. Defaults to self.page.
    Returns:
        list[str]: A list of trimmed strings extracted from the elements found via the XPath expression.

    Raises:
        ValueError: If there is an error during XPath evaluation or element extraction.
        """
        try:
            target = element if element is not None else self.page
            elements = target.xpath(xpath)
            return [trim(e) for e in elements if e]
        except Exception as e :
            raise ValueError(f"Error at xpath data extract'{xpath}': {e}") from e
    
    def get_text_by_xpath(
            self,
            xpath: str,
            pos: int =0,
            iloc: Optional[int] = None,
            iloc_from: Optional[int] = None,
            iloc_to: Optional[int] = None,
            join_str: Optional[str] = None,
            attribute: Optional[str] =None,
            element = None
    ) -> Optional[str]:
        """
    Extract text or attribute from elements using XPath.

    Args:
        xpath (str): XPath expression to select elements.
        pos (int): Default index to select if multiple elements match.
        iloc (int): Specific index of the desired element (alternative to 'pos').
        iloc_from (int): Start index for slicing (inclusive).
        iloc_to (int): End index for slicing (exclusive).
        join_str (str): If provided, joins multiple extracted values using this separator.
        attribute (str): Attribute to extract (e.g., 'alt', 'title'). If None, extracts text content.

    Returns:
        Optional[str]: Extracted text or attribute value, or None if not found.
        """
        

        if not hasattr(self,"page"):
            self.page = self.request_url_page()

        base = element if element is not None else self.page

        elements = base.xpath(xpath) 
        
        if not elements:
            return None

        def extract(e):
            if isinstance(e,etree._Element):
                if attribute:
                    return trim(e.get(attribute,""))
                return trim(e.text) if e.text else None
            return trim(str(e)) if e else None

        elements = [extract(e) for e in elements if extract(e)]

        if isinstance(iloc,int):
            return elements[iloc] if iloc < len(elements) else None
        
        if isinstance(iloc_from, int) and isinstance(iloc_to, int):
            elements= elements[iloc_from:iloc_to]
        elif isinstance(iloc_to, int):
            elements = elements[:iloc_to]
        elif isinstance(iloc_from,int):
            elements= elements[iloc_from:]

        if join_str:
            return join_str.join(elements)
        
        try:
            return elements[pos]
        except IndexError:
            return None

    def raise_exception_if_not_found(self, xpath: str):
        """
    Raise an HTTP 404 exception if no element is found for the given XPath expression.

    Args:
        xpath (str): The XPath expression used to search for content on the page.

    Raises:
        HTTPException: Raised with status code 404 if the XPath does not return any result,
        indicating that the requested resource was not found or is invalid.
        """

        if not self.get_text_by_xpath(xpath):
            raise HTTPException(status_code = 404, detail=f"Invalid request (url: {self.URL})")
        
    
    def get_elements_by_xpath(self, xpath: str, element = None) -> list[etree._Element]:
        """
    Extract all matching elements from the page or a given element using the provided XPath expression.

    Args:
        xpath (str): The XPath expression to evaluate.
        element (etree._Element, optional): The base element to search within. If None, uses the full page.

    Returns:
        list[etree._Element]: A list of lxml elements that match the XPath.

    Raises:
        ValueError: If the XPath evaluation fails.
        """
        
        base = element if element is not None else self.page
        try:
            return base.xpath(xpath)
        except Exception as e:
            raise ValueError(f"Error at xpath elements extract '{xpath}': {e}") from e