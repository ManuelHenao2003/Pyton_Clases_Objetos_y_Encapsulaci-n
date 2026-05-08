Primero se creó la clase Libro, que funciona como un molde para crear diferentes libros. Dentro de la clase se utilizó el método constructor __init__, el cual sirve para inicializar los atributos cada vez que se crea un objeto. Los atributos definidos fueron titulo, autor, paginas y disponible. El atributo disponible se inicializó en True porque al crear un libro se supone que está disponible en la biblioteca.

Después se crearon varios métodos para controlar el comportamiento de los libros. El método prestar() verifica si el libro está disponible; si lo está, cambia el estado a False y muestra un mensaje indicando que el libro fue prestado. Si ya estaba prestado, muestra un mensaje diciendo que no está disponible.

El método devolver() realiza el proceso contrario. Si el libro estaba prestado, cambia nuevamente el estado a True y muestra un mensaje indicando que fue devuelto. Si el libro ya estaba disponible, muestra un mensaje informando que ya se encontraba en la biblioteca.

También se creó el método informacion(), el cual sirve para mostrar todos los datos del libro, incluyendo el estado actual de disponibilidad. Este método devuelve una cadena de texto organizada con toda la información.

Para probar la clase se crearon dos objetos diferentes: uno para el libro “Don Quijote de la Mancha” y otro para “Cien años de soledad”. Luego se llamaron todos los métodos para comprobar que funcionaran correctamente, mostrando préstamos, devoluciones y el cambio de estado de los libros.
