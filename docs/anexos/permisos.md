---
tags:
  - Archivos
  - Carpetas
---

# Permisos de usuario



## Permisos por acciones

Los permisos de usuario se asignan mediante por un numero representado en sistema
binario de tres digitos. 


Cada dígito es una composición de *booleanos*
(valores binarios)
que otorgan permisos para leer (*read*),
escribir (*write*) 
y ejecutar (*execute*), 
en ese mismo orden: `r-w-x`.
El número binario puede ser convertido a octal, decimal o hexadecimal para una lectura más fácil.


Los valores numéricos equivalentes para cada permiso aslado son:

|Permiso |binario|octal| hexadecimal| decimal|
|:--- |:---:|:----:|:---:|:---:
| Leer  (r)  |`0b100 `| `0o4` | `0h4` | `4`|
| Escribir (w) |`0b010` | `0o2` | `0h2` | `2` | 
| Ejecutar (x) |`0b001` | `0o1` | `0h1` | `1`|

Los numeros de los permisos se construyen combinando lógicamente los números previos.
Esto equivale en la práctica a sumar los números equivalentes para cada permiso.

Ejemplos:

|Permiso combinado |binario|octal| hexadecimal| decimal
|:--- |:---:|:----:|:---:|:---:|
| Sólo lectura (r)  |0b100 | 0o4 | 0h4 | 4 |
| Lectura y escritura (r+w) |0b110 | 0o6 | 0h6 | 6| 
| Sólo ejecucion  (x) |0b001 | 0o1 | 0h1 | 1 |
| Lectura, escritura y ejecucion  (r+w+x) |0b111 | 0o7 | 0h7 | 7 | 


## Permisos para usuarios

Los digitos con los permisos se asignan con el siguiente orden de usuarios:

- usuario actual;
- grupo del usuario actual;
- todos los usuarios.

Notacion resumida:

|Usuario|Grupo| Todos|
|:---:|:---:|:---:|
| `rwx` | `rwx` | `rwx `|

!!! info "Usuario **root**"
    El usuario administrador o raíz (*root*) del sistema siempre
    tiene **todos los derechos posibles**,
    por ello no se le asignan permisos especificos.



## Ejemplos

!!! example "Ejemplo 1: Permisos diferenciados"


    - usuario propietario con todos los permisos; 
    - grupo del propietario con lectura y escritura;  
    - accesos de sólo lectura para terceros.

    Número permisos:
    
    |sistema | numero permisos|
    |:---|:---|
    | binario | `0o111110100`|  
    | octal | `0o764` |
    | hexadecimal | `0x764`| 
    | decimal | `764` |

!!! example "Ejemplo 2: Sólo ejecución para todos"

    Número permisos:


    |sistema | numero permisos|
    |:---|:---|
    | binario | `0o001001001`|  
    | octal | `0o111` |
    | hexadecimal | `0x111`| 
    | decimal | `111` |


!!! example "Ejemplo 3: Todos los permisos para todos los usuarios (mala práctica)"

    Número permisos:

    |sistema | numero permisos|
    |:---|:---|
    | binario | `0o111111111`|  
    | octal | `0o777` |
    | hexadecimal | `0x777`| 
    | decimal | `777` |


