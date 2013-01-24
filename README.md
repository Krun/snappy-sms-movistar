#Snappy SMS

Snappy SMS es un módulo python sencillo para enviar SMS a través de la API REST de Movistar. Para ello es necesario tener un número en servicio con Movistar, y activar la clave de servicios web.

Esta API funciona y está probada únicamente para clientes de __Movistar España__. Para consultar la compatibilidad con Movistar en otros países consulta con tu operadora la validez de la API web para envío de SMS.

Esta información sobre acceso a servicios de Movistar ha sido revisada el día _24 de Enero de 2013_. Es posible que se produzcan cambios inesperados en la disponibilidad del servicio o forma de acceder a las claves por parte de Movistar.

##Coste del servicio

Los SMS enviados a través de esta API se facturan exactamente igual que si se hubieran enviado desde el terminal móvil que utiliza ese número. Actualmente movistar ofrece varios planes que incluyen SMS ilimitados de forma gratuita, pero en caso de no disponer de este servicio, los SMS enviados se facturarán con la tarifa habitual.

##Obtener clave del servicio

Para obtener la clave necesaria para utilizar esta API es necesario enviar un SMS gratuito al número 22770 que contenga la clave deseada. Por ejemplo, si enviamos "hola" al numero 22770 nuestra clave será "hola". Recibiremos un mensaje confirmando la clave.

Esta clave se comparte con la de acceso a otros servicios como la gestión de la segunda linea.

##Ejemplos de ejecución
### Desde otro modulo python
Es tan sencillo como importar la función send_sms del módulo snappy_sms, como se muestra a continuación:
```python
from snappy_sms import send_sms

#If login data has been specified within the module:
send_sms(600000000, 'hello!')

#Alternatively. 611111111 is your own numer (username)
send_sms(600000000, 'hello!', 611111111, 'mypassword')

```

### Mediante linea de comandos
El modulo ofrece la posibilidad de enviar sms mediante linea de comandos. Para ello, se puede llamar con python a la carpeta del propio módulo (python snappy\_sms), lo que equivale a ejecutar el contenido del script \_\_main\_\_.py. De forma alternativa, se pueden dar permisos de ejecución a un script python y ejecutar simplemente ese archivo desde linea de comandos.

```bash
usage: snappy_sms [-h] [-l LOGIN] [-p PASSWORD] [-v] destination message

positional arguments:
  destination           destination phone number
  message               content of the text message

optional arguments:
  -h, --help            show this help message and exit
  -l LOGIN, --login LOGIN
                        movistar api username (sender number). Can be
                        hardcoded in module.
  -p PASSWORD, --password PASSWORD
                        movistar api password. Can be hardcoded in module.
  -v, --verbose         print details on operation and success
```

A continuación se pueden ver algunos ejemplos de ejecución por linea de comandos:

```bash
#!/bin/bash

# Notice how when using python you can call to the module folder
# instead of the actual .py script.
# Executing 'python snappy_sms' and 'python snappy_sms/__main__.py'
# are completely equivalent options, though the first one is recommended
# for simplicity.

# Sends a message to 600000000. Uses the username and password 
# defined in snappy_sms/__init__.py
python snappy_sms 600000000 "hello world!"

# Same, but prints out details on destination number, message and success
python snappy_sms -v snappy_sms 600000000 "hello world!"

# Same, but uses 611111111 as username and 'mypass' as password 
# instead of those defined in snappy_sms/__init__.py
python snappy_sms -l 611111111 -p mypass 600000000 "hello world!"

# Verbose option is available and confirms which username we are using
python snappy_sms -v -l 611111111 -p mypass 600000000 "hello world!"

# Alternatively, the executable python script 'execute.py' can be called with
# the same parameters.
# It is important to have previously give execution permissions to that file by
# executing 'chmod +x execute.py'

./execute.py 600000000 "hello world!"
./execute.py -v snappy_sms 600000000 "hello world!"
./execute.py -l 611111111 -p mypass 600000000 "hello world!"
./execute.py -v -l 611111111 -p mypass 600000000 "hello world!"

```
