import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv
import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="Введите ссылку для сокращения: ")
 
    return parser


def shorten_link(token, long_url):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "long_url": long_url
    }

    response = requests.post(url, headers=headers, json=payload)
    
    response.raise_for_status()

    return response.json()['link']


def get_total_clicks(token, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "unit": "day",
        "units": -1
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()["total_clicks"]


def is_bitlink(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    return response.ok


def main():
    load_dotenv(find_dotenv())
    
    bitly_token = os.getenv('BITLY_SECRET_KEY')

    parser = createParser()
    user_url = parser.parse_args()

    user_input = user_url.url
    
    parsed_url = urlparse(user_input)

    netloc_path_address = f"{parsed_url.netloc}{parsed_url.path}"

    if is_bitlink(bitly_token, netloc_path_address):
        try:
            total_clicks = get_total_clicks(bitly_token, netloc_path_address)
            print("Количество кликов:", total_clicks)
        except requests.exceptions.HTTPError:
            print('Вы ввели ссылку не от Bitly')
    else:
        try:
            bitlink = shorten_link(bitly_token, user_input)
            print("Битлинк:", bitlink)
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка для сокращения')


if __name__ == "__main__":
    main()
    
