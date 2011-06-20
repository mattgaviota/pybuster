Archivo de procedimientos
=========================

En las tablas
-------------

Dado que web2py genera de manera automatica los id para cada registro dentro de
la tabla, no son necesarios esos campos, seria necesario una clave secundaria,
para:

    -   Empleados
    -   Clientes

se puede tomar como clave, ademas del id existente como clave primaria y
autonumerico, el DNI, condicionando que sea unico y distinto de vacio.

Normalizando
------------

Hay que ver si es necesario poner otras tablas para evitar la redundancia de
datos, por el momento la unica surgida es la tabla Genero.

