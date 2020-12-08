# import requests

# BASE_URL=" http://127.0.0.1:5000/"

# data = [{"likes":1023, "name":"This is video title","views":2220},
#         {"likes":1021, "name":"Another video title","views":1040},
#         {"likes":104, "name":"tim","views":1000}]

# for i in range(len(data)):
#     response = requests.put(BASE_URL + "video/" + str(i),data[i])
#     print(response.json())


# input()

# response = requests.get(BASE_URL + "video/1")
# print(response.json())

import requests
import json
BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/1", {"likes":9999})
print(response.json())
