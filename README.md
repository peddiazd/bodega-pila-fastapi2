# Sistema de Inventario de Bodega — TransCarga S.A.S.

WebService REST construido con FastAPI que modela los estantes de una bodega como Pilas LIFO con Nodos enlazados.

## Stack tecnológico
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic v2

## Instalación y ejecución

1. Clonar el repositorio
   git clone https://github.com/tu-usuario/bodega-pila-fastapi2

2. Crear entorno virtual
   python -m venv venv
   source venv/bin/activate

3. Instalar dependencias
   pip install -r requirements.txt

4. Ejecutar el servidor
   uvicorn main:app --reload --port 8000

5. Abrir Swagger UI
   http://localhost:8000/docs

## Endpoints disponibles

| Método | Ruta | Operación |
|--------|------|-----------|
| POST | /api/v1/estantes | Crear estante |
| POST | /api/v1/estantes/{id}/cajas | PUSH — Ingresar caja |
| DELETE | /api/v1/estantes/{id}/cajas/tope | POP — Retirar caja |
| GET | /api/v1/estantes/{id}/cajas/tope | PEEK — Ver tope |
| GET | /api/v1/estantes/{id}/cajas | Listar cajas |
| GET | /api/v1/estantes/{id} | Estado estante |
| GET | /api/v1/estantes | Listar bodega |
| GET | /api/v1/estantes/{id}/nodos | Ver nodos |

## Universidad Cooperativa de Colombia
Ingeniería de Sistemas — Estructura de Datos — 2025