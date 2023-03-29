'''
 .d8888b.   .d8888b.        d8888 888b    888 888b     d888 8888888888                                 
d88P  Y88b d88P  Y88b      d88888 8888b   888 8888b   d8888 888                                        
Y88b.      888    888     d88P888 88888b  888 88888b.d88888 888                                        
 "Y888b.   888           d88P 888 888Y88b 888 888Y88888P888 8888888    88888b.   .d88b.  888  888  888 
    "Y88b. 888          d88P  888 888 Y88b888 888 Y888P 888 888        888 "88b d88""88b 888  888  888 
      "888 888    888  d88P   888 888  Y88888 888  Y8P  888 888        888  888 888  888 888  888  888 
Y88b  d88P Y88b  d88P d8888888888 888   Y8888 888   "   888 888        888  888 Y88..88P Y88b 888 d88P 
 "Y8888P"   "Y8888P" d88P     888 888    Y888 888       888 8888888888 888  888  "Y88P"   "Y8888888P"  
                                                                                                       
                                                                                                       
                                                                                                       
888888b.                 888     888 888                                 d8b 888                       
888  "88b                888     888 888                                 Y8P 888                       
888  .88P                888     888 888                                     888                       
8888888K.  888  888      888     888 88888b.  888  888  .d88888 888  888 888 888888                    
888  "Y88b 888  888      888     888 888 "88b 888  888 d88" 888 888  888 888 888                       
888    888 888  888      888     888 888  888 888  888 888  888 888  888 888 888                       
888   d88P Y88b 888      Y88b. .d88P 888 d88P Y88b 888 Y88b 888 Y88b 888 888 Y88b.                     
8888888P"   "Y88888       "Y88888P"  88888P"   "Y88888  "Y88888  "Y88888 888  "Y888                    
                888                                888      888                                        
           Y8b d88P                           Y8b d88P      888                                        
            "Y88P"                             "Y88P"       888    
'''



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