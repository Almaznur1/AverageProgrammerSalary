import requests
from datetime import datetime
from common_functions import get_average_salary


def auth_sj(email, sj_password, app_id, sj_secret_key):
    url = '	https://api.superjob.ru/2.0/oauth2/password/'
    payload = {
        'login': f'{email}',
        'password': f'{sj_password}',
        'client_id': f'{app_id}',
        'client_secret': f'{sj_secret_key}',
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    access_token = response.json()['access_token']
    return access_token


def fetch_sj_vacancies(sj_secret_key, access_token):
    languages = [
        'Java', 'C', 'C++', 'C#', 'Python',
        'PHP', 'Kotlin', 'JavaScript', 'Go', 'Swift'
        ]
    sj_vacancies = {}
    MONTH_IN_SEC = 2592000
    date_month_ago = datetime.now() - datetime.fromtimestamp(MONTH_IN_SEC)
    url = 'https://api.superjob.ru/2.0/vacancies/'

    for language in languages:
        page = 0
        vacancies_processed = 0
        sum_salary = 0
        average_salary = 0

        while True:
            payload = {
                'Authorization': f'Bearer {access_token}',
                'app_key': f'{sj_secret_key}',
                'keyword': f'программист {language}',
                'town': '4',
                'date_published_from': f'{date_month_ago}',
                'page': f'{page}',
                }
            response = requests.get(url, params=payload)
            response.raise_for_status()

            salaries_per_page = [
                {
                    'from': response.json()['objects'][i]['payment_from'],
                    'to': response.json()['objects'][i]['payment_to'],
                    'currency': response.json()['objects'][i]['currency'],
                    }
                for i in range(len(response.json()['objects']))
                ]

            (
                vacancies_processed_per_page, sum_salary_per_page
                ) = get_average_salary(salaries_per_page)
            vacancies_processed += vacancies_processed_per_page
            sum_salary += sum_salary_per_page
            if vacancies_processed != 0:
                average_salary = sum_salary / vacancies_processed
            if not response.json()['more']:
                break
            page += 1
        sj_vacancies[language] = {}
        sj_vacancies[language]['vacancies_processed'] = vacancies_processed
        sj_vacancies[language]['average_salary'] = int(average_salary)
        sj_vacancies[language]['vacancies_found'] = response.json()['total']
    return sj_vacancies
