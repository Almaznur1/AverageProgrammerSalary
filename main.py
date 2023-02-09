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

    email = os.environ['SUPER_JOB_ACCOUNT_EMAIL']
    sj_password = os.environ['SUPER_JOB_ACCOUNT_PASSWORD']
    app_id = os.environ['APP_ID']
    sj_secret_key = os.environ['SUPER_JOB_SECRET_KEY']

    access_token = auth_sj(email, sj_password, app_id, sj_secret_key)
    sj_vacancies = fetch_sj_vacancies(sj_secret_key, access_token)
    print_table(sj_vacancies, 'SuperJob')


if __name__ == '__main__':
    main()
