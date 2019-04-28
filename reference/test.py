
import threading
import requests
import time
import docker
import math

client = docker.from_env()
# c=client.images.build(path ="/home/nihali/work/6th sem/subjects/CC/selfie-less-act/acts", tag="acts")
# print(c)
# con = client.containers.run('acts', detach=True, ports= {'8000/tcp': 8003}, command="sh -c 'python manage.py collectstatic --noinput && sleep 2 && python manage.py makemigrations --noinput && python manage.py migrate --noinput && gunicorn --reload cloud_project.wsgi:application -b 0.0.0.0:8000 --error-logfile gunicorn.error'")

# print(con.logs())
# c = requests.get('http://127.0.0.1:8000/api/v1/acts')
# print(c)
# # con = client.containers.run('acts',detach=True,command="ls")
# # print(con.logs())
# # con = client.containers.run('acts', detach=True)
# print(len(client.containers.list()))
# print(len(client.containers.list(all)))
# print(client.containers.list())
# container = client.containers.get('270e0249b0')
# container.kill()

count = 0
k=8000


def printit():
  global k
  threading.Timer(10.0, printit).start()
  print("Hello, World!")
  # getrequest for the count
  num_of_con_req = math.ceil(count/20)
  print(num_of_con_req)
  n = len(client.containers.list())
  # k = n
  print(n)
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
      k = k-1

  if(n == num_of_con_req):
    return
  if(n < num_of_con_req):
    num_add = num_of_con_req - n
    for i in range(0, num_add):
      print(k)
      con = client.containers.run('acts', detach=True, volumes={'acts_vol': {'bind': '/acts', 'mode': 'rw'}}, ports={
                                  '8000/tcp':k}, command="sh -c 'python manage.py collectstatic --noinput && sleep 2 && python manage.py makemigrations --noinput && python manage.py migrate --noinput && gunicorn --reload cloud_project.wsgi:application -b 0.0.0.0:8000 --error-logfile gunicorn.error'")
      print(con.logs())
      print("container added:", con)
      # print(8000+k)
      k = k+1
  # print("k value:", k-1)
  # count = 25


printit()

time.sleep(5)
print("yolo")
# i=0
# while(i<1000):
#     print("yolo!")
#     i=i+1
