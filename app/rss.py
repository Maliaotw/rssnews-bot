from utils import request
def refresh():
    request.post('refresh')



def push():
    request.post('push')