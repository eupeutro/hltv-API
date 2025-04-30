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
    URL: str = field(init = False)
    response: dict = field(default_factory= lambda: {}, init= False)
    
    def make_request(self,url: Optional[str] = None) -> Response:
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
    
    def request_url_bsoup(self) -> BeautifulSoup:
        response: Response = self.make_request()
        return BeautifulSoup(markup=response.content, features="html.parser")
    
    @staticmethod
    def convert_bsoup_to_page(bsoup: BeautifulSoup) -> ElementTree:
        return etree.HTML(str(bsoup))
    
    def request_url_page(self) -> ElementTree:
        bsoup: BeautifulSoup = self.request_url_bsoup()
        return self.convert_bsoup_to_page(bsoup=bsoup)
    
    def get_all_by_xpath(self,xpath: str) -> list[str]:
        try:
            elements = self.page.xpath(xpath)
            return [trim(e) for e in elements if e]
        except Exception as e :
            raise ValueError(f"Error at xpath data extract'{xpath}': {e}") from e
            return []
    
    def get_text_by_xpath(
            self,
            xpath: str,
            pos: int =0,
            iloc: Optional[int] = None,
            iloc_from: Optional[int] = None,
            iloc_to: Optional[int] = None,
            join_str: Optional[str] = None,
            attribute: Optional[str] =None
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

        elements = self.page.xpath(xpath) 
        
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
        if not self.get_text_by_xpath(xpath):
            raise HTTPException(status_code = 404, detail=f"Invalid request (url: {self.URL})")