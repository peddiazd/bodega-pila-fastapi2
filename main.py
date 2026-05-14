from fastapi import FastAPI
from rutas.estantes import router

app = FastAPI(
    title="Sistema de Bodega TransCarga S.A.S.",
    description="WebService REST para gestión de bodega con Pilas LIFO",
    version="1.0.0"
)

# Registrar el router con prefijo /api/v1
app.include_router(router, prefix="/api/v1")


# Endpoint raíz
@app.get("/")
def bienvenida():
    """
    Endpoint de bienvenida del sistema.
    """
    return {
        "sistema": "Sistema de Inventario de Bodega",
        "empresa": "TransCarga S.A.S.",
        "version": "1.0.0",
        "docs": "/docs"
    }