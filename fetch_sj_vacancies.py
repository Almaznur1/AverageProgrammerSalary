import requests
from dotenv import load_dotenv
import os


def fetch_sj_vacancies(sj_secret_key, sj_password):
    # url = '	https://api.superjob.ru/2.0/oauth2/password/'
    # payload = {
    #     'login': 'aboohnifa@gmail.com',
    #     'password': f'{sj_password}',
    #     'client_id': '2146',
    #     'client_secret': f'{sj_secret_key}',
    #     }
    # response = requests.post(url, data=payload)
    # print(response.json())
    url = 'https://api.superjob.ru/2.0/vacancies/'
    payload = {
        'host': 'api.superjob.ru',
        'X-Api-App-Id': f'{sj_secret_key}',
        'Authorization': 'Bearer v3.r.137281259.7a56c95ed738cd460bf075beecbe60f6e0134222.a638230263e361a228d71f3b3931d7c5a8439c8d',
        'app_key': f'{sj_secret_key}',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        # 'keyword': 'программист',
        }
    response = requests.post(url, data=payload)
    print(response.text)
    # response.raise_for_status()



def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']
    sj_password = os.environ['SUPER_JOB_ACCOUNT_PASSWORD']
    fetch_sj_vacancies(sj_secret_key, sj_password)


if __name__ == '__main__':
    main()
