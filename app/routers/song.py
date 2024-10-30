from fastapi import APIRouter

from app.models.song import Song
from app.resources.song_resource import SongResource # stops circular import issue
from app.services.service_factory import ServiceFactory
from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()


@router.get("/songs/{song_id}")
async def get_songs(song_id: str) ->Song:
    res = ServiceFactory.get_service("SongResource")
    result = res.get_by_key(song_id)
    return result


@router.get("/songs")
async def get_songs(
    page: Optional[int] = Query(1, ge=1, description="Page number"),
    limit: Optional[int] = Query(12, ge=1, le=100, description="Items per page")
):
    """
    Get paginated list of songs
    
    - **page**: Page number (starts from 1)
    - **limit**: Number of items per page (default 12, max 100)
    """
    song_resource = ServiceFactory.get_service("SongResource")
    
    try:
        result = song_resource.get_paginated(page=page, limit=limit)
        return result
    except Exception as e:
        print(f"Error getting songs: {e}")
        return {"error": "Failed to fetch songs"}