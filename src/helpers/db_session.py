from src.db import Database
import functools

def session(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        with Database() as session:
            return func(self, session, *args, **kwargs)
    return wrapper
