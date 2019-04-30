# from .apps import client, api_count, port, count
import threading
import math
import docker
import requests
from .models import Count
client = docker.from_env()
# count = 0
k = 8000
container_list = []
started_count = False
prev_con = 0


def increment_count():
    global started_count
    global container_list
    if list(Count.objects.all()) == []:
        c = Count()
        started_count = True
        c.api_count = 1
        c.save()
        print("Incremented count")
        run_container()
        # scale()
        # health_check()
        # p = 8000
        # for i in client.containers.list():
        #     container_list.append({p: i})
        #     p+=1
        # # health_check()
        # print("CON INIT:", container_list)
        # scale()
        # health_check()
        return 1
    c = Count.objects.first()
    c.api_count = c.api_count + 1
    c.save()
    # p = 8000
    # for i in client.containers.list():
    #     container_list.append({p: i})
    #     p += 1
    # print("Count incremented")
    return 1

def scale():
    # global count
    global client
    global k
    global container_list


    tr = Count.objects.all()
    if list(tr) == []:
        count = 1
    else:
        count = Count.objects.first().api_count
    capi = Count.objects.first()
    capi.api_count = 1
    capi.save()
    print("Count from scale",count)
    threading.Timer(120.0, scale).start()
    # getrequest for the count
    num_of_con_req = math.ceil(count-1 / 20)
    if num_of_con_req == 0:
        num_of_con_req = 1
    print("required=", num_of_con_req)
    n = len(client.containers.list())
    # k = n
    print("no of containers=", n)
    print("number of k values used:", k)
    l = []
    for con in client.containers.list():
        l.append(con.id)

    while(n > num_of_con_req):
        # num_remove = n - num_of_con_req
        # for i in range(0, num_remove):
        kill_container(0)
        n -= 1
        return

    if (n == num_of_con_req):
        return
    if(n < num_of_con_req):
        num_add = num_of_con_req - n
        for i in range(0, num_add):
            run_container()
            print("on port", k)
        return
    # print("k value:", k-1)


def health_check():
    global container_list
    ip = "http://127.0.0.1:"
    threading.Timer(1.0, health_check).start()
    for i in range(len(container_list)):
        port = list(container_list[i].keys())[0]
        print(ip + str(port) + "/api/v1/_health")
        response = requests.get(ip + str(port) + "/api/v1/_health")
        # print(ip + str(port) + "/api/v1/_health")
        print("Health :", response)
        if not response:
            requests.get(ip + str(port) + "/api/v1/_resetcrash")
            c_id = list(container_list[i].values())[0]
            c_id.kill()
            container_list.remove(container_list[i])
            run_container()
        print("\n")


def run_container():
    global client
    global k
    global container_list
    con = client.containers.run('acts', detach=True, volumes={'actw_vol': {'bind': '/acts', 'mode': 'rw'}}, ports={
        '8000/tcp': k}, command="sh -c 'python manage.py collectstatic --noinput && python manage.py makemigrations --noinput && python manage.py migrate --noinput && gunicorn --reload cloud_project.wsgi:application -b 0.0.0.0:8000 --error-logfile gunicorn.error'")
    container_list.append({k: con})
    k += 1
    print(container_list)

def kill_container(i):
	global client
	global k
	global container_list
	l = []
	for con in client.containers.list():
		l.append(con.id)
	con = client.containers.get(l[i])
	con.kill()
	print("container killed:", con)
	for j in container_list:
		if list(j.values())[0] == con:
			container_list.remove(j)
	return 
