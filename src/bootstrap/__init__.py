from src.errors.exception import handleException

class Bootstrap:
    def __init__(self, app):
        self.app = app
        self.handleErrors()
        self.loadMiddleware()
    
    def handleErrors(self):
        self.app.register_error_handler(Exception, handleException)
    
    def loadMiddleware(self):
        pass