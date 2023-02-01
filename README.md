# Расчет средней зарплаты программиста на HeadHunter и SuperJob

Скрипт рассчитывает среднюю зарплату разработчика на 10 популярных языках по вакансиям 
[HeadHunter](https://hh.ru/) и [SuperJob](https://www.superjob.ru/) в Москве

### Как установить

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для получения вакансий на сайте SuperJob через API необходимо [зарегистрировать](https://api.superjob.ru/register) приложение и получить SecretKey. При регистрации приложения потребуется указать сайт. Введите любой, сайт не проверяется.

После регистрации вы получите следующие данные:

* ID приложения

* Secret key

Переименуйте файл `.env.example` в `.env` и занесите в него следующие данные:

* ID приложения
* Secret key
* Адрес электронной почты, указанный при регистрации
* Пароль к вашему аккаунту на SuperJob

```
APP_ID=<your_app_ID>
SUPER_JOB_SECRET_KEY=<SuperJob_secret_key>
SUPER_JOB_ACCOUNT_EMAIL=<your_email>
SUPER_JOB_ACCOUNT_PASSWORD=<your_SuperJob_account_password>
```

### Как запустить

Запустите main.py
```
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).