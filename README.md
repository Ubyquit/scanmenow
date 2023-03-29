# Escáner de puertos en red local

Nmap Network Scanner
Este es un programa simple que utiliza la biblioteca nmap para escanear la red local y buscar hosts activos. El usuario puede seleccionar un host específico para escanear y especificar un rango de puertos a escanear. El resultado del escaneo se guarda en un archivo de registro y se muestra en la consola.

Utiliza [Nmap](https://nmap.org/) para escanear los hosts de la red y mostrar los puertos abiertos en el host seleccionado por el usuario.

## Uso

1. Clona el repositorio.

git clone https://github.com/TU_USUARIO/AQUI_EL_NOMBRE_DEL_REPOSITORIO.git

2. Requerimientos


- Python 3.x
- Nmap
- TQDM
- termcolor


3. Instala las dependencias.


pip install -r requirements.txt


4. Ejecuta el script.

python scanmenow.py

El programa escaneará la red local y mostrará una lista de hosts activos. Luego, pedirá al usuario que ingrese el número del host que desea escanear y el rango de puertos a escanear. El resultado del escaneo se mostrará en la consola y se registrará en un archivo de registro llamado `script.log`.

Sigue las instrucciones en pantalla para seleccionar el host que deseas escanear y el rango de puertos a escanear.

5. Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de enviar un pull request o abrir un issue si encuentras algún error o quieres sugerir alguna mejora.

6. Licencia
Este proyecto está bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

## Autor

Este proyecto fue creado por **Ubyquit**.