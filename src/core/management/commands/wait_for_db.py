"""
Command to wait for the database to be available before proceeding.

Inspired from https://github.com/enzofrnt/django_wait_for_db
"""

import time

from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for the database to be available before proceeding."

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Waiting for the database to be available..."))

        while True:
            try:
                connection = connections[DEFAULT_DB_ALIAS]
                connection.ensure_connection()

                self.stdout.write(self.style.SUCCESS("Database available!"))
                break

            except OperationalError as e:
                self.stdout.write(self.style.ERROR(f"Error with database: {e}"))
                self.stdout.write(self.style.WARNING("Database unavailable, waiting 1 second..."))

                time.sleep(1)
