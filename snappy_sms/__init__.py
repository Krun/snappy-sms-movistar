import urllib, httplib, socket, ssl

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
  #This is to force TLSv1. Connection might fail otherwise.
  sock = socket.create_connection((conn.host, conn.port), conn.timeout, conn.source_address)
  conn.sock = ssl.wrap_socket(sock, conn.key_file, conn.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)
  conn.request("POST", "/aplicacionpost/loginEnvio.jsp", data, headers)
  resp = conn.getresponse()
  rred = resp.read()
  conn.close()
  return(rred == 'OK')