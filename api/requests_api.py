import requests

class RequestsApi:

    url = "https://api.thecatapi.com/v1/votes"
    headers = {'x-api-key': '3052ed48-f0ae-4299-b481-965308b88d88'}

    @staticmethod
    def save_api(vote):
        try:
            data = "{\"image_id\":\" "+vote.get_image_id()+" \",\"sub_id\":\""+vote.get_sub_id()+"\",\"value\":"+ str(vote.get_value())+"}"
            headers = {
                'content-type': "application/json",
                'x-api-key': "3052ed48-f0ae-4299-b481-965308b88d88"
                }

            response = requests.request("POST", RequestsApi.url, data=data, headers=headers)
            if response.status_code != 200:
                return False
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def get_all_api():
        try:
            querystring = {"sub_id":"my-user-12344321"}
            response = requests.request("GET", RequestsApi.url, headers=RequestsApi.headers, params=querystring)
            if response.status_code != 200:
                return False
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def get_one_api(id):
        try:
            response = requests.request("GET", RequestsApi.url + "/" +str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return None
            else:
                return response.json()
        except:
            return False

    @staticmethod
    def delete_api(id):
        try:
            response = requests.request("DELETE", RequestsApi.url + "/" +str(id), headers=RequestsApi.headers)
            if response.status_code != 200:
                return None
            else:
                return response.json()
        except:
            return False




