# Clase CuentaBancaria
# Esta clase aplica el concepto de encapsulación
class CuentaBancaria:

    # Método constructor
    # Se ejecuta automáticamente al crear un objeto
    def __init__(self, titular, saldo=0):

        # Atributo privado del titular
        # El guion bajo (_) indica que no debería modificarse directamente
        self._titular = titular

        # Atributo privado del saldo
        self._saldo = saldo

    # Propiedad para obtener el titular
    # Solo lectura
    @property
    def titular(self):

        # Retorna el nombre del titular
        return self._titular

    # Propiedad getter para obtener el saldo
    @property
    def saldo(self):

        # Retorna el saldo actual
        return self._saldo

    # Propiedad setter para modificar el saldo
    @saldo.setter
    def saldo(self, nuevo_saldo):

        # Verificamos que el saldo no sea negativo
        if nuevo_saldo < 0:

            # Lanzamos un error si el saldo es negativo
            raise ValueError("El saldo no puede ser negativo")

        # Si el saldo es válido, lo actualizamos
        self._saldo = nuevo_saldo

    # Método para depositar dinero
    def depositar(self, cantidad):

        # Verificamos que la cantidad sea positiva
        if cantidad > 0:

            # Sumamos la cantidad al saldo
            self._saldo += cantidad

            # Retornamos True indicando éxito
            return True

        # Si la cantidad no es válida
        return False

    # Método para retirar dinero
    def retirar(self, cantidad):

        # Verificamos que haya suficiente saldo
        if cantidad > 0 and cantidad <= self._saldo:

            # Restamos el dinero del saldo
            self._saldo -= cantidad

            # Retornamos True indicando éxito
            return True

        # Si no hay suficiente dinero
        return False


# Función principal
def main():

    # Creamos una cuenta bancaria
    cuenta1 = CuentaBancaria("Manuel", 1000)

    # Mostramos el titular
    print("=== Información de la cuenta ===")
    print("Titular:", cuenta1.titular)

    # Mostramos el saldo inicial
    print("Saldo inicial:", cuenta1.saldo)

    print("\n=== Depósito ===")

    # Depositamos dinero
    if cuenta1.depositar(500):
        print("Depósito realizado correctamente")
    else:
        print("Error al depositar")

    # Mostramos el saldo actualizado
    print("Saldo actual:", cuenta1.saldo)

    print("\n=== Retiro ===")

    # Retiramos dinero
    if cuenta1.retirar(300):
        print("Retiro realizado correctamente")
    else:
        print("Fondos insuficientes")

    # Mostramos el saldo actualizado
    print("Saldo actual:", cuenta1.saldo)

    print("\n=== Intento de saldo negativo ===")

    # Intentamos asignar un saldo negativo
    try:

        # Esto generará un error
        cuenta1.saldo = -200

    except ValueError as error:

        # Mostramos el mensaje del error
        print("Error:", error)


# Verifica si el archivo se ejecuta directamente
if __name__ == "__main__":

    # Ejecutamos la función principal
    main()