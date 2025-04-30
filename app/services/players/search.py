from dataclasses import dataclass
from xml.etree import ElementTree

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, trim
from app.utils.xpath import Players


@dataclass
class HLTVPlayerSearch(HLTVBase):
    query: str

    def __post_init__(self) -> None:
        url = f"https://www.hltv.org/search?query={self.query}"
        HLTVBase.__init__(self)
        self.URL = url
        self.page = self.request_url_page()
    
    def __parse_search_results(self) -> list:

        search_results: list[ElementTree] = self.page.xpath(Players.Search.RESULTS)
        results = []

        for result in search_results:
            id = extract_from_url(result.xpath(Players.Search.URL), "id")
            url= f"https://www.hltv.org/{result.xpath(Players.Search.URL)}"
            name = trim(result.xpath(Players.Search.NAME))
