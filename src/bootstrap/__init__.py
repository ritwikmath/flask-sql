from src.errors.exception import handleException
from src.errors.handle_db_error import handleDbError
from src.errors.handle_validation_error import handleValidationError
from src.middlewares.before_request import beforeRequest
from src.middlewares.after_request import afterRequest
from src.routes import routes
import mysql
from pydantic import ValidationError

class Bootstrap:
    def __init__(self, app):
        self.app = app
        self.__handleErrors()
        self.__loadMiddleware()
        self.__loadRoutes()
    
    def __handleErrors(self):
        self.app.register_error_handler(Exception, handleException)
        self.app.register_error_handler(mysql.connector.Error, handleDbError)
        self.app.register_error_handler(ValidationError, handleValidationError)
    
    def __loadMiddleware(self):
        self.app.after_request(afterRequest)
        self.app.before_request(beforeRequest)

    def __loadRoutes(self):
        for route in routes:
            self.app.register_blueprint(route)