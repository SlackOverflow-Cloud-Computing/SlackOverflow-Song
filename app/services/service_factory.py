from framework.services.service_factory import BaseServiceFactory
import app.resources.song_resource as song_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #
        if service_name == 'SongResource':
            result = song_resource.SongResource(config=None)
        elif service_name == 'SongResourceDataService':
            context = dict(user="admin", password="slackOverflowDB",
                           host="database-1.ccjxezwbfect.us-east-1.rds.amazonaws.com", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result




