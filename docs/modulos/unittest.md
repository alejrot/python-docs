
# UnitTest - Tests unitarios


## Importación


```py
import unittest
```


## Definir tests


Para evaluar la función se crea una clase hija de la clase `TestCase` y se le asigna un método por cada test unitario que se requiera hacer. 

La clase `TestCase` proporciona a sus clases hijas una serie de métodos predefinidos para verificar el buen funcionamiento de las funciones: valores y tipos de retorno correctos, excepciones disparadas ante ciertas condiciones, etc.

<!-- 
- su nombre debe empezar con 'test', de otra manera no se ejecuta;
- debe estar incorporada dentro de una clase como método
- cada método cuenta como un test separado 
-->

El formato básico es el siguiente:

```py title="Sintaxis de test" hl_lines="2 5 9"
# clase para preparar los tests
class TestComponente(unittest.TestCase):


    def test_primero(self):
        pass


    def test_segundo(self):
        pass
```

!!! warning "Nombres de tests"

    Los nombres de métodos que implementan los test unitarios siempre deben comenzar con la palabra `test`, de otra manera no serán ejecutados al final. 



### Test de funciones

Supóngase que se busca poner a prueba una función como la que sigue:

```py title="Funcion bajo prueba" hl_lines="4-5 7"
# funcion bajo prueba
def suma(a,b):
    # Excepciones ante tipos de entrada incorrectos 
    if not  isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    # retorno numérico
    return a + b
```

En este caso interesa verificar que algunas sumas de ejemplo dan valores correctos y que ante tipos de entrada incorrectos (textos, booleanos, etc ) se produce la excepción `ValueError`. Entonces se crea una clase con dos tests para verificar cada comportamiento por separado



```py 
class TestSuma(unittest.TestCase):

    # Primer test: resultados correctos 
    def test_suma(self):
        self.assertEqual(suma(5, 7), 12)
        self.assertEqual(suma(-3, -9), -12)


    # Segundo test: excepciones disparadas ante tipos de entrada erróneas
    def test_excepciones(self):
        with self.assertRaises(ValueError):
            suma("5", 7)
        with self.assertRaises(ValueError):
            suma(5, "7")
        with self.assertRaises(ValueError):
            suma(None, 7)
```


### Test de datos


Supóngase que se busca verificar la estructura y valores de un dicionario:

``` py
diccionario = { 
    "id": 31416,
    "user" : "yo"
    }
```

En este caso la clase requiere del método de inicialización `setUp()`, donde se agrega una referencia al diccionario bajo prueba. Esto permite que los tests puedan acceder a la data desde adentro del test.


``` py  hl_lines="4-6"
class TestDiccionario(unittest.TestCase):

    # Inicializacion
    def setUp(self)->None:
        # cargar data de entrada
        self.data = diccionario

    # primer test
    def test_campo_existente(self):
        # test de claves
        self.assertIn("id"  , self.data)
        self.assertIn("user", self.data)
        # self.assertIn("nombre", self.data)    # MAL: campo inexistente

    # segundo test
    def test_data_correcta(self):
        # test de valores
        self.assertEqual(self.data["id"], 31416)
        self.assertEqual(self.data["user"], "yo")
        # test de tipos
        self.assertIsInstance(self.data["id"],  int)
        self.assertIsInstance(self.data["user"], str)
```

Esta forma permite poner a prueba clases


## Ejecución

La ejecución de todos los tests definidos se realiza con la función `main()`:

``` py title="Ejecucion test"
unittest.main()
```


Por defecto la ejecución del programa se interrumpe al ejecutar esta función. Para ejecutar el test únicamente cuando la rutina se ejecute como rutina principal se agrega el condicional:

``` py title="Ejecucion test - desde main()"
if __name__ == '__main__':
    unittest.main()
```

Si se desea continuar la ejecución de la rutina tras los test se hace el argumento `exit=False` :


``` py title="Ejecucion test - Sin interrupción"
unittest.main(exit=False)

# Codigo adicional
print("Test exitoso")
```


## Decoradores

El módulo `unittest` proporciona decoradores para saltear tests o para omitir errores esperables. Los decoradores implementados en el módulo son los siguientes:


|Decorador| Uso |
|:---|:-----|
|`skip( razon )`| Omite el test |
|`skipIf( condicion , razon )`| Omite el test sólo si se cumple cierta condicion  |
|`skipUnless( condicion, razon )`| Omite el test a menos que se cumpla cierta condicion     |
|`expectedFailure`| Verifica que el error se produzca, de otro modo falla el test |


Los decoradores del módulo se usan agregándolos justo arriba de la definición del test elegido.


Por ejemplo, si en el test de la función `suma()` hay error, con el decorador `expectedFailure` se verifica que el error siga existiendo:

``` py hl_lines="3 4 8"
class TestSuma(unittest.TestCase):

    @unittest.expectedFailure
    def test_suma(self):
        # tests con resultados correctos 
        self.assertEqual(suma( 5,  7),  12)
        self.assertEqual(suma(-3, -9), -12)
        self.assertEqual(suma( 2,  3),  -6)        # Error de resultado
```


Da como resultado el mensaje:

    OK (expected failures=1)


## Métodos de test

### Uso general

|Método| Expresion equivalente |
|:---|:-----:|
|`assertEqual(a, b)` | `a == b` |
|`assertNotEqual(a, b)`|`a != b`|
|`assertTrue(x)`|`bool(x) is True `|
|`assertFalse(x)`|`bool(x) is False`|
|`assertIs(a, b)`|`a is b `|
|`assertIsNot(a, b)`| `a is not b` |
|`assertIsNone(x)` | `x is None` |
|`assertIsNotNone(x)` | `x is not None` |
|`assertIn(a, b)` |`a in b`|
|`assertNotIn(a, b)` | `a not in b` |


### Números

|Método| Expresion equivalente | Explicación |
|:---|:-----:|:---|
|`assertAlmostEqual(a, b)`|`round(a-b, 7) == 0`| Numeros (redondeados a 7 dígitos) iguales        |
|`assertNotAlmostEqual(a, b)`|`round(a-b, 7) != 0`|Numeros (redondeados a 7 dígitos) distintos        |
|`assertGreater(a, b)`|`a > b`| |
|`assertGreaterEqual(a, b)`|`a >= b`| |
|`assertLess(a, b)`|`a < b`|  |
|`assertLessEqual(a, b)`|`a <= b`| |


### Secuencias

|Método| Explicación |
|:---|:---|
|`assertRegex(s, r)`| Patrón encontrado en secuencia|
|`assertNotRegex(s, r)`|Patrón no encontrado en secuencia|


### Datos estándar

|Método| Significado |
|:---|:-----|
|`assertMultiLineEqual(a, b)`|*strings* iguales|
|`assertSequenceEqual(a, b)`|secuencias iguales|
|`assertListEqual(a, b)`|listas iguales|
|`assertTupleEqual(a, b)`|tuplas iguales|
|`assertSetEqual(a, b)`|conjuntos iguales|
|`assertDictEqual(a, b)`|diccionarios iguales|
|`assertCountEqual(a, b)`| mismos elementos en igual número, sin importar el orden|


### Clases

|Método| Expresion equivalente |
|:---|:-----:|
|`assertIsInstance(a, b)`| `isinstance(a, b)`|
|`assertNotIsInstance(a, b)` | `not isinstance(a, b)`|






### Excepciones, warnings, logs

|Método| Explicación |
|:---|:-----:|
|`assertRaises(excepcion, funcion, *args, **kargs)` | La función dispara la excepción|
|`assertRaisesRegex(excepcion, patron, funcion, *args, **kargs)` |La función dispara la excepción y el mensaje coincide con el patron |
|`assertWarns(warning, funcion, *args, **kargs)`|La función dispara la advertencia|
|`assertWarnsRegex(warning, patron, funcion, *args, **kargs)`| La función dispara la advertencia y el mensaje coincide con el patrón|
|`assertLogs(logger, nivel)` | El bloque `with` produce el log con nivel de al menos  el minimo indicado |
|`assertNoLogs(logger, nivel)` | El bloque `with` produce un log que no cumple con el nivel minimo indicado  |






## Referencias


[Documentacion oficial - Unittest](https://docs.python.org/3/library/unittest.html)

[MoureDev TV - Ruta de estudio programación | 13 - TESTING](https://youtu.be/3WFQ2grp0h0?list=PLv0dxH7HRDx_kQRNoldG7iPvydy8DyvE3)