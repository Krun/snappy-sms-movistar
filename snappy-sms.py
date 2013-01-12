import urllib, httplib

MOVISTAR_USERNAME = 600000000
MOVISTAR_PASSWORD = 'tu_clave_de_la_api_sms'

def send_sms(to, text, username=MOVISTAR_USERNAME, password=MOVISTAR_PASSWORD):
  form = dict(to = to,
              message = text,
              TM_ACTION = 'AUTHENTICATE',
              TM_LOGIN = username,
              TM_PASSWORD = password)
  headers = {'Content-type':'application/x-www-form-urlencoded'}
  data = urllib.urlencode(form)

  conn = httplib.HTTPSConnection("opensms.movistar.es")
  conn.request("POST", "/aplicacionpost/loginEnvio.jsp", data, headers)
  resp = conn.getresponse()
  rred = resp.read()
  conn.close()
  return(rred == 'OK')

if __name__ == "__main__":
  print " "
  to = raw_input('Escribe el numero de destino: ')
  message = raw_input('Escribe el texto del SMS: ')
  succ = send_sms(to, message)
  if(succ):
    print 'El SMS se ha enviado con exito'
  else:
    print 'Ha habido un problema al enviar el SMS. Revisa tu usuario y password.'
