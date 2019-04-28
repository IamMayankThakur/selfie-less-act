# from .apps import client, api_count, port, count
import threading
import math
import docker

client = docker.from_env()
count = 2
def printit():
        global count
        global client
        threading.Timer(10.0, printit).start()
        # getrequest for the count
        num_of_con_req = math.ceil(count/20)
        print("required=",num_of_con_req)
        n = len(client.containers.list())
        k = n
        print("no of containers=",n)
        print("number of k values used:", k)
        l = []
        for con in client.containers.list():
            l.append(con.id)

        if(n > num_of_con_req):
            num_remove = n - num_of_con_req
            for i in range(0, num_remove):
                con = client.containers.get(l[i])
                con.kill()
                print("container killed:", con)
                k = k - 1
            return

        if (n == num_of_con_req):
                return
        if(n < num_of_con_req):
            num_add = num_of_con_req - n
            for i in range(0, num_add):
                con = client.containers.run('acts', detach=True, ports={
                                            '5000/tcp': 5000 + k}, command="sh -c 'python manage.py collectstatic --noinput && sleep 2 && python manage.py makemigrations --noinput && python manage.py migrate --noinput && gunicorn --reload cloud_project.wsgi:application -b 0.0.0.0:5000 --error-logfile gunicorn.error'")
                print("log=",con.logs())
                print("container added:", con)
                print("on port",5000+k)
                k = k + 1
            return
        print("k value:", k-1)
