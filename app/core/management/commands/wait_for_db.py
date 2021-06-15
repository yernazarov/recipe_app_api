import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    def handle(self, *args, **options): #what is ran whenever we run this command;
        #args and #options are there to allow us pass in custom arguments and functions.
        self.stdout.write('Waiting for database...')
        db_conn = None #database connection
        while not db_conn:
            try:
                db_conn = connections['default'] #try to set db_conn to database connection
            except OperationalError:
                self.stdout.write('Database unavailable, waiting for 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available')) #green style
