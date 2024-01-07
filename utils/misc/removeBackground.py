import logging
import requests

url = "https://background-removaL.p.rapidapi.com/remove"

payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg"}
headers = {
         "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "2a3e540985mshe66e3dbd53e4361p13a8b5jsn8e6be55e5ecc",
        "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# response = requests.post(url,data=payload, headers=headers)

# print(response.json())

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST",url,data=payload, headers=headers)
    return response.json()['response']['image_url']