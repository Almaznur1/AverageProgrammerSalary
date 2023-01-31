def get_average_salary(salaries):
    vacancies_processed = 0
    sum_salary = 0
    for salary in salaries:
        if (
                salary is None or
                salary['currency'] != 'RUR' and salary['currency'] != 'rub' or
                not salary['from'] and not salary['to']
                ):
            continue
        elif salary['from'] and salary['to']:
            sum_salary += (int(salary['from']) + int(salary['to'])) / 2
        elif not salary['from']:
            sum_salary += int(salary['to']) * 0.8
        elif not salary['to']:
            sum_salary += int(salary['from']) * 1.2
        vacancies_processed += 1

    return vacancies_processed, sum_salary
