class NodeD:

    __slots__ = ("__value", "__next", "__prev")

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise TypeError("El valor no debe ser None/Null.")
        
        self.__value = new_value

    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, NodeD):
            raise TypeError("El next de un nodo solo puede ser None u otro nodo.")
        
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev):
        if new_prev is not None and not isinstance(new_prev, NodeD):
            raise TypeError( "El prev de un nodo solo puede ser None u otro nodo.")
        
        self.__prev = new_prev


    def __str__(self):
        return str(self.__value)
    

