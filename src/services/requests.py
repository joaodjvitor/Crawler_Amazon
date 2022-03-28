from urllib import response
import requests as req

def get_request(url, headers = {}):
    response = req.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception()
        
    return response

