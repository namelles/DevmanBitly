import os
import requests
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse
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
    return response.json()


def count_click(user_url, headers):
    parsed_url = urlparse(user_url).netloc+urlparse(user_url).path
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url}/clicks/summary'
    clicks_count = requests.get(url, headers=headers)
    clicks_count.raise_for_status()
    return clicks_count.json()['total_clicks']


def check_bitlink(user_url, headers):
    parsed_url = urlparse(user_url).netloc + urlparse(user_url).path
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url}'
    response = requests.get(url, headers=headers)
    return any(response.ok for resp in response)


def create_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='?')
    return parser


if __name__ == '__main__':
    headers = {
        "Authorization": f"Bearer {BITLY_TOKEN}"
    }
    parser = create_argument_parser()
    url_in_argument = parser.parse_args()

    if url_in_argument.url:
        user_url = url_in_argument.url
    else:
        user_url = input('Input URL: ')

    try:
        if check_bitlink(user_url, headers=headers):
            print(f'Number clicks for bitlink {user_url}: ',
                  count_click(user_url, headers=headers))
        else:
            print(f'Bitlink for url {user_url}:',
                  get_shortened_link(user_url, headers=headers)['link'])
    except requests.exceptions.HTTPError as http_error:
        print('HTTP error code:', http_error)
