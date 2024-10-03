from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.song import Song
from app.services.service_factory import ServiceFactory


class SongResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        self.data_service = ServiceFactory.get_service("SongResourceDataService")
        self.database = "spotify_db"
        self.collection = "spotify_songs"
        self.key_field= "track_id"

    def get_by_key(self, key: str) -> Song:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        result = Song(**result)
        return result


