from snappy_sms import send_sms

#If login data has been specified within the module:
send_sms(destination_number, 'hello!')

#Alternatively
send_sms(destination_number, 'hello!', own_number, password)