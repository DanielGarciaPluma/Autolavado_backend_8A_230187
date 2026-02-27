from fastapi import FastAPI
from routes.routes_rol import rol
from routes.routes_usuario import usuario
from routes.routes_auto import auto
from routes.routes_servicios import servicio
from routes.routes_auto_servicio import auto_servicio
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="API Segura de Administracion de un autolavado",
    description="API creada por mi profesor y le copie el código"
)
@app.get("/")
def root():
    return RedirectResponse(url="/docs")

app.include_router(usuario)
app.include_router(rol)
app.include_router(auto)
app.include_router(servicio)
app.include_router(auto_servicio)