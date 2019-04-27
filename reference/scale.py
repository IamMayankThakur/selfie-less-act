import docker
import random
client = docker.from_env()
portVal = 8000


def scale(val):
	print("\n" + "scaling " + str(val))
	c = len(client.containers.list())
	l = client.containers.list()
	global portVal
	if(val < 20):
		if(c > 1):
			for i in range(c-1):
				down(l[i].id, portVal - i + 1)
			portVal = portVal - (c - 1)

	if(val >= 20 and val < 40):
		run(2, c, l)

	if(val >= 40 and val < 60):
		run(3, c, l)

	if(val >= 60 and val < 80):
		run(4, c, l)

	if(val >= 80 and val < 100):
		run(5, c, l)

	if(val >= 100 and val < 120):
		run(6, c, l)

	if(val >= 120 and val < 140):
		run(7, c, l)

	if(val >= 140 and val < 160):
		run(8, c, l)

	if(val >= 160 and val < 180):
		run(9, c, l)

	if(val >= 180 and val < 200):
		run(10, c, l)
	print("# of containers " + str(len(client.containers.list())) + "\n")


def run(num, c, l):
	global portVal
	if(c < num):
		while(c < num):
			portVal = portVal + 1
			up(portVal)
			c = c + 1
	if(c > num):
		for i in range(c-num):
			down(l[i].id, portVal - i + num)
		portVal = portVal - (c - num)


def up(portVals):
	s1 = client.containers.run('acts', ports={
	                           '80/tcp': portVals}, privileged=False, detach=True)
	print(str(portVals) + " added")


def down(ids, p):
	k = client.containers.get(ids)
	k.kill()
	print(str(p) + " killed")


def killAll():
	for i in client.containers.list():
		k = client.containers.get(i.id)
		k.kill()


killAll()
up(8000)

for i in range(10):
	# k = random.randint(0, 5)
	k=25
	scale(k)

killAll()
