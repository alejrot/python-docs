

# Procesos (*proccess*)

Los procesos (***process***) son **"programas" unitarios** cuya ejecución es gestionada por el sistema operativo, el cual asigna cada proceso en activo a un núcleo del procesador que esté disponible para que se encargue de ejecutarlo. Los demás procesos quedan en espera hasta que el sistema operativo los ponga en activo de nuevo, los cierre o simplemente se terminen.

Un programa completo puede estar compuesto por múltiples procesos vinculados entre sí. Esto permite:

- modularizar el programa al dividirlo en rutinas específicas;
- mejorar los tiempos de ejecución al repartir varios subprocesos del programa entre los núcleos del procesador, permitiendo la ejecución simultánea.

## Contenidos

{{ pagetree(siblings)}}




## Referencias


[Documentación oficial - Módulo `multiprocessing`](https://docs.python.org/es/3/library/multiprocessing.html)

[Learn Tutorials - Procesos e hilos](https://learntutorials.net/es/python/topic/4110/procesos-e-hilos)

[El Blog Python - Crea múltiples procesos en python](https://elblogpython.com/tutoriales-python/crea-multiples-procesos-en-python/)
