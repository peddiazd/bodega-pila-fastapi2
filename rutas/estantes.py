from fastapi import APIRouter, HTTPException
from datetime import datetime
from modelos.caja import CajaEntrada, EstanteEntrada
from repositorio.bodega import (
    get_estante,
    crear_estante,
    estante_existe,
    get_bodega,
    generar_codigo_caja
)

router = APIRouter()


@router.post("/estantes", status_code=201)
def crear_nuevo_estante(datos: EstanteEntrada):
    if estante_existe(datos.id_estante):
        raise HTTPException(
            status_code=409,
            detail=f"El estante {datos.id_estante} ya existe en la bodega."
        )
    crear_estante(datos.id_estante, datos.ubicacion)
    return {
        "mensaje": f"Estante {datos.id_estante} creado y listo para recibir cajas.",
        "id_estante": datos.id_estante,
        "capacidad_maxima": 10,
        "cajas_actuales": 0
    }


@router.post("/estantes/{id_estante}/cajas", status_code=201)
def ingresar_caja(id_estante: str, datos: CajaEntrada):
    estante = get_estante(id_estante)
    if estante is None:
        raise HTTPException(
            status_code=404,
            detail=f"El estante {id_estante} no existe en la bodega."
        )
    caja = {
        "codigo": generar_codigo_caja(),
        "producto": datos.producto,
        "peso_kg": datos.peso_kg,
        "proveedor": datos.proveedor,
        "fecha_ingreso": datetime.now().isoformat()
    }
    try:
        estante.push(caja)
    except ValueError:
        raise HTTPException(
            status_code=409,
            detail=f"Estante {id_estante} lleno. Máximo 10 cajas por seguridad."
        )
    return {
        "mensaje": f"Caja ingresada al tope del estante {id_estante}.",
        "caja": caja,
        "cajas_en_estante": estante.tamanio
    }


@router.delete("/estantes/{id_estante}/cajas/tope", status_code=200)
def retirar_caja_tope(id_estante: str):
    estante = get_estante(id_estante)
    if estante is None:
        raise HTTPException(
            status_code=404,
            detail=f"El estante {id_estante} no existe en la bodega."
        )
    try:
        caja_retirada = estante.pop()
    except ValueError:
        raise HTTPException(
            status_code=409,
            detail=f"El estante {id_estante} está vacío. No hay cajas que retirar."
        )
    return {
        "mensaje": f"Caja retirada del tope del estante {id_estante}.",
        "caja_retirada": caja_retirada,
        "cajas_restantes": estante.tamanio
    }


@router.get("/estantes/{id_estante}/cajas/tope", status_code=200)
def ver_tope(id_estante: str):
    estante = get_estante(id_estante)
    if estante is None:
        raise HTTPException(
            status_code=404,
            detail=f"El estante {id_estante} no existe en la bodega."
        )
    try:
        caja_tope = estante.peek()
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"El estante {id_estante} está vacío."
        )
    return {
        "mensaje": f"Caja en el tope del estante {id_estante}.",
        "caja": caja_tope,
        "es_la_ultima": estante.tamanio == 1
    }


@router.get("/estantes/{id_estante}/cajas", status_code=200)
def listar_cajas(id_estante: str):
    estante = get_estante(id_estante)
    if estante is None:
        raise HTTPException(
            status_code=404,
            detail=f"El estante {id_estante} no existe en la bodega."
        )
    cajas = estante.listar()
    cajas_con_posicion = [
        {"posicion": i + 1, **caja}
        for i, caja in enumerate(cajas)
    ]
    return {
        "id_estante": id_estante,
        "total_cajas": estante.tamanio,
        "orden": "tope → base",
        "cajas": cajas_con_posicion
    }
