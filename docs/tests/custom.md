# Excepciones personalizadas


Las excepciones personalizadas se crean
como clases
a partir de la excepción genérica `Exception`:

```py
class ExcepcionCustom(Exception):
    pass 
```
Esta excepción puede ser disparada con ayuda de la cláusula `raise`:

```py
raise ExcepcionCustom
raise ExcepcionCustom()
```





