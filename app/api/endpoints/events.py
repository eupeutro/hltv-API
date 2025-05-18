from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.events.search import EventsSearch
from app.schemas.events.profile import EventProfile

from app.services.events.search import HLTVEventsSearch
from app.services.events.profile import HLTVEventProfile

router = APIRouter()

@router.get("/search/{event_name}", response_model= EventsSearch)
def search_events(event_name: str):
    hltv = HLTVEventsSearch(query=event_name)
    found_events = hltv.search_events()
    return found_events

@router.get("/{event_id}/profile", response_model= EventProfile)
def get_event_profile(event_id: str):
    hltv = HLTVEventProfile(event_id=event_id)
    event_info = hltv.get_event_profile()
    return event_info