Service to generate short urls.

[![Build Status](https://travis-ci.org/ruduran/shorty.svg?branch=master)](https://travis-ci.org/ruduran/shorty)

## Setup

### Python

The easiest way is to work with a virtualenv.
```
virtualenv -p python3.6 venv
. venv/bin/activate
pip install -U -r requirements.txt -r test-requirements.txt
```

### Service

Before starting the service, we need to setup the DB:
```
# Inside the shorty/ dir
python manage.py migrate
```

## Start the service

Once everything is ready, we can run the service:
```
python manage.py runserver
```

## Usage

Things are pretty straightforward, there is just one form where to enter/paste the URL we want to shorten.

Once we click the *Get short url* button or press *Enter*, we'll get the shortened URL ready to be used.

## Run the tests

We can run the tests with the following command:
```
python manage.py test
```

We can also run flake8 to check the code style and PEP8 compliance.
```
flake8
```
