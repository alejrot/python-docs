

# Archivos YAML

Las traducciones se suelen guardar
en archivos YAML.
Esto archivos permiten definir diccionarios y listas
fácilmente mediante indentado.
[Más sobre los archivos YAML](../archivos/pyyaml.md)

## Lectura de archivos

El directorio de referencia para la traducción
se ingresa con el método `append()`
de la función `load_path()`: 

```python title="YAML - Carpeta de traducciones"
# directorio con traducciones
i18n.load_path.append('.')        # directorio actual
i18n.load_path.append('carpeta_traducciones/')   # subdirectorio
```

Lo habitual es colocar los archivos de traducciones
en una misma carpeta.

## Estructura de programa


Los archivos con las traducciones se nombran con la siguiente convención: `{nombre_archivo}.{locale}.{format}.`

Por ejemplo un
un programa demo
con traducciones al inglés y al español
podría tener una estructura como esta:

```bash title="YAML- arbol de archivos"
.
├── traducciones
│   ├── demo.en.yml
│   └── demo.es.yml
└── demo.py
```

donde las traducciones al inglés
se guardan en el archivo `demo.en.yml`
y las traducciones al español
están en el archivo `demo.es.yml`. 

Las traducciones de un mismo idioma
se pueden repartir en varios archivos,
en caso de considerarse necesario.


## Formato en YAML

Las traducciones se guardan en los archivos YAML
como diccionarios
con la siguiente convención:
primero se el lenguaje implementado (`en`, `es`, etc)
como primera clave
y como valores internos se guardan los pares campo - traducción.

Por ejemplo,
en el archivo de traducciones
para el inglés
se especifica la clave `en` y bajo ésta
se incluyen los campos `hi` y `gb`
con sus textos respectivos:

```yml title="YAML - traducción al inglés"
# archivo 'demo.en.yml'
en:
  hi: Hello!
  gb: Goodbye!
```

En el archivo de traducciones
para el español
se agrega la clave `es` y bajo ésta
se incluyen los mismos campos:

```yml title="YAML - traducción al español"
# archivo 'demo.es.yml'
es: 
  hi: Hola!
  gb: Hasta luego!
```

Este mecanismo se aplica con todos los archivos de traducciones implementados.

!!! hint "Texto sin comillas"

    YAML no obliga a usar comillas para delimitar claves ni valores.
    Su uso es opcional.


## Lectura


La lectura de traducciones se realiza nuevamente con la función `t()`.
Si se elige como directorio de referencia la carpeta de traducciones: 

```python title="YAML - cargar carpeta de traducciones"
i18n.load_path.append('traducciones/')   # subdirectorio
```

entonces el argumento de entrada de `t()`
toma la forma `{nombre_archivo}.{campo}`:

```python title="YAML - usar traducciones"
text = i18n.t('demo.hi')
print(text)
text = i18n.t('demo.gb')
print(text)
```

es decir se omite la abreviación de idioma y la extensión `.yml`.


Si en cambio se carga todo el directorio del programa: 

```python title="YAML - cargar carpeta de programa"
i18n.load_path.append('.')
```

entonces la lectura de traducciones
tiene como formato de argumento 
`{nombre_carpeta}.{nombre_archivo}.{campo}`
:


```python title="YAML - usar traducciones"
text = i18n.t('traducciones.demo.hi')
print(text)
text = i18n.t('traducciones.demo.gb')
print(text)
```


!!! tip "Traducciones faltantes"

    Si falta alguno de los archivos de idioma
    entonces simplemente se carga la traducción de `fallback`.


!!! example "Ejemplo - rutina completa"


    === "Carga de subcarpeta"

        ```py
        # importacion
        import i18n

        # referencia a la carpeta de traducciones
        i18n.load_path.append('traducciones/')

        # eleccion de idiomas
        i18n.set('locale', 'es')
        i18n.set('fallback', 'en')

        # lectura de traduccion
        text = i18n.t('demo.hi')
        print(text)
        text = i18n.t('demo.gb')
        print(text)
        ```

    === "Carga de directorio raiz"

        ```py
        # importacion
        import i18n

        # referencia a la carpeta del programa
        i18n.load_path.append('.')

        # eleccion de idiomas
        i18n.set('locale', 'es')
        i18n.set('fallback', 'en')

        # lectura de traduccion
        text = i18n.t('traducciones.demo.hi')
        print(text)
        text = i18n.t('traducciones.demo.gb')
        print(text)
        ```


## Placeholders 

Los placeholders mantienen la misma notación que en los *scripts*:

```yaml title="YAML - crear placeholders"
# archivo 'demo.es.yml' (español)
es: 
  hi: Hola %{name}!     # placeholder 'name'
```

y se llaman de la misma manera,
esta vez inclkuyendo el nombre de archivo:

```python title="YAML - cargar placeholders"
text = i18n.t('demo.hi', name="Bob")
print(text)
```

## Pluralización

La pluralización se implementa en archivos YAML
adaptando el diccionario de opciones al formato YAML.
En él se crean las claves `zero`, `one`, `few` y `many`
con sus respectivos valores.
La variable de control sigue siendo `count`
y se reutiliza el formato de *placeholder*.


En el ejemplo previo del contador de correos,
la definición quedaría así

```yaml title="YAML - crear pluralización"
# archivo 'demo.es.yml' (español)
es: 
  mails:
    'zero': No tienes ningún correo nuevo.
    'one':  Tienes un nuevo correo.
    'few':  Sólo tienes %{count} correos nuevos.
    'many': Tienes %{count} correos nuevos.
```

y la orden de lectura incluye al nombre de archivo:

```py title="YAML - leer pluralizacion"
print( i18n.t('demo.mails', count=6) )  # caso 'many' (6 o mayor)
```

## Demo - cliente de correo

Se muestra una implementación completa del demo usado como ejemplo.

!!! example "demo YAML - completo"


    ```bash title="demo YAML - arbol de archivos"
    .
    ├── traducciones
    │   ├── demo.en.yml
    │   └── demo.es.yml
    └── demo.py
    ```

    ```yaml title="demo YAML - traduccion al español"
    # archivo 'demo.es.yml' (español)
    # carpeta 'traducciones'
    es: 
      hi: Hola %{name}!
      gb: Hasta luego!
      mails:
        zero: No tienes ningún correo nuevo.
        one:  Tienes un nuevo correo.
        few:  Sólo tienes %{count} correos nuevos.
        many: Tienes %{count} correos nuevos.
    ```

    ```yaml title="demo YAML - traduccion al inglés"
    # archivo 'demo.en.yml' (inglés)
    # carpeta 'traducciones'
    en: 
      hi: Hello %{name}!
      gb: Goodbye!
      correos:    
        zero: You haven't any new mail.
        one:  You have a new mail.
        few:  You only have %{count} new mails.
        many: You have %{count} new mails.
    ```

    ``` py title="demo YAML - rutina completa"
    import i18n


    i18n.load_path.append('traducciones/')

    i18n.set('locale', 'es')
    i18n.set('fallback', 'en')


    text = i18n.t('traducciones.demo.hi', name="Bob")
    print(text)
    text = i18n.t('traducciones.demo.mails', count=0)
    print(text)
    text = i18n.t('traducciones.demo.gb')
    print(text)
    ```