import requests as req
import datetime as dt
import pandas as pd

key='2b24d54d562f42e78b721e11673d49c6'

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY"+key
json_data = req.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) + ", " + json_data("articled")[i]["title"]+".")

    return ar
