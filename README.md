Tabla de contenidos
-   [Descripción y contexto](#descripción_y_contexto)
-   [Guía de usuario](#guía_de_usuario)
-   [Guía de instalación](#guía_de_instalación)
-   [Cómo contribuir](#cómo-contribuir)
-   [Código de conducta](#código_de_conducta)
-   [Autor](#autor)
-   [Licencia](#licencia)
-   [Limitación de responsabilidades](#limitación_de_responsabilidades)

## Descripción y contexto
<p align="justify">SCANMENOW es una herramienta de escaneo de red desarrollada con Python. Utiliza las librerías nmap, socket, os, tqdm y termcolor para escanear una red local y encontrar los hosts disponibles, escanear los puertos abiertos de un host en particular y buscar vulnerabilidades en esos puertos.</p>
## Guía de usuario

<p align="justify">Para utilizar SCANMENOW, simplemente ejecute el archivo scanmenow.py y siga las instrucciones en pantalla. La herramienta escaneará la red local y mostrará una lista de hosts disponibles. Luego, pedirá al usuario que seleccione un host y que introduzca un rango de puertos para escanear. SCANMENOW escaneará los puertos seleccionados y mostrará una lista de los puertos abiertos. Finalmente, se ofrecerá al usuario la opción de buscar vulnerabilidades en los puertos abiertos utilizando la herramienta nmap.</p>

## Guía de instalación

<p align="justify">Para utilizar SCANMENOW, asegúrese de tener instaladas las librerías nmap, socket, os, tqdm y termcolor. Puede instalar estas librerías utilizando el gestor de paquetes de Python pip. A continuación se muestra un ejemplo de cómo instalar estas librerías en una distribución de Linux basada en Debian:</p>

```
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ pip3 install python-nmap tqdm termcolor
```


## Cómo contribuir

Si desea contribuir a SCANMENOW, por favor, siga los siguientes pasos:

### Forkee este repositorio.

- Cree su propia rama (`git checkout -b feature/AmazingFeature`).
- Haga sus cambios y realice un commit (`git commit -m 'Añadiendo un feature increíble'`).
- Haga un push a la rama (`git push origin feature/AmazingFeature`).
- Abra una solicitud de pull.

## Código de conducta

Todos los colaboradores de SCANMENOW deben adherirse al código de conducta de la comunidad.

## Autor

SCANMENOW fue creado por Ubyquit.

## Licencia

<p align="justify">SCANMENOW se distribuye bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.</p>

## Limitación de responsabilidades

<p align="justify">Esta herramienta se proporciona con fines educativos. El uso inadecuado de esta herramienta será responsabilidad exclusiva de la persona que la use. Los autores de SCANMENOW no se hacen responsables de ningún daño causado por el uso de esta herramienta.</p>
