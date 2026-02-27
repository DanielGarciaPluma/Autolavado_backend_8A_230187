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

def test_obtener_autos_sin_token():
    response = client.get("/auto/")
    assert response.status_code == 401

def test_crear_auto_con_token():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    auto_nuevo = {
        "usuario_Id": 3, 
        "placa": "XYZ-987",
        "modelo": "Civic",
        "serie": "123456789ABC",
        "color": "Azul",
        "tipo": "Sedan",
        "anio": 2022, 
        "estado": True,
        "fecha_registro": "2026-02-27T10:00:00",
        "fecha_actualizacion": "2026-02-27T10:00:00"
    }
    
    response = client.post("/auto/", json=auto_nuevo, headers=headers)
    assert response.status_code == 200
    assert response.json()["placa"] == "XYZ-987"