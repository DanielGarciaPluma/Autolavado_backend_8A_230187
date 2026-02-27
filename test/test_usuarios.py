from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv
import os

client = TestClient(app)

def obtener_token():
    test_email = os.getenv("TEST_USER_EMAIL")
    test_password = os.getenv("TEST_USER_PASSWORD")

    login_response = client.post("/login/", data={"username": test_email, "password": test_password})
    return login_response.json()["access_token"]

def test_obtener_usuarios_con_token():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/usuario/", headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_usuario_nuevo():
    # En este caso asumimos que POST /usuario/ está desprotegido para que la gente se registre, 
    # o protegido si solo el jefe puede crear empleados. Mandamos el token por si acaso.
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    nuevo_usuario = {
        "rol_Id": 1,
        "nombre": "Carlos",
        "primer_apellido": "Gomez",
        "segundo_apellido": "Perez",
        "direccion": "Calle Falsa 123",
        "correo_electronico": "carlos@autolavado.com",
        "numero_telefono": "5551234567",
        "contrasena": "carlos123",
        "estado": True,
        "fecha_registro": "2026-02-27T10:00:00",
        "fecha_actualizacion": "2026-02-27T10:00:00"
    }
    
    response = client.post("/usuario/", json=nuevo_usuario, headers=headers)
    # Esperamos 200 (éxito) o 400 (si Carlos ya existe de una prueba anterior)
    assert response.status_code in [200, 400]