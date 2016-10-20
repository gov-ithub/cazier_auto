# Cazier Auto

[![Code Climate](https://codeclimate.com/github/gov-ithub/cazier_auto/badges/gpa.svg)](https://codeclimate.com/github/gov-ithub/cazier_auto)
[![Test Coverage](https://codeclimate.com/github/gov-ithub/cazier_auto/badges/coverage.svg)](https://codeclimate.com/github/gov-ithub/cazier_auto/coverage)
[![Build Status](https://travis-ci.org/gov-ithub/cazier_auto.svg?branch=master)](https://travis-ci.org/gov-ithub/cazier_auto)

Date despre istoricul autovehiculelor inscrise in Romania.

## Install

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cp cazier_auto/settings_local.template cazier_auto/settings_local.py
python manage.py migrate
python manage.py runserver
```

## Contributing

Please read the [contribution guidelines](https://github.com/gov-ithub/guidelines).

## Coding style

We use [pep8](https://www.python.org/dev/peps/pep-0008/).

```shell
pep8 cazier_auto
```

## Tests

```shell
python manage.py test
```
