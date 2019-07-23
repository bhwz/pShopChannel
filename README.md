# pShopChannel
An advanced Flask (Python) based storefront CMS. 

## Setup
Steps to Success.

### Init Pipenv:
```
pipenv install
```
You can also use regular old pip and venv if you want, I won't stop you.

### Set Environment Variables:
```
cp .env.default .env
```
...and then edit. You can also (and should probably prefer to) set them at runtime
from the command line, or in your service file (you are using one, aren't you?) 

### Make DB:
```
pipenv run flask db init

pipenv run flask db migrate

pipenv run flask db upgrade
```
Obviously, don't prefix with `pipenv run` if you aren't using pipenv.

### Run it with Gunicorn:
```
gunicorn -w <number of workers> "app:create_app()"
```
And that's it!
