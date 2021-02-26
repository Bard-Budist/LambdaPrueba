from database.db import Db
import requests
import time
from decouple import config

#Initialice data base
database = Db()

def lambda_handler():
    # main function
    steps = 0
    while True:
        if (steps == 15):
            send_data()
            break
        save_database()
        time.sleep(60)
        steps = steps + 1

def get_data():
    """
    Get data with API of the site
    """
    try:
        data = requests.get("https://dweet.io:443/get/latest/dweet/for/thecore")
        return data.json()
    except:
        print("Error while process data of site Dweet")

def save_database():
    """
    Format and save data in data_base 
    """
    data_save = get_data()
    # Get data of the dict
    temperature = data_save['with'][0]['content']['temperature']
    humidity = data_save['with'][0]['content']['humidity']
    database.insert(temperature, humidity)

def send_data():
    """
    Send data to URL 
    """
    data_temperature = database.all()
    data_to_return = []
    for item in data_temperature:
        data_json = {
            'id': item[0],
            'temperature': item[1],
            'humidity': item[2]
        }
        data_to_return.append(data_json)
    requests.post(config("URL_POST"), data = {'data': data_to_return[0]})
