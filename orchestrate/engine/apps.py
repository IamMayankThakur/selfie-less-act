from django.apps import AppConfig
import docker
import threading
from .utils import printit

client = None
api_count = 0
port = 0
prev_con = 0
count = 19
class EngineConfig(AppConfig):
    name = 'engine'
    def ready(self):
        # global client
        # client = docker.from_env()  
        print("TESTTTT")
        printit()
        # print(client.info())

