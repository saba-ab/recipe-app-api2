"""
Django command to wait for the database to be available.
"""
from time import sleep
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting database to connect ...")
        db_is_ready = False
        while not db_is_ready:
            try:
                self.check(databases=['default'])
                db_is_ready = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write("Database is not ready, waiting 1 second...")
                sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is ready!"))
