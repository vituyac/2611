from drf_spectacular.utils import OpenApiParameter, extend_schema

# Описание параметров для пагинации
pagination_parameters = [
    OpenApiParameter(
        name='page_size',
        description='Кол-во объектов на странице',
        required=False,
        type=int
    ),
    OpenApiParameter(
        name='page',
        description='Номер страницы',
        required=False,
        type=int
    ),
]

account_endpoints = {
    "create": extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя",
        # request="UserSerializer",
        # responses="UserSerializer",
        tags=["Account"]
    ),
    "me": extend_schema(
        summary="Получение данных пользователя",
        description="Возвращает данные текущего пользователя",
        tags=["Account"]
    ),
    "update": extend_schema(
        summary="Обновление данных пользователя",
        description="Обновляет данные текущего пользователя",
        tags=["Account"]
    ),
    "token": extend_schema(
        summary="Авторизация пользователя",
        description="Получение access и refresh токенов",
        tags=["Account"]
    ),
}

admin_account_endpoints = {
    "list": extend_schema(
        summary="Список пользователей",
        description="Возвращает список всех пользователей",
        parameters=pagination_parameters,
        tags=["Admin/Account"]
    ),
    "retrieve": extend_schema(
        summary="Получение данных пользователя",
        description="Возвращает информацию о конкретном пользователе по ID",
        tags=["Admin/Account"]
    ),
    "create": extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя",
        tags=["Admin/Account"]
    ),
    "update": extend_schema(
        summary="Обновление данных пользователя",
        description="Обновляет данные существующего пользователя",
        tags=["Admin/Account"]
    ),
    "destroy": extend_schema(
        summary="Удаление пользователя",
        description="Удаляет существующего пользователя по ID",
        tags=["Admin/Account"]
    ),
}

resetpassword_endpoints = {
    "request_token": extend_schema(
        summary="Запрос на восстановление пароля",
        description="Отправляет письмо с токеном на почту",
        tags=["password_reset"]
    ),
    "confirm_token": extend_schema(
        summary="Смена пароля по токену",
        description="Если токен верный, пароль меняется на новый",
        tags=["password_reset"]
    )
}