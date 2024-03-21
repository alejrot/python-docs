# 5 COSAS EXTRAÑAS en PYTHON
https://www.youtube.com/watch?v=0IjLBjatT5Y

Conexion a bases de datos con SQL Server
https://youtu.be/BzsF1cG6JJU?list=PLWYKfSbdsjJg9-Knrk6iKbM-u6Z33zavD
REVISAR

Se trabaja en base al paquete pyodbc. También debe instalarse un driver del lenguaje de la base de datos elegida.

Ejemplo: una rutina de lectura de base de datos ubicada localmente.

```python
import pyodbc
<descriptor> = pyodbc.connect( 
	'Driver={<nombre_driver_base_datos>}'; 
	'Server=localhost;'
	'Database=<nombre_base_datos>;'
	'UID=<nombre_administrador>;'
	'PWD=<contraseña>;')
cursor = conn.cursor()
cursor.execute(‘select * from persona’)
```
