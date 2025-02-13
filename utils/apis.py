import requests

class APIS:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    #to get
    def getRequest(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def postResquest(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def putRequest(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def deleteRequest(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.request('DELETE', url, headers=self.headers)
        return response
