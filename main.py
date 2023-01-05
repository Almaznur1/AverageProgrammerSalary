import requests


def fetch_hh_vacancies():
    url = 'https://api.hh.ru/vacancies/'
    payload = {'text': 'Programmer'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.url)


def main():
    fetch_hh_vacancies()


if __name__ == '__main__':
    main()
