## [Volver](../README#traducciones---python-i18n)

# Traducciones - python-i18n

### Contenido

- [python-i18n](#python-i18n)
- [Instalación](#instalación)
- [Importación](#importación)
- [Traduccion desde script](#traduccion-desde-script)
- [Set y Fallback](#set-y-fallback)
- [Traduccion desde archivos YML](#traduccion-desde-archivos-yml)
- [Placeholders](#placeholders)
- [Pluralizacion](#pluralizacion)
- [Traduccion desde archivos JSON](#traduccion-desde-archivos-json)
- ['skip locale from root'](#skip-locale-from-root)
- [Ejemplo aplicado - Lectura JSON](#ejemplo-aplicado---lectura-json)


## python-i18n

i18n es una abreviación de 'InternationalizatioN' (18 letras entre la I y la N). **python-i18n** es es una de las implementaciones de Python para las traducciones i18n.

Documentación: 

https://pypi.org/project/python-i18n/


## Instalación

i18n se instala fácilmente desde PIP:

```python
pip install python-i18n
```

Si se prefiere guardar las traducciones en formato YAML el paquete requerido es el siguiente:

```python
pip install python-i18n[YAML]
```


## Importación

El paquete debe importarse para su uso:
```python
import i18n
```


## Traduccion desde script

Las traducciones se pueden cargar con la función *add_tranlation()* en forma de pares *campo - valor*, ambos en formato string:

```python
i18n.add_translation('hello','hola')
```
en tanto que las traducciones se realizan con la función *t()*:

```python
campo = 'hello'
traducido = i18n.t(campo)
print(traducido)
```
Para cada par campo-valor se puede asignar una abreviación de lenguaje, de modo de permitir soporte simultáneo a múltiples idiomas:
```python
i18n.add_translation('hello','good morning', locale='en')   # 'en' : inglés (english) 
i18n.add_translation('hello','buenos días', locale='es')    # 'es' : español
```

Las etiquetas 'es' y 'en' son etiquetas de idioma definidas por el desarrollador. Éstas no vienen predefinidas por el paquete, aunque convensionalmente se usan las abreviaciones en inglés de los lenguajes. 


##  Set y Fallback

El lenguaje prioritario se establece on la función *set()*:
```python 
# Lenguaje preferido
i18n.set('locale', 'es')   # español
```
en tanto que la opción alternativa se establece con la función *fallback()*:

```python 
# alternativa : 'fallback'
i18n.set('fallback', 'en')  # inglés
```

Esto permite completar los campos para los cuales no existan traducciones en el lenguaje preestablecido. Como alternativa habitualmente se elige el inglés.


## Traduccion desde archivos YML

Las traducciones se guardan en archivos YML en una misma carpeta. El directorio se carga con el método *append()* de la función *load_path()*: 

```python
# directorio con traducciones
i18n.load_path.append('.')        # directorio actual
i18n.load_path.append('local/')   # subdirectorio 'local'
```

Los archivos tienen en su nombre un nombre de espacio (*namespace*), la abreviación del idioma (*locale*) y el formato del archivo (*format*):

    {namespace}.{locale}.{format}

Ejemplo: archivo para el inglés con los campos 'hi' y 'gb'
```yml
# archivo 'foo.en.yml' (inglés)
# carpeta 'local'
en: 
  hi: Hello Word!
  gb: Goodbye!
```
Ejemplo: archivo para el español con el campo único 'hi'
```yml
# archivo 'foo.es.yml' (español)
# carpeta 'local'
es: 
  hi: Hola Mundo!
    # campo 'gb' faltante
```
Las traducciones de estos archivos se cargan con el nombre del descriptor de archivo y el nombre del campo elegido. 

Ejemplo: 

Si se necesita la traduccion al inglés:
```python 
# traducción al ingles
i18n.set('locale', 'en')    
traducido = i18n.t('foo.hi')
print(traducido)   
traducido = i18n.t('foo.gb')
print(traducido) 
```
Si en cambio se necesita la traduccion al español (incompleta):
```python 
# traducción al español
i18n.set('locale', 'es')    
traducido = i18n.t('foo.hi')
print(traducido)    
#campo faltante
traducido = i18n.t('foo.gb')
print(traducido)    # resultado en ingles
```
en este caso la traducción incluirá los campos faltantes en inglés, por ser éste el idioma alternativo elegido.

Y si en cambio se necesita la traducción a un lenguaje no implementado, como por ejemplo el polaco:
```python 
# traducción al polaco (faltante)
i18n.set('locale', 'pl')    
traducido = i18n.t('foo.hi')
print(traducido)   # resultado en ingles
```
en este caso simplemente se traduce al inglés.

**Importante:** si los archivos de traducción se guardan en *subdirectorios* entonces los nombres de éstos también cuentan como *nombre de espacio*


## Placeholders

Se pueden implementar parámetros (campos variables) dentro de las traducciones, éstos son llamados ***placeholders*** o *marcadores*:
```python 
# campo 'name' variable 
i18n.add_translation('hi', 'Hola %{name} !')
```

Los parámetros variables se asignan como argumento para la función *t()* en el momento de traducir:
```python 
traducido = i18n.t('hi', name='Bob')    # 'Hola Bob!'
```

## Pluralizacion

El ***placeholder***, si éste tiene valor numérico, puede usarse para elegir entre varias traducciones posibles.

El valor numérico se pasa con la propiedad *'count'*. Las opciones de traducción se enmarcan entre llaves y hay cuatro opciones:

|  Opcion |   Valor   |
|:------:|:-----:|
|'zero' |     0     |
|'one'  | 1         |
|'few'  | 2 a 5     |
|'many' | 6 o mayor |

Ejemplo: conteo de emails

```python 
i18n.add_translation('numero', {
    'zero': 'No tienes ningún correo.',
    'one': 'Tienes un nuevo correo.',
    'few': 'Sólo tienes %{count} correos.',
    'many': 'Tienes %{count} correos nuevos.'
})
```
La lectura de la traducción se hace asignándole el valor a la propiedad *count*:

```python 
print( i18n.t('numero', count=0) )  # caso 'zero'(0)
print( i18n.t('numero', count=1) )  # caso 'one' (1)
print( i18n.t('numero', count=5) )  # caso 'few' (2 a 5)
print( i18n.t('numero', count=6) )  # caso 'many' (6 o mayor)
```



## Traduccion desde archivos JSON

Los archivos JSON deben ser habilitados para ser leidos por el paquete:
```python
# habilitar JSON
i18n.set('file_format', 'json')
```


## 'skip locale from root'

Los archivos de traducciones no siempre traen internamente indicado el campo *locale* (idioma).
Para estos casos se habilita la opción *'skip_locale_root_data'*:

```python
i18n.set('skip_locale_root_data', True)
```
## Ejemplo aplicado - Lectura JSON

Archivo JSON de traducciones al inglés, carpeta 'local':
```JSON
// archivo inglés: 'foo.en.json'
// carpeta 'local'
{
   "key-1": "Welcome %{firstname} %{lastname}!",
   "key-2": "Good morning!",
   "key-3": "Bye!"
}
```
Archivo JSON de traducciones al español, carpeta 'local':
```JSON
// archivo español: 'foo.es.json'
// carpeta 'local'
{
    "key-1": "Bienvenido %{firstname} %{lastname}!",
    "key-2": "Buenos días!",
    "key-3": "Adiós!"
}
```
Código de aplicación:

```python
i18n.set('file_format', 'json')

i18n.load_path.append('local/')

i18n.set('fallback', 'en')  # Ultima opcion
i18n.set('skip_locale_root_data', True)


# prueba español
i18n.set('locale', 'es')  
print( i18n.t('foo.key-1',firstname='Aitor', lastname='Tilla'))
print( i18n.t('foo.key-2'))
print( i18n.t('foo.key-3'))

# prueba español
i18n.set('locale', 'en')  
print( i18n.t('foo.key-1',firstname='Aquiles', lastname='Brinco'))
print( i18n.t('foo.key-2'))
print( i18n.t('foo.key-3'))
```





----
----
----

## [Inicio](#traducciones---python-i18n) 

## [Volver](../README#traducciones---python-i18n)






