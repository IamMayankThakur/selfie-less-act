import docker
client = docker.from_env()

# print(client.info())
# print(client.containers.list())
print(client.images.list())

# client.containers.run("acts:latest", detach=True)
# client.containers.run("acts:latest", detach=True)
# client.containers.run("users:latest", detach=True)

print(client.containers.list())


