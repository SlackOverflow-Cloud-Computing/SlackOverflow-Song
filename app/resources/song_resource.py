from typing import Any, Dict, List
from framework.resources.base_resource import BaseResource
from app.models.song import Song
from app.services.service_factory import ServiceFactory
import dotenv, os
from math import ceil

dotenv.load_dotenv()
db = os.getenv('DB_NAME')
collection = os.getenv('DB_COLLECTION')

class SongResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)
        self.data_service = ServiceFactory.get_service("SongResourceDataService")
        self.database = db
        self.collection = collection
        self.key_field = "track_id"

    def get_by_key(self, key: str) -> Song:
        d_service = self.data_service
        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
        result = Song(**result)
        return result

    def get_paginated(self, page: int = 1, limit: int = 12) -> Dict[str, Any]:
        """
        Get paginated songs from the database
        
        Args:
            page (int): The page number (1-based indexing)
            limit (int): Number of items per page
            
        Returns:
            Dict containing:
                - total: Total number of songs
                - songs: List of songs for the current page
        """
        d_service = self.data_service
        
        # Get total count
        total = d_service.get_count(self.database, self.collection)
        
        # Calculate offset
        offset = (page - 1) * limit
        
        # Get paginated results
        songs = d_service.get_paginated_data(
            self.database,
            self.collection,
            offset=offset,
            limit=limit
        )
        
        return {
            "total": total,
            "songs": songs
        }

    def get_all(self) -> list[Song]:
        d_service = self.data_service
        result = d_service.get_all_data_objects(self.database, self.collection)
        return result
    
    def add(self, data: List[Song]) -> bool:
        d_service = self.data_service
        for d in data:
            result = d_service.add_data_object(self.database, self.collection, d.model_dump())
        return result