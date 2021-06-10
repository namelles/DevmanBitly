import os
import requests
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_shortened_link(user_url, headers):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        'long_url': user_url
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


def count_click(user_url, headers):
    parsed_url = f'{urlparse(user_url).netloc}{urlparse(user_url).path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url}/clicks/summary'
    clicks_count = requests.get(url, headers=headers)
    clicks_count.raise_for_status()
    return clicks_count.json()['total_clicks']


def check_bitlink(user_url, headers):
    parsed_url = f'{urlparse(user_url).netloc}{urlparse(user_url).path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url}'
    response = requests.get(url, headers=headers)
    return response.ok


def create_argument_parser():
    parser = argparse.ArgumentParser(description="""Getting short links 
                                    using the Bitly service API.""")
    parser.add_argument('-url', help='Sends url for execution')
    return parser


if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    headers = {
        'Authorization': f'Bearer {bitly_token}'
    }
    parser = create_argument_parser()
    args = parser.parse_args()
    user_url = args.url

    try:
        if check_bitlink(user_url, headers=headers):
            print(f'Number clicks for bitlink {user_url}: ',
                  count_click(user_url, headers=headers))
        else:
            print(f'Bitlink for url {user_url}:',
                  get_shortened_link(user_url, headers=headers)['link'])
    except requests.exceptions.HTTPError as http_error:
        print('HTTP error code:', http_error)
