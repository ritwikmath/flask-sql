from src.errors.exception import handleException
from src.middlewares.before_request import beforeRequest
from src.middlewares.after_request import afterRequest

class Bootstrap:
    def __init__(self, app):
        self.app = app
        self.handleErrors()
        self.loadMiddleware()
    
    def handleErrors(self):
        self.app.register_error_handler(Exception, handleException)
    
    def loadMiddleware(self):
        self.app.before_request(beforeRequest)
        self.app.after_request(afterRequest)