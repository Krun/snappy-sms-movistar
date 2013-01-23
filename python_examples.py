from snappy_sms import send_sms

#If login data has been specified within the module:
send_sms(600000000, 'hello!')

#Alternatively. 611111111 is your own numer (username)
send_sms(600000000, 'hello!', 611111111, 'mypassword')
