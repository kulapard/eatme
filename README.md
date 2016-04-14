# EatMe #

[![Build Status](https://drone.io/github.com/kulapard/eatme/status.png)](https://drone.io/github.com/kulapard/eatme/latest)
[![codecov.io](https://codecov.io/bitbucket/KulaPard/eatme/coverage.svg?branch=default)](https://codecov.io/bitbucket/KulaPard/eatme?branch=default)

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

- `-h` или `--help` - вывод справочной информации по доступным параметрам
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
