from fastapi import APIRouter

from app.api.endpoints import players
from app.api.endpoints import events
from app.api.endpoints import teams
from app.api.endpoints import ranking

api_router = APIRouter()

api_router.include_router(players.router, prefix="/players", tags =["Players"])

api_router.include_router(events.router, prefix="/events", tags= ["Events"]) 

api_router.include_router(teams.router, prefix="/teams", tags = ["Teams"])

api_router.include_router(ranking.router, prefix="/ranking", tags = ["Ranking"])