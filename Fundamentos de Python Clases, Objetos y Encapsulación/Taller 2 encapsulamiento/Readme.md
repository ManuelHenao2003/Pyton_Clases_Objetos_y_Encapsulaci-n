rimero se creó la clase CuentaBancaria, la cual representa una cuenta bancaria con un titular y un saldo. Dentro del constructor __init__ se definieron los atributos privados _titular y _saldo. Se utilizaron guiones bajos al inicio de los nombres para indicar que estos atributos no deberían modificarse directamente desde fuera de la clase.

Después se implementaron propiedades usando @property. La propiedad titular se dejó como solo lectura, permitiendo únicamente consultar el nombre del titular, pero no modificarlo directamente. Esto ayuda a proteger la información del usuario.

También se creó la propiedad saldo, que permite consultar y modificar el saldo de forma controlada. Para esto se utilizó un método setter con @saldo.setter, donde se agregó una validación que impide asignar valores negativos. Si se intenta colocar un saldo menor que cero, el programa genera un error ValueError con el mensaje “El saldo no puede ser negativo”.

Además, se añadieron métodos para manejar operaciones bancarias. El método depositar(cantidad) aumenta el saldo únicamente si la cantidad ingresada es positiva. Si el depósito es válido devuelve True, y si no lo es devuelve False.

El método retirar(cantidad) permite retirar dinero solamente si la cuenta tiene fondos suficientes y la cantidad es positiva. Si la operación se realiza correctamente devuelve True; de lo contrario devuelve False.

Para probar la clase se creó un objeto llamado cuenta1 con un titular y un saldo inicial. Luego se realizaron operaciones de depósito y retiro para verificar el funcionamiento del programa. Finalmente, también se probó la validación del saldo negativo utilizando try y except, comprobando que el sistema mostrara el error correctamente.
