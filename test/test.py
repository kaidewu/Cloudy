import requests

x = 100

while x != 0:
    print(x)
    requests.get("http://192.168.1.47/api/v1/logs?errorId=asd")
    x -= 1