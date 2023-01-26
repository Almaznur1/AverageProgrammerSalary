import requests
from dotenv import load_dotenv
import os


def auth_sj(sj_secret_key, sj_password):
    url = '	https://api.superjob.ru/2.0/oauth2/password/'
    payload = {
        'login': 'aboohnifa@gmail.com',
        'password': f'{sj_password}',
        'client_id': '2146',
        'client_secret': f'{sj_secret_key}',
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    access_token = response.json()['access_token']
    return access_token


def fetch_sj_vacancies(sj_secret_key, access_token):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    payload = {
        'Authorization': f'Bearer {access_token}',
        'app_key': f'{sj_secret_key}',
        'keyword': 'программист',
        'town': '4',
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    vacancies = response.json()['objects']
    for vacancy in vacancies:
        print(vacancy['profession'])


def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']
    sj_password = os.environ['SUPER_JOB_ACCOUNT_PASSWORD']
    access_token = auth_sj(sj_secret_key, sj_password)
    fetch_sj_vacancies(sj_secret_key, access_token)


if __name__ == '__main__':
    main()
