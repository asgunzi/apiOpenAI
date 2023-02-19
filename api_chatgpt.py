# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 02:07:56 2023

@author: ASGUNZI
"""

import openai

#Salvei o Key da API num arquivo do computador
with open("C://Analytics//api_key.txt", "r") as file:
    api_key = file.read()

openai.api_key =api_key

# Chamar a API do GPT
prompt = ""
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=500
)

# Exibir a resposta do GPT
print(response["choices"][0]["text"])



