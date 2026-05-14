from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CajaEntrada(BaseModel):
    """
    Modelo Pydantic para la entrada de una caja en la bodega.
    """
    producto: str = Field(..., min_length=2, description="Nombre del producto")
    peso_kg: float = Field(..., gt=0, description="Peso en kilogramos, debe ser mayor a 0")
    proveedor: Optional[str] = Field(None, description="Proveedor opcional")


class CajaRespuesta(CajaEntrada):
    """
    Modelo Pydantic para la respuesta de una caja registrada en la bodega.
    Incluye información adicional: código único y fecha de ingreso.
    """
    codigo: str = Field(..., description="Código único de la caja")
    fecha_ingreso: datetime = Field(..., description="Fecha y hora de ingreso de la caja")


class EstanteEntrada(BaseModel):
    """
    Modelo Pydantic para la entrada de un nuevo estante en la bodega.
    """
    id_estante: str = Field(..., min_length=3, description="Identificador del estante")
    ubicacion: str = Field(..., description="Ubicación del estante en la bodega")


class ResumenEstante(BaseModel):
    """
    Modelo Pydantic para el resumen de estado de un estante.
    """
    id_estante: str = Field(..., description="Identificador del estante")
    ubicacion: str = Field(..., description="Ubicación del estante")
    tamanio: int = Field(..., ge=0, description="Cantidad de cajas en el estante")
    esta_vacio: bool = Field(..., description="Indica si el estante está vacío")
    esta_lleno: bool = Field(..., description="Indica si el estante está lleno")
    peso_total_kg: float = Field(..., ge=0, description="Peso total en kilogramos")
