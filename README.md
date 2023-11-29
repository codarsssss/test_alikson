# test_alikson
### Документация
http://127.0.0.1:8000/swagger/?format=openapi

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
