import requests

import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "66bd5d0894msh7e795bc31731dabp1ce714jsnd5337ac96dab",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}



# print(response.json())
async def remove_background(img_url):
	payload = f"image_url={img_url}"
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.json()["response"]["image_url"]