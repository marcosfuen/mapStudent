# Aplicaci贸n encuesta de la UC para el COVOD-19

_Aplicaci贸n web para encuesta de la covid19_

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 馃搵

_Primero que todo tenemos que tener un entorno virtual creado con tadas las dependecias del proyecto el mismo esta hecho con Python y Django_

### Instalaci贸n 馃敡

_Instalaci贸n del entorno virtual con virtualenv_

_Instalamos el modulo de python la el entorno virtual_

```
# apt-get install python-virtualenv
```

_Creamos el entorno virtual es este caso es con python 2.7_

```
$ virtualenv entorno1
```

_Para crear un entorno virtual con python 3_

```
$ virtualenv -p /usr/bin/python3 entorno2
```

_Nos movemos al directorio que se creo y listamos_

```
$ cd entorno2
$ ls
bin  lib
```

_Activamos el entorno virtual_

```
$ source entorno2/bin/activate
(entorno2)$
```

_o despues de estar en el directorio del entorno virtual ponemos_

```
source bin/activate
```

_Ejemplo de como hacerlo todo en una linea en este caso es covid-19 el entorno virtual y en git esta el proyecto_

```
cd virtualenvs/covid-19/ && source bin/activate && cd ~ && cd git/covid-19
```

_Desactivar el entorno virtual_

```
deactivate
```

_Instalando paquetes dentro del entorno virtual tener en cuenta que tiene que estar activado_

```
pip install django
```

_o instalar paquetes que esten en un fichero requirements.txt_

```
pip install -r requirements.txt
```

_De esta forma ya tenemos en entorno virtual preparado para que nuestra aplicaci贸n pueda correr sin problema alguno_

### Requerimientos para correr el proyecto o configuraci贸n 鈿欙笍

```
pip install -r requirements.txt (recomendada)

O

pip install Pillow
pip install django
pip install bla bla bla bla
```

## Colaboradores

```
UC_Dev

```

## Deployment 馃摝

_Agrega notas adicionales sobre como hacer deploy o ver a darvin_

## Construido con 馃洜锔?

_Herramientas que se utilizar贸n para crear el proyecto_

- [Python](https://www.python.org/) - El lenguaje de programaci贸n usado
- [Django](https://www.djangoproject.com/) - El framework web usado
- [Visual Studio Code](https://code.visualstudio.com/) - Editor Usado

## Licencia 馃搫

Este proyecto est谩 bajo la Licencia (GPL3) - mira el archivo [LICENSE.md](LICENSE) para detalles o el enlace actualizado [GPL_V3](https://www.gnu.org/licenses/gpl-3.0.html)
