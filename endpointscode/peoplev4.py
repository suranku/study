from datetime import datetime
from flask_accept import accept
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "firstname": "Doug3",
        "lastname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "firstname": "Kent3",
        "lastname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "firstname": "Bunny3",
        "lastname": "Easter",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
@accept('application/vnd.your_vendor.v1', 'application/vnd.your_vendor.v2')
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

@read.support('application/vnd.your_vendor.v3')
def read_V4():
    return 'Goodbye cruel world.'