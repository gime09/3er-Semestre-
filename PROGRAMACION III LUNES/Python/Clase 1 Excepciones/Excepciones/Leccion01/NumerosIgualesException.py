class NumerosIgualesException (Exception): # Extiende de la clase {padre}
    def __init__(self, mensaje):
        self.message = mensaje
