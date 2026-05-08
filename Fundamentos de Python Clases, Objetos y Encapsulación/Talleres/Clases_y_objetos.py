# Creamos la clase Libro
# Una clase es como un molde para crear objetos
class Libro:

    # Método constructor
    # Se ejecuta automáticamente cuando creamos un objeto
    def __init__(self, titulo, autor, paginas):

        # Guardamos el título del libro
        self.titulo = titulo

        # Guardamos el autor del libro
        self.autor = autor

        # Guardamos el número de páginas
        self.paginas = paginas

        # El libro inicia disponible
        # True significa que sí se puede prestar
        self.disponible = True

    # Método para prestar el libro
    def prestar(self):

        # Verificamos si el libro está disponible
        if self.disponible:

            # Cambiamos el estado a False
            # False significa que el libro ya fue prestado
            self.disponible = False

            # Retornamos un mensaje
            return f"El libro '{self.titulo}' ha sido prestado."

        else:
            # Si ya estaba prestado, mostramos este mensaje
            return f"El libro '{self.titulo}' no está disponible."

    # Método para devolver el libro
    def devolver(self):

        # Verificamos si el libro NO está disponible
        # not significa "no"
        if not self.disponible:

            # Volvemos a poner el libro como disponible
            self.disponible = True

            # Mensaje de devolución
            return f"El libro '{self.titulo}' ha sido devuelto."

        else:
            # Si el libro ya estaba disponible
            return f"El libro '{self.titulo}' ya estaba en la biblioteca."

    # Método para mostrar la información del libro
    def informacion(self):

        # Operador ternario
        # Si disponible es True -> "Disponible"
        # Si disponible es False -> "Prestado"
        estado = "Disponible" if self.disponible else "Prestado"

        # Retornamos toda la información en texto
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}\n"
            f"Estado: {estado}"
        )


# Función principal
def main():

    # Creamos el primer objeto libro
    libro1 = Libro(
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
        863
    )

    # Creamos el segundo objeto libro
    libro2 = Libro(
        "Cien años de soledad",
        "Gabriel García Márquez",
        471
    )

    # Mostramos la información inicial
    print("=== Información inicial de los libros ===")

    # Llamamos el método informacion()
    print(libro1.informacion())

    print("\n")

    print(libro2.informacion())

    print("\n")

    # Prestamos los libros
    print("=== Préstamo de libros ===")

    # Llamamos el método prestar()
    print(libro1.prestar())
    print(libro2.prestar())

    print("\n")

    # Intentamos prestar otra vez el mismo libro
    print("=== Intento de préstamo de libros ya prestados ===")

    print(libro1.prestar())

    print("\n")

    # Mostramos la información después del préstamo
    print("=== Información después del préstamo ===")

    print(libro1.informacion())

    print("\n")

    # Devolvemos el libro
    print("=== Devolución de libros ===")

    print(libro1.devolver())

    print("\n")

    # Intentamos devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")

    print(libro1.devolver())

    print("\n")

    # Mostramos la información final
    print("=== Información final de los libros ===")

    print(libro1.informacion())

    print("\n")

    print(libro2.informacion())


# Esta condición verifica si el archivo se ejecuta directamente
if __name__ == "__main__":

    # Ejecutamos la función principal
    main()