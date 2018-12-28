import yagmail
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Init yagmail keyring"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        yagmail.register("questionbox18@gmail.com", "fanmorondave")
