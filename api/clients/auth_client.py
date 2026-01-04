class AuthClient:
    """
    Клиент для работы с эндпоинтами аутентификации API.
    
    Инкапсулирует логику входа в систему через REST API:
    - отправляет запрос на /auth/login с email и паролем,
    - извлекает JWT-токен из успешного ответа,
    - автоматически устанавливает токен в заголовок Authorization
      для последующих запросов в рамках той же сессии.
    
    Позволяет тестам использовать аутентификацию как единое действие:
        auth = AuthClient(api_client)
        auth.login("user@example.com", "pass123")
        # Все следующие api_client.get/post уже с токеном
    """
    def __init__(self, api_client):
        self.api = api_client

    def login(self, email, password):
        response = self.api.post("/auth/login", json={"email": email, "password": password})
        token = response.json().get("access_token")
        self.api.session.headers["Authorization"] = f"Bearer {token}"
        return response