from framework.services.service_factory import BaseServiceFactory
import app.resources.song_resource as song_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
import dotenv, os

dotenv.load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))


class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        if service_name == 'SongResource':
            result = song_resource.SongResource(config=None)
        elif service_name == 'SongResourceDataService':
            print(user, password, host, port)
            context = dict(user=user, password=password, host=host, port=port)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result




