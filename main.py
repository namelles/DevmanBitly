import os
import requests
from dotenv import load_dotenv
load_dotenv()


BITLY_TOKEN = os.getenv('BITLY_TOKEN')


def get_username_info(headers):
    url = 'https://api-ssl.bitly.com/v4/user'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.json())

def get_shortened_link(user_url, headers):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        "long_url": f"{user_url}"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


if __name__ == '__main__':
    headers = {
        "Authorization": f"Bearer {BITLY_TOKEN}"
    }

    user_url = input('Input URL: ')
    try:
        print('Битлинк: ', get_shortened_link(user_url, headers))
    except requests.exceptions.HTTPError:
        print('Error. Invalid URL ')
