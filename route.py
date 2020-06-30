from flask_accept import accept
from endpointscode import peoplev1, peoplev2, peoplev3
# Create a handler for our read (GET) people

@accept('application/vnd.your_vendor.v1')
def read():
    return peoplev1.read()
@read.support('application/vnd.your_vendor.v2')
def read_prev_1():
    return peoplev2.read()
@read.support('application/vnd.your_vendor.v3')
def read_prev_2():
    return peoplev3.read()
