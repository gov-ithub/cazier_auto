# Cazier Auto

[![Code Climate](https://codeclimate.com/github/gov-ithub/cazier_auto/badges/gpa.svg)](https://codeclimate.com/github/gov-ithub/cazier_auto)
  
TODO: migrate HTMLs from POC (https://github.com/gov-ithub/hackaton-v0.0.1/tree/master/cazier-auto)

## Install

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
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
