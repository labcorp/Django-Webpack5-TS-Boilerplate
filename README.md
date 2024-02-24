# Minimal Django with Webpack, Typescript and Bootstrap setup!
It should be pretty self explanatory, let me know if you need any help!

> **IMPORTANT:** Docker setup is not yet ready for production!

## Docker usage
0. Rename `.env.example` > `.env` and update it
1. Run `docker-compose build`
2. Run `docker-compose up -d`
3. [optional] Run `docker-compose exec boilerplate_app python manage.py createsuperuser`
4. Profit...

Suggestion: Rename the `boilerplate_` image names in docker to your own app/project (also in DB scheme on .env).

## Debugging Django App (in VSCode)
Django App can be debugged attaching VSCode to the PTVSD server (launch.json is included in this boilerplate), so:

1. Add your breakpoints (or not)
2. Go to 'Run and Debug' on the left panel
3. Select 'Docker: Django'
4. Start it (F5)

## Basic usage (legacy, but still works - kindof)

**Front-end**
1. Run `yarn install`
2. Run `yarn serve`
3. Profit...

**Back-end**
1. Create virtualenv && activate
2. Run `pip install -r requirements.txt`
3. Rename `.env.example` > `.env` and update it
4. [optional] Make `manage.py` "runabble": `$ chmod +x manage.py`
5. Run `./manage.py migrate`
6. [optional] Run `./manager.py createsuperuser`
7. Run `./manage.py runserver`
8. Profit...

---
