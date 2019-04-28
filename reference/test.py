import docker
client = client = docker.from_env()

print(client.info())
