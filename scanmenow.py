import nmap
import socket
import os
from tqdm import tqdm
from termcolor import colored, cprint

import os

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')


banner = '''
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

cprint(banner,"red")
cprint("\n\nEscaneando la Red local ....","green")


# Obtener la dirección IP de la red local
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

# Escanear la red local con Nmap
nm = nmap.PortScanner()
nm.scan(hosts=f"{local_ip}/24", arguments="-sn")

# Obtener la lista de hosts encontrados
hosts = nm.all_hosts()

# Mostrar los hosts encontrados
cprint("Hosts encontrados:","green", attrs=["bold"])
for i, host in enumerate(hosts):
    print(f"  {i}. {host}")

# Preguntar al usuario por la dirección IP a escanear
while True:
    try:
        target_index = int(input(f"Introduce el número del host a escanear (0-{len(hosts)-1}): "))
        if target_index < 0 or target_index >= len(hosts):
            raise ValueError
        break
    except ValueError:
        cprint("Entrada inválida. Por favor introduce un número válido.","red", attrs=["bold"])

target = hosts[target_index]
port_range = input("Introduce el rango de puertos a escanear (ej. 1-65536): ")
start_port, end_port = map(int, port_range.split("-"))
total_ports = end_port - start_port + 1
open_ports = []

# Registrar los resultados en un archivo de log
with open("script.log", "w") as f:
    f.write(f"Escaneando el host {target} en el rango de puertos {port_range}\n")

try:
    with tqdm(total=total_ports, desc="🛸 Progreso", unit="puerto", ncols=80, bar_format="{l_bar}{bar}{r_bar}", colour="red") as pbar:
        for port in range(start_port, end_port+1):
            # Crear un objeto socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)

                # Intentar conectar con el puerto
                result = s.connect_ex((target, port))
                
                # Registrar el resultado en el archivo de log
                with open("script.log", "a") as f:
                    if result == 0:
                        f.write(f"El puerto {port} está abierto\n")
                        open_ports.append(port)
                    # else:
                     #   f.write(f"El puerto {port} está cerrado\n")

                # Actualizar la barra de progreso
                pbar.update(1)

    # Imprimir la lista de puertos abiertos ordenada
    if open_ports:
        open_ports.sort()
        cprint("\n\n😀 Puertos abiertos:","green", attrs=["bold"])
        print('\n'.join(map(str, open_ports)))
        
    else:
        cprint("\n😭 No se encontraron puertos abiertos.","red", attrs=["bold"])
        
except KeyboardInterrupt:
    cprint("\nSaliendo del programa.","red", attrs=["bold"])
    exit()

try: 
    # Escanear vulnerabilidades con Nmap
    print(f"\nEscaneando vulnerabilidades en el host {target} puede demorar dependiendo del número de puertos ...")
    with tqdm(total=len(open_ports), desc="🎯 Progreso", unit="puerto", ncols=80, bar_format="{l_bar}{bar}{r_bar}", colour="green") as pbar:
        for port in open_ports:
            # Ejecutar comando nmap
            result = os.popen(f"nmap -sV -O --script vuln {target} -p {port}").read()
            # Pintar CVE de rojo
            result = result.replace("CVE", colored("CVE", "red"))
            # Imprimir resultado
            print(result)
            pbar.update(1)
            
except KeyboardInterrupt:
    cprint("\nSaliendo del programa.","red", attrs=["bold"])
    exit()    

