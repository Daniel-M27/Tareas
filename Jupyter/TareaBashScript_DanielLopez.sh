#!/bin/bash

# Comenta que es lo que hace cada uno de los siguientes comandos

# Crean un árbol de directorios con los nombres especificados. La opción -p especifica que si los directorios padre no existen, se crearán también.
mkdir -p respaldo_sistema/configuracion 
mkdir -p python/scripts  

touch  respaldo_sistema/guia  # Crea el archivo "guía" dentro de respaldo_sistema/
touch  python/scripts/secuencia.data  # Crea el archivo "secuencia.data" dentro de python/scripts/

cp -r /bin/* respaldo_sistema/programas/ # Copia todo el contenido de /bin/ (incluyendo subdirectorios) a la ruta especificada.
cp /etc/X11/ respaldo_sistema/  # Como la copia no es recursiva, y lo que se quiere copiar es un directorio, no se copiará nada a la ruta especificada.  

echo $USER  # Regresa el valor de la variable de entorno "USER", el nombre del usuario actual.
echo $HOME  # Regresa el valor de la variable de entorno "HOME", la ruta a nuestro directorio de usuario actual. 


head -37 $HOME/.bashrc > PEGADO.txt  # Escribe las primeras 37 líneas del archivo ".bashrc" (ubicado en nuestro directorio de usuario) al archivo "PEGADO.txt". (si no existe, lo crea).

echo "#############################" >> PEGADO.txt  # Anexa lo que está entre paréntesis al final de PEGADO.txt (sin sobreescribir).
tail -37 $HOME/.bash_history >> PEGADO.txt  # Anexa las últimas 37 líneas del archivo ".bash_history" al final de PEGADO.txt (sin sobreescribir).

touch python/notas  # Crea el archivo "notas" en el directorio python/
touch respaldo_sistema/configuracion/guia  # Crea el archivo "guia" en respaldo_sistema/configuracion/

find /usr -perm 777 >> todos.prm  # Regresa todos los archivos con permisos 'rwx' para todos los tipos de usuario en la carpeta /usr, o alguno de sus subdirectorios. Luego se anexan al archivo "todos.prm". (si no existe, lo crea).
 
find /var -name *.tar >> all.compress  # Regresa todos los archivos con extensión '.tar' en la carpeta /var, o alguno de sus subdirectorios. Luego se anexan al archivo "all.compress". (si no existe, lo crea).

ls -laR /etc/* | grep daemon  # Lista recursivamente el contenido del directorio /etc/ y sus subdirectorios (incluyendo archivos ocultos); luego se filtran para mostrar sólo los que tienen "daemon" en su nombre. 

grep -lri daemon /etc/* > Demonios  # Regresa el nombre de los archivos dentro de /etc/, o alguno de sus subdirectorios, que contienen la palabra "daemon" (sin distinguir entre mayúsculas y minúsculas) en su interior. Luego se escriben al archivo "Demonios". (si no existe, lo crea).

find /etc/ -name *.conf >> Demonios  # Regresa todos los archivos con extensión '.conf' en la carpeta /etc/, o alguno de sus subdirectorios. Luego se anexan al final del archivo "Demonios" (sin sobreescribir).

ps -ea -u $USER > Procesos.txt  # Regresa todos los procesos, asociados a una terminal, que están siendo ejecutados por el usuario actual. Luego se escriben al archivo "Procesos.txt".

tar -cvf respaldo_sistema  # Intentará comprimir el directorio 'respaldo_sistema', pero al no especificar un nombre para el archivo resultante, el proceso falla.

