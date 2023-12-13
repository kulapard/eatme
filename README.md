### 📢 Notice: EatMe has been succeeded by [GoEatMe](https://github.com/kulapard/go-eatme)

As of now, EatMe is no longer maintained.

---

# EatMe #

[![Build Status](https://travis-ci.org/kulapard/eatme.svg?branch=master)](https://travis-ci.org/kulapard/eatme)
[![codecov.io](https://codecov.io/github/kulapard/eatme/coverage.svg?branch=master)](https://codecov.io/github/kulapard/eatme?branch=master)
[![Updates](https://pyup.io/repos/github/kulapard/eatme/shield.svg)](https://pyup.io/repos/github/kulapard/eatme/)
[![Python 3](https://pyup.io/repos/github/kulapard/eatme/python-3-shield.svg)](https://pyup.io/repos/github/kulapard/eatme/)


Утилита для выполнения массовых операций с вложенными репозиториями
(Mercurial, Git). 

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
