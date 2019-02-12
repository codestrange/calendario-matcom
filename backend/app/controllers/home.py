from . import api


@api.route('/')
def index():
    return 'Hello World!'
