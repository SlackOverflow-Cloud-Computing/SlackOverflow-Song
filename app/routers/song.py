from fastapi import APIRouter

from app.models.song import Song
from app.resources.song_resource import SongResource # stops circular import issue
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/songs/{song_id}")
async def get_songs(song_id: str) ->Song:
    res = ServiceFactory.get_service("SongResource")
    result = res.get_by_key(song_id)
    return result

