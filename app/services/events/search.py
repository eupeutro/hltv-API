from dataclasses import dataclass

from app.services.base import HLTVBase

@dataclass
class HLTVEventsSearch(HLTVBase):

    query: str

    def __post_init__(self) -> None:
        """
        Initialize the HLTVPlayerSearch class by setting up the search URL.
        """
        HLTVBase.__init__(self)
        self.URL=f"https://www.hltv.org/search?term={self.query}"
        self.response["query"] = self.query
        self.page_data = self.__fetch_json()

    def __fetch_json(self) -> dict:
        """
        Makes a GET request to the HLTV search URL and returns the JSON response.

        Returns:
            dict: Raw JSON data returned from the HLTV search endpoint.
        """

        res = self.make_request(self.URL)
        return res.json()
    
    def __parse_search_results(self) -> list:
        """
        Parses the list of events from the HLTV search results.

        Extracted data includes:
            - id: Unique HLTV event ID
            - name: Event name
            - url: Link to the event profile page
            - event_location: Event physical location
            - prize_pool: Event prize pool
            - flag_url: URL to the event country flag
            - event_logo_url: URL to the event logo
            - event_type: Type of event (eg. "Major", "International LAN")
            - event_matches_url: URL to the event matches

        Returns:
            list: A list of dictionaries, each representing a event.
        """

        results = []

        events = self.page_data[0].get("events", [])

        for event in events:
            id = event.get("id")
            name = event.get("name")
            url = f"https://www.hltv.org{event.get('location')}"
            event_location = event.get("physicalLocation")
            prize_pool = event.get("prizePool")
            flag_url = event.get("flagUrl")
            event_logo_url = event.get("eventLogo")
            event_type = event.get("eventType")
            event_matches_url = f"https://www.hltv.org{event.get('eventMatchesLocation')}"

            results.append({
                "id": str(id),
                "name": name,
                "url": url,
                "event_location": event_location,
                "prize_pool": prize_pool,
                "flag_url": flag_url,
                "event_logo_url": event_logo_url,
                "event_type": event_type,
                "event_matches_url": event_matches_url
            })

        return results
    
    def search_events(self) -> dict:
        """
        Retrieves and parses event search results based on the provided query.

        Returns:
            dict: A dictionary containing the original search query and a list of results.
        """
        
        self.response["query"] = self.query
        self.response["results"] = self.__parse_search_results()

        return self.response
