# test_alikson
### Документация
http://127.0.0.1:8000/swagger/?format=openapi

# Запуск приложения в Docker контейнере

Это руководство предоставляет инструкции по запуску Django-приложения в контейнере с использованием Docker и Docker Compose.

## Предварительные требования

Убедитесь, что у вас установлены Docker и Docker Compose. Если нет, вы можете установить их, следуя инструкциям на [официальном сайте Docker](https://docs.docker.com/get-docker/) и [официальном сайте Docker Compose](https://docs.docker.com/compose/install/).

## Шаги

1. **Склонируйте репозиторий:**

    ```bash
    git clone https://github.com/codarsssss/test_alikson.git
    ```

2. **Перейдите в каталог проекта:**

    ```bash
    cd test_alikson
    ```

3. **Создайте файл `.env` в корне проекта и укажите необходимые переменные окружения.** Пример файла `.env`:

    ```env
    DEBUG=1
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=localhost 127.0.0.1
    ```

4. **Запустите контейнеры с помощью Docker Compose:**

    ```bash
    docker-compose up --build
    ```

5. **Откройте ваш веб-браузер и перейдите по адресу [http://localhost:8000/](http://localhost:8000/) для доступа к приложению.**

6. **Чтобы завершить работу контейнеров, используйте команду:**

    ```bash
    docker-compose down
    ```

## Примечания

- Если вы вносите изменения в код приложения, они автоматически будут обновляться в контейнере.
- Если вам нужно выполнить дополнительные команды внутри контейнера, используйте:

    ```bash
    docker-compose run web <ваша_команда>
    ```


### Примеры запросов для Postman:
###### Создание производителя
POST http://localhost:8000/manufacturers/

{
    "name": "Manufacturer1"
}
###### Создание категории
POST http://localhost:8000/categories/

{
  "name": "Category1",
  "parent_category": null
}

###### Создание товара
POST http://localhost:8000/products/

{
    "name": "Название товара",
    "category": 1, 
    "manufacturer": 1, 
    "characteristics": [
        {"name": "Характеристика 1", "value": "Значение 1"},
        {"name": "Характеристика 2", "value": "Значение 2"}
    ]
}

###### Добавление характеристик для товара
POST http://localhost:8000/product-characteristics/

{
  "characteristic": {
    "name": "Some Characteristic",
    "value": "Some Value"
  },
  "value": "Some Value",
  "product": 1
}

###### Получение списка товаров по категории с пагинацией
GET http://localhost:8000/categories/1/products/?page=1


###### Получение карточки товара с полным списком характеристик
GET http://localhost:8000/products/1/


###### Создание производителя
GET http://localhost:8000/categories/1/filtered-products/?characteristic=Color:Red
