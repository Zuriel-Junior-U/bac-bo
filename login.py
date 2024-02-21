import os

import requests
import dotenv


dotenv.load_dotenv()

def logar():
    data = {
        'emailId': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
    }

    response = requests.post('https://service.estrelabet.com//ajax/login', data=data)
    return response.cookies
