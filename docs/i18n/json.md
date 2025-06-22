
# Archivos JSON

`python-i18n` también soporta la lectura de archivos en formato JSON.
Estos archivos guardan los datos como diccionarios exclusivamente.
[Más sobre los archivos JSON](../archivos/json.md)

## Utilización

Se soportan todas las opciones disponibles para archivos YAML
y se usan las mismas funciones tanto para configurar como para leer.

Sin embargo
los archivos JSON 
no son detectados por defecto y
y deben ser habilitados para ser leidos
con ayuda de la función `set()`:

```python title="JSON - habilitación"
# habilitar JSON
i18n.set('file_format', 'json')
```

Los archivos JSON deben tener una sintaxis como esta:

```json title="JSON - archivos de traducción"
{
    "es": {
        "hi": "Hola %{name}!",
        "gb": "Goodbye!",
        "mails": {
            "zero": "No tienes ningún correo.",
            "one": "Tienes un nuevo correo.",
            "few": "Sólo tienes %{count} correos nuevos.",
            "many": "Tienes %{count} correos nuevos."
        }
    }
}
```

El uso de comillas dobles es obligatorio,
como también es obligatorio estructurar
los campos y sus valores mediante llaves.
No se admite el uso de comentarios.



## `locale` tácito


Los archivos de traducciones no siempre traen internamente indicado el campo `locale` (idioma).
Para estos casos
se necesita habilitar
la opción `skip_locale_root_data`:

```python title='skip locale from root'
i18n.set('skip_locale_root_data', True)
```
De esta manera los archivos JSON son simplificados:


```json title="JSON - archivos de traducción (locale tácito)"
{
    "hi": "Hola %{name}!",
    "gb": "Hasta luego!",
    "mails": {
        "zero": "No tienes ningún correo.",
        "one": "Tienes un nuevo correo.",
        "few": "Sólo tienes %{count} correos nuevos.",
        "many": "Tienes %{count} correos nuevos."
    }
}
```

## Demo - cliente de correo

Se muestra una implementación completa del demo usado como ejemplo.

!!! example "demo JSON - completo"

    ``` title="demo JSON - arbol de archivos"
    ├── traducciones
    │   ├── demo.en.json
    │   └── demo.es.json
    └── traducir.py
    ```


    ```json title="demo JSON - traduccion al español"
    {
        "hi": "Hola %{name}!",
        "gb": "Hasta luego!",
        "mails": {
            "zero": "No tienes ningún correo.",
            "one": "Tienes un nuevo correo.",
            "few": "Sólo tienes %{count} correos nuevos.",
            "many": "Tienes %{count} correos nuevos."
        }
    }
    ```
    ```json title="demo JSON - traduccion al español"
    {
        "hi": "Hello %{name}!",
        "gb": "Goodbye!",
        "mails": {
            "zero": "You haven't any new mail.",
            "one": "You have a new mail.",
            "few": "You only have %{count} new mails.",
            "many": "You have %{count} new mails."
        }
    }
    ```


    ```py title="demo JSON - rutina completa"
    import i18n


    i18n.set('file_format', 'json')
    i18n.set('skip_locale_root_data', True)

    i18n.load_path.append('traducciones/')

    i18n.set('locale', 'es')
    i18n.set('fallback', 'en')


    text = i18n.t('demo.hi', name="Bob")
    print(text)
    text = i18n.t('demo.mails', count=0)
    print(text)
    text = i18n.t('demo.gb')
    print(text)
    ```