#!/bin/bash

# Notice how when using python you can call to the module folder
# instead of the actual .py script.
# Executing 'python snappy_sms' and 'python snappy_sms/__main__.py'
# are completely equivalent options, though the first one is recommended
# for simplicity.

# Sends a message to 600000000. Uses the username and password defined in snappy_sms/__init__.py
python snappy_sms 600000000 "hello world!"

# Same, but prints out details on destination number, message and success
python snappy_sms -v snappy_sms 600000000 "hello world!"

# Same, but uses 611111111 as username and 'mypass' as password instead of those defined in snappy_sms/__init__.py
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
