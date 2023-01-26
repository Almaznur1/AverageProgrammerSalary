import requests


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
    languages = [
        'Java'#, 'C', 'C++', 'C#', 'Python', 'PHP', 'JavaScript',  'Go', 'Swift'
        ]

    for language in languages:
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

            hh_vacancies[language]['vacancies_found'] = response.json()['found']
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

    return hh_vacancies


def get_average_salary(salaries):
    vacancies_processed = 0
    sum_salary = 0
    for salary in salaries:
        if salary is None or salary['currency'] != 'RUR':
            continue
        elif salary['from'] and salary['to']:
            sum_salary += (int(salary['from']) + int(salary['to'])) / 2
        elif not salary['from']:
            sum_salary += int(salary['to']) * 0.8
        elif not salary['to']:
            sum_salary += int(salary['from']) * 1.2
        vacancies_processed += 1

    return vacancies_processed, sum_salary


def main():
    print(*fetch_hh_vacancies().items(), sep='\n')


if __name__ == '__main__':
    main()
