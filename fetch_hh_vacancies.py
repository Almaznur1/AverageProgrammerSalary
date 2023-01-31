import requests
from common_functions import get_average_salary


def fetch_hh_vacancies():
    hh_vacancies = {
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
    url = 'https://api.hh.ru/vacancies/'

    for language in hh_vacancies:
        page = 0
        vacancies_processed = 0
        sum_salary = 0
        while True:
            payload = {
                'text': f'Программист {language}',
                'area': '1', 'period': '30', 'page': {page}, 'per_page': '100'
                }
            response = requests.get(url, params=payload)
            response.raise_for_status()

            pages_number = response.json()['pages']
            salaries_per_page = [
                response.json()['items'][i]['salary']
                for i in range(len(response.json()['items']))
                ]
            (
                vacancies_processed_per_page, sum_salary_per_page
                ) = get_average_salary(salaries_per_page)
            vacancies_processed += vacancies_processed_per_page
            sum_salary += sum_salary_per_page
            page += 1
            if page == pages_number:
                break
        average_salary = sum_salary / vacancies_processed
        hh_vacancies[language]['vacancies_processed'] = vacancies_processed
        hh_vacancies[language]['average_salary'] = int(average_salary)
        hh_vacancies[language]['vacancies_found'] = response.json()['found']
    return hh_vacancies


def main():
    print(*fetch_hh_vacancies().items(), sep='\n')


if __name__ == '__main__':
    main()
