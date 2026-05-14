class NodoCaja:
    """
    Representa un nodo en la pila de cajas.
    Cada nodo contiene los datos de una caja y apunta al nodo de abajo (hacia la base).
    """
    
    def __init__(self, caja: dict):
        """
        Inicializa un nodo con los datos de una caja.
        
        Args:
            caja: dict con los datos de la caja
        """
        self.caja = caja
        self.siguiente = None  # Apunta hacia abajo (hacia la base)
    
    def __repr__(self):
        """
        Retorna una representación del nodo en formato Nodo(codigo→siguiente).
        
        Returns:
            str con el formato del nodo
        """
        codigo = self.caja.get('codigo', 'SIN_CODIGO')
        return f"Nodo({codigo})"


class PilaEstante:
    """
    Implementa una pila de cajas para un estante de bodega.
    La pila crece hacia abajo (tope en la parte superior).
    """
    
    CAPACIDAD_MAXIMA = 10
    
    def __init__(self, id_estante: str, ubicacion: str):
        """
        Inicializa un estante vacío.
        
        Args:
            id_estante: str identificador del estante
            ubicacion: str ubicación del estante en la bodega
        """
        self.id_estante = id_estante
        self.ubicacion = ubicacion
        self.tope = None
        self.tamanio = 0
    
    def esta_vacio(self) -> bool:
        """
        Verifica si la pila está vacía.
        
        Complejidad temporal: O(1)
        
        Returns:
            bool True si la pila está vacía, False en caso contrario
        """
        return self.tope is None
    
    def esta_lleno(self) -> bool:
        """
        Verifica si la pila está llena (alcanzó capacidad máxima).
        
        Complejidad temporal: O(1)
        
        Returns:
            bool True si la pila está llena, False en caso contrario
        """
        return self.tamanio >= self.CAPACIDAD_MAXIMA
    
    def push(self, caja: dict) -> None:
        """
        Agrega una caja al tope de la pila.
        
        Complejidad temporal: O(1)
        
        Args:
            caja: dict con los datos de la caja a agregar
            
        Raises:
            ValueError: si el estante está lleno
        """
        if self.esta_lleno():
            raise ValueError('Estante lleno')
        
        nuevo_nodo = NodoCaja(caja)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamanio += 1
    
    def pop(self) -> dict:
        """
        Retira y retorna la caja del tope de la pila.
        
        Complejidad temporal: O(1)
        
        Returns:
            dict con los datos de la caja retirada
            
        Raises:
            ValueError: si el estante está vacío
        """
        if self.esta_vacio():
            raise ValueError('Estante vacío')
        
        caja_retirada = self.tope.caja
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return caja_retirada
    
    def peek(self) -> dict:
        """
        Retorna los datos de la caja del tope sin modificar la pila.
        
        Complejidad temporal: O(1)
        
        Returns:
            dict con los datos de la caja en el tope
            
        Raises:
            ValueError: si el estante está vacío
        """
        if self.esta_vacio():
            raise ValueError('Estante vacío')
        
        return self.tope.caja
    
    def listar(self) -> list:
        """
        Recorre la pila de tope a base y retorna lista de todos los dicts de cajas.
        No modifica la pila.
        
        Complejidad temporal: O(n) donde n es el tamaño de la pila
        
        Returns:
            list de dicts con los datos de todas las cajas desde tope hasta base
        """
        cajas = []
        nodo_actual = self.tope
        
        while nodo_actual is not None:
            cajas.append(nodo_actual.caja)
            nodo_actual = nodo_actual.siguiente
        
        return cajas
    
    def peso_total(self) -> float:
        """
        Suma el campo peso_kg de cada caja en la pila y retorna el total.
        
        Complejidad temporal: O(n) donde n es el tamaño de la pila
        
        Returns:
            float con el peso total en kilogramos
        """
        peso = 0.0
        nodo_actual = self.tope
        
        while nodo_actual is not None:
            peso += nodo_actual.caja.get('peso_kg', 0.0)
            nodo_actual = nodo_actual.siguiente
        
        return peso
    
    def representacion_nodos(self) -> str:
        """
        Retorna una representación en string de los nodos desde tope a base.
        Formato: 'Nodo(CJA-0001) → Nodo(CJA-0002) → NULL'
        o 'NULL (pila vacía)' si está vacía.
        
        Complejidad temporal: O(n) donde n es el tamaño de la pila
        
        Returns:
            str con la representación de la pila
        """
        if self.esta_vacio():
            return 'NULL (pila vacía)'
        
        representacion = []
        nodo_actual = self.tope
        
        while nodo_actual is not None:
            representacion.append(repr(nodo_actual))
            nodo_actual = nodo_actual.siguiente
        
        return ' → '.join(representacion) + ' → NULL'

