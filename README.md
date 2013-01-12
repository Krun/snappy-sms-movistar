#Snappy SMS

Snappy SMS es un módulo python sencillo para enviar SMS a través de la API REST de Movistar. Para ello es necesario tener un número en servicio con Movistar, y activar la clave de servicios web.

##Coste del servicio

Los SMS enviados a través de esta API se facturan exactamente igual que si se hubieran enviado desde el terminal móvil que utiliza ese número. Actualmente movistar ofrece varios planes que incluyen SMS ilimitados de forma gratuita, pero en caso de no disponer de este servicio, los SMS enviados se facturarán con la tarifa habitual.

##Obtener clave del servicio

Para obtener la clave necesaria para utilizar esta API es necesario enviar un SMS gratuito al número 22770 que contenga la clave deseada. Por ejemplo, si enviamos "hola" al numero 22770 nuestra clave será "hola". Recibiremos un mensaje confirmando la clave.

Esta clave se comparte con la de acceso a otros servicios como la gestión de la segunda linea.

##Ejemplo
```python
from snappy_sms import send_sms

#If login data has been specified within the module:
send_sms(destination_number, 'hello!')

#Alternatively
send_sms(destination_number, 'hello!', own_number, password)

```
