from src.errors.exception import handleException
from src.errors.handle_db_error import handleDbError
from src.errors.handle_validation_error import handleValidationError
from src.errors.handle_forbidden_error import handleForbiddenError
from src.middlewares.before_request import beforeRequest
from src.middlewares.after_request import afterRequest
from src.routes import routes
import sqlalchemy
from pydantic import ValidationError
from werkzeug.exceptions import Forbidden

class Bootstrap:
    def __init__(self, app):
        self.app = app
        self.__handleErrors()
        self.__loadMiddleware()
        self.__loadRoutes()
    
    def __handleErrors(self):
        self.app.register_error_handler(Exception, handleException)
        self.app.register_error_handler(sqlalchemy.orm.exc.DetachedInstanceError, handleDbError)
        self.app.register_error_handler(ValidationError, handleValidationError)
        self.app.register_error_handler(Forbidden, handleForbiddenError)
    
    def __loadMiddleware(self):
        self.app.after_request(afterRequest)
        self.app.before_request(beforeRequest)

    def __loadRoutes(self):
        for route in routes:
            self.app.register_blueprint(route)