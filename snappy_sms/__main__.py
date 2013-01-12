from __init__ import send_sms
print " "
to = raw_input('Escribe el numero de destino: ')
message = raw_input('Escribe el texto del SMS: ')
succ = send_sms(to, message)
if(succ):
  print 'El SMS se ha enviado con exito'
else:
  print 'Ha habido un problema al enviar el SMS. Revisa tu usuario y password.'
