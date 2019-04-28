from django.apps import AppConfig
import docker
import threading


class EngineConfig(AppConfig):
    name = 'engine'
    # def ready(self):
    #     # global client
    #     # client = docker.from_env()  
    #     print("TESTTTT")
    #     s = SessionStore()
    #     s['hit'] = 0
    #     scale()

