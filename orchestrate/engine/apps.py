from django.apps import AppConfig
import docker

client = None
class EngineConfig(AppConfig):
    name = 'engine'
    def ready(self):
        global client
        client = docker.from_env()  
        print("TESTTTT")
        print(client.info())
