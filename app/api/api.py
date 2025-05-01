from fastapi import APIRouter

from app.api.endpoints import players

api_router = APIRouter()

api_router.include_router(players.router, prefix="/players", tags =["players"])