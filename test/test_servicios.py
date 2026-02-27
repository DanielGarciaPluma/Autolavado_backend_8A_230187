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

def test_crear_servicio():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    nuevo_servicio = {
        "nombre": "Lavado Premium",
        "descripcion": "Lavado exterior e interior con cera",
        "costo": 150.50,
        "duracion_minutos": 45,
        "estado": True,
        "fecha_registro": "2026-02-27T10:00:00",
        "fecha_actualizacion": "2026-02-27T10:00:00"
    }
    
    response = client.post("/servicio/", json=nuevo_servicio, headers=headers)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Lavado Premium"

def test_obtener_servicios():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.get("/servicio/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)