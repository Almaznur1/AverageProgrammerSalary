import requests
from dotenv import load_dotenv
import os
from datetime import datetime


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
    MONTH_IN_SEC = 2592000
    sj_vacancies = {
        'Java': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'C': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'C++': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'C#': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'Python': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'PHP': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'JavaScript': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'Go': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        'Swift': {
            'vacancies_found': 0,
            'vacancies_processed': 0,
            'average_salary': 0,
            },
        }
    
    url = 'https://api.superjob.ru/2.0/vacancies/'
    language = 'Python'
    date_published_from = datetime.now() - datetime.fromtimestamp(MONTH_IN_SEC)
    while True:
        page = 0
        for language in sj_vacancies:
            payload = {
                'Authorization': f'Bearer {access_token}',
                'app_key': f'{sj_secret_key}',
                'keyword': f'программист {language}',
                'town': '4',
                'date_published_from': f'{date_published_from}',
                'page': f'{page}',
                'count': '100',
                }
            response = requests.get(url, params=payload)
            response.raise_for_status()

        if response.json()['more']:
            page += 1
        else:
            break
    vacancies = response.json()['objects']
    for vacancy in vacancies:
        print(vacancy['profession'], vacancy['town']['title'])


def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']
    sj_password = os.environ['SUPER_JOB_ACCOUNT_PASSWORD']
    access_token = auth_sj(sj_secret_key, sj_password)
    fetch_sj_vacancies(sj_secret_key, access_token)


if __name__ == '__main__':
    main()
