from utils import request

def cache():
    request.post('cache')

def refresh():
    request.post('refresh')

def push():
    request.post('push')