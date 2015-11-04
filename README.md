# EatMe #

[![Build Status](https://drone.io/bitbucket.org/KulaPard/eatme/status.png)](https://drone.io/bitbucket.org/KulaPard/eatme/latest)
[![codecov.io](https://codecov.io/bitbucket/KulaPard/eatme/coverage.svg?branch=master)](https://codecov.io/bitbucket/KulaPard/eatme?branch=master)

Утилита для выполнения массовых операций с вложенными репозиториями
(пока только Mercurial). 

## Установка ##
```
pip install eatme
```

## Запуск ##
```
eatme COMMAND
```

Дополнительные ключи:

- `--help` - вывод справочной информации по доступным параметрам
- `--version` - вывод версии приложения и даты последнего обновления

## Тестирование ##
Тесты (nosetests) + проверка покрытия (coverage) + статическая проверка кода на наличие грубых ошибок (flake8 + pylint)
с помощью [tox](https://pypi.python.org/pypi/tox):
```
tox --skip-missing-interpreters --recreate
```

Тщательная статическая проверка кода:
```
tox -e check --skip-missing-interpreters --recreate
```