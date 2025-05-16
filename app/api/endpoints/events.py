from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.events.search import EventsSearch

from app.services.events.search import HLTVEventsSearch

router = APIRouter()

@router.get("/search/{event_name}", response_model= EventsSearch)
def search_events(event_name: str):
    hltv = HLTVEventsSearch(query=event_name)
    found_events = hltv.search_events()
    return found_events