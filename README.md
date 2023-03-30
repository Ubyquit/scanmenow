![Logo de Hacking Online](https://academiahacking.online/cursos/pluginfile.php/1/theme_moove/logo/1679680585/logo%20completo.png)


Tabla de contenidos
- [Descripción y contexto](#descripción-y-contexto)
- [Guía de usuario](#guía-de-usuario)
- [Guía de instalación](#guía-de-instalación)
- [Instalación](#instalación)
- [Cómo contribuir](#cómo-contribuir)
- [Código de conducta](#código-de-conducta)
- [Autores](#autores)
- [Licencia](#licencia)
- [Limitación de responsabilidades](#limitación-de-responsabilidades)


## Descripción y contexto
<p align="justify">SCANMENOW es una herramienta de escaneo de red desarrollada con Python
. Utiliza las librerías nmap, socket, os, tqdm y termcolor para escanear una red local y encontrar los hosts disponibles, escanear los puertos abiertos de un host en particular y buscar vulnerabilidades en esos puertos.</p>

## Guía de usuario
<p align="justify">Para utilizar SCANMENOW, simplemente ejecute el archivo scanmenow.py y siga las instrucciones en pantalla. La herramienta escaneará la red local y mostrará una lista de hosts disponibles. Luego, pedirá al usuario que seleccione un host y que introduzca un rango de puertos para escanear. SCANMENOW escaneará los puertos seleccionados y mostrará una lista de los puertos abiertos. Finalmente, se ofrecerá al usuario la opción de buscar vulnerabilidades en los puertos abiertos utilizando la herramienta nmap.</p>

### Estructura del proyecto


```
.
└── scanmenow
	├── README.md
	├── scanmenow.py
	├── LICENSE.md
```



## Guía de instalación

<p align="justify">Para utilizar SCANMENOW, asegúrese de tener instaladas las librerías nmap, socket, os, tqdm y termcolor. Puede instalar estas librerías utilizando el gestor de paquetes de Python pip. A continuación se muestra un ejemplo de cómo instalar estas librerías en una distribución de Linux basada en Debian:</p>
Plataforma

-   [Python](https://www.python.org/) ![Python Platform](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-yellow)

Las librerías utilizadas son:

-   [Nmap](https://pypi.org/project/python-nmap/)  ![Nmap version](https://img.shields.io/badge/nmap-7.91-green.svg)
-   [socket](https://docs.python.org/3/library/socket.html)  ![Socket version](https://img.shields.io/badge/socket-0.1.1-blue.svg)
-   [os](https://docs.python.org/3/library/os.html)  ![Os version](https://img.shields.io/badge/os-0.1.0-red.svg)
-   [tqdm](https://pypi.org/project/tqdm/)  ![Tqdm version](https://img.shields.io/badge/tqdm-4.62.2-orange.svg)
-   [termcolor](https://pypi.org/project/termcolor/) ![Termcolor version](https://img.shields.io/badge/termcolor-1.1.0-pink.svg)

Estas librerías se utilizan en el proyecto para escanear una red local y encontrar hosts disponibles, escanear puertos abiertos en un host en particular y buscar vulnerabilidades en esos puertos. También se utilizan para la gestión de paquetes y la presentación de información en pantalla.

## Instalación

```shell
sudo apt-get update
sudo apt-get install python3-pip
pip3 install python-nmap tqdm termcolor
```

Instalación y descarga:

```shell
git clone https://github.com/Ubyquit/scanmenow.git
cd scanmenow
chmod -X scanmenow.py
python3 scanmenow.py
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

## Autores

<img src="https://scontent.fcjs3-2.fna.fbcdn.net/v/t39.30808-6/297334960_10226115189318803_3515507641582716610_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=174925&_nc_eui2=AeFsmOOwNjwqvA8Ff-CmN6YIcsff39AepwByx9_f0B6nADoiY11wIZw4d3l_suHGeVQ&_nc_ohc=eirIIEFi8BwAX-TiA_O&_nc_ht=scontent.fcjs3-2.fna&oh=00_AfA32kMgNMcpq0so9TnL1zwkZCIE3o3fBOTFf2hJ-nMl9g&oe=642AADAA" width="100">



## Licencia

SCANMENOW se distribuye bajo la licencia MIT. Consulte el archivo [LICENSE.MD](LICENSE.md) para obtener más detalles.

## Limitación de responsabilidades

<p align="justify">Esta herramienta se proporciona con fines educativos. El uso inadecuado de esta herramienta será responsabilidad exclusiva de la persona que la use. Los autores de SCANMENOW no se hacen responsables de ningún daño causado por el uso de esta herramienta.</p>

## Gratitud 🎁

-   Comenta a otros sobre este proyecto 📢
-   Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
-   Da las gracias públicamente 🤓.
