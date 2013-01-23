from __init__ import send_sms
import argparse, sys


def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('destination', help='destination phone number')
  parser.add_argument('message', help='content of the text message')
  parser.add_argument('-l','--login', help='movistar api username (sender number). Can be hardcoded in module.')
  parser.add_argument('-p','--password', help='movistar api password. Can be hardcoded in module.')
  parser.add_argument('-v','--verbose', help='print details on operation and success', action="store_true")
  args = parser.parse_args()
  if args.login == None and args.password == None:
    succ = send_sms(args.destination, args.message)
  else:
    succ = send_sms(args.destination, args.message, args.login, args.password)
  if args.verbose:
    print 'Sending message to: ' + args.destination
    print 'Content: ' + args.message
    if args.login != None and args.password != None: 
      print 'Username: ' + args.login
    if succ:
      print 'Message successfully sent'
    else:
      print 'Unexpected problem sending message. Check username and password'
  sys.exit(0)

if __name__ == "__main__":
  main(sys.argv[1:])
