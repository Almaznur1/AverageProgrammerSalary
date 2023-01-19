import requests
from dotenv import load_dotenv
import os


def fetch_sj_vacancies(sj_secret_key):
    # url = 'https://api.superjob.ru/2.0/oauth2/access_token/'
    url = 'https://api.superjob.ru/2.0/vacancies/'
    # payload = {
    #     # 'Host': 'api.superjob.ru',
    #     'X-Api-App-Id': f'{sj_secret_key}',
    #     # 'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    # response = requests.get(url), params=payload)
    url = 'https://api.superjob.ru/2.0/favorites/'
    payload = {
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': f'{sj_secret_key}',
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print(response.text)


def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']
    fetch_sj_vacancies(sj_secret_key)


if __name__ == '__main__':
    main()
