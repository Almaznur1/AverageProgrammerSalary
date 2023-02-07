import requests
from common_functions import get_average_salary


def fetch_hh_vacancies():
    languages = [
        'Java', 'C', 'C++', 'C#', 'Python',
        'PHP', 'Kotlin', 'JavaScript', 'Go', 'Swift'
        ]
    hh_vacancies = {}
    url = 'https://api.hh.ru/vacancies/'
    moscow_code = '1'
    month = '30'

    for language in languages:
        page = 0
        vacancies_processed = 0
        sum_salary = 0
        while True:
            payload = {
                'text': f'Программист {language}',
                'area': moscow_code, 'period': month,
                'page': {page}, 'per_page': '100'
                }
            response = requests.get(url, params=payload)
            response.raise_for_status()

            response = response.json()
            pages_number = response['pages']
            salaries_per_page = [
                response['items'][i]['salary']
                for i in range(len(response['items']))
                ]
            (vacancies_processed_per_page,
                sum_salary_per_page) = get_average_salary(salaries_per_page)
            vacancies_processed += vacancies_processed_per_page
            sum_salary += sum_salary_per_page
            page += 1
            if page == pages_number:
                break
        average_salary = sum_salary / vacancies_processed
        hh_vacancies[language] = {}
        hh_vacancies[language]['vacancies_processed'] = vacancies_processed
        hh_vacancies[language]['average_salary'] = int(average_salary)
        hh_vacancies[language]['vacancies_found'] = response['found']
    return hh_vacancies
