# образ на основе которого создаём контейнер
FROM python:3.11.5-slim-bullseye

# переменные окружения для python
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# рабочая директория внутри проекта
WORKDIR /test_alikson

# устанавливаем зависимости
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .