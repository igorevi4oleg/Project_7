BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'

# API эндпоинты
COURIER_CREATE = '/courier'
COURIER_LOGIN = '/courier/login'
COURIER_DELETE = '/courier/{courier_id}'
ORDERS = '/orders'
GET_ORDERS = '/orders?limit=10&page=0&nearestStation=["110"]'

# Тестовые данные
SUCCESSFUL_CREATION_MESSAGE = {"ok": True}
DUPLICATE_COURIER_MESSAGE = "Этот логин уже используется. Попробуйте другой."
MISSING_FIELD_MESSAGE = "Недостаточно данных для создания учетной записи"
MISSING_FIELD_LOGIN_MESSAGE = "Недостаточно данных для входа"