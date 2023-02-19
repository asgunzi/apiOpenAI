# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:56:44 2023

@author: ASGUNZI
"""

import requests
import json


# Set up the API endpoint and authorization
url = "https://api.openai.com/v1/images/generations"

#Salvei o Key da API num arquivo do computador
with open("C://Analytics//api_key.txt", "r") as file:
    api_key = file.read()

OPENAI_API_KEY=api_key 

# Set up the request headers with the API key and content type
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set up the request data with the prompt and other parameters
prompt = "futuristic robot in a boat in a lake, some trees and mountain in backgroud monet style  highly detailed 4k"
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "512x512"
}

# Make the API request using the requests library
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse the response JSON to get the image URL
response_json = response.json()
image_url = response_json['data'][0]['url']

# Do something with the image URL, like download or display it
print(image_url)


