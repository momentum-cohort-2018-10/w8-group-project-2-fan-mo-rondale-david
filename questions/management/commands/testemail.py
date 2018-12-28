from questions.notify import Notify
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Test yagmail"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        yag = Notify()
        to = "david@davidlndean.com"
        subject = "Test from Yag"
        content = "Some message content"
        yag.sendemail(to, subject, content)
