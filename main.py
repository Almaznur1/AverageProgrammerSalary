from dotenv import load_dotenv
import os
from fetch_sj_vacancies import auth_sj
from fetch_sj_vacancies import fetch_sj_vacancies
from fetch_hh_vacancies import fetch_hh_vacancies
from common_functions import print_table


def main():
    load_dotenv()

    hh_vacancies = fetch_hh_vacancies()
    print_table(hh_vacancies, 'HeadHunter')

    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']
    sj_password = os.environ['SUPER_JOB_ACCOUNT_PASSWORD']
    access_token = auth_sj(sj_secret_key, sj_password)
    sj_vacancies = fetch_sj_vacancies(sj_secret_key, access_token)
    print_table(sj_vacancies, 'SuperJob')


if __name__ == '__main__':
    main()
