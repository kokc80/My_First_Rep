# Проект "Домашняя работа 10.1 модуль Продвинутый Git"

## Описание:

Проект "Домашняя работа 10.1 модуль Продвинутый Git" - это приложение для отработки навыков работы с Git

## Установка:

1. Клонируйте репозиторий:
git clone https://github.com/kokc80/My_First_Rep
2. Установите зависимости
poetry install


## Использование:
используется для проверки/закрепления материала пройденного на уроке 10.1 
## Документация:
[project]
name = "cd MyGit"
version = "poetry init"
description = "Работа с Git"
authors = [
    {name = "Kokc80",email = "kokc@inbox.ru"}
]
license = {text = "none"}
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
]

[tool.poetry]
packages = [{include = "cd "}]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
## Лицензия:
насколько я понимаю на данном этапе нет необходимости в лицензии