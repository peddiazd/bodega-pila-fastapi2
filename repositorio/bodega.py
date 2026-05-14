from estructuras.pila import PilaEstante

# Variables globales del repositorio
_bodega: dict[str, PilaEstante] = {}
_contador_cajas: int = 0


def generar_codigo_caja() -> str:
    """
    Genera un código único para una caja incrementando el contador global.
    
    Complejidad temporal: O(1)
    
    Returns:
        str con formato 'CJA-0001', 'CJA-0047', etc.
    """
    global _contador_cajas
    _contador_cajas += 1
    return f"CJA-{_contador_cajas:04d}"


def get_bodega() -> dict:
    """
    Retorna el diccionario de estantes de la bodega.
    
    Complejidad temporal: O(1)
    
    Returns:
        dict con los estantes de la bodega
    """
    return _bodega


def get_estante(id_estante: str) -> PilaEstante | None:
    """
    Obtiene un estante de la bodega por su identificador.
    
    Complejidad temporal: O(1)
    
    Args:
        id_estante: str identificador del estante
        
    Returns:
        PilaEstante si existe, None en caso contrario
    """
    return _bodega.get(id_estante)


def estante_existe(id_estante: str) -> bool:
    """
    Verifica si un estante existe en la bodega.
    
    Complejidad temporal: O(1)
    
    Args:
        id_estante: str identificador del estante
        
    Returns:
        bool True si el estante existe, False en caso contrario
    """
    return id_estante in _bodega


def crear_estante(id_estante: str, ubicacion: str) -> PilaEstante:
    """
    Crea un nuevo estante en la bodega.
    
    Complejidad temporal: O(1)
    
    Args:
        id_estante: str identificador del estante
        ubicacion: str ubicación del estante en la bodega
        
    Returns:
        PilaEstante el estante creado
        
    Raises:
        ValueError: si el identificador del estante ya existe
    """
    if estante_existe(id_estante):
        raise ValueError(f'Estante con ID {id_estante} ya existe')
    
    nuevo_estante = PilaEstante(id_estante, ubicacion)
    _bodega[id_estante] = nuevo_estante
    return nuevo_estante

