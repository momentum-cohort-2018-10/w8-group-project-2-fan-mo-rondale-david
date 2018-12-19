from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from questions.models import User, Question, Answer
from django.db.models import Count
from faker import Faker
from random import randint


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        User.objects.exclude(username='fan').delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()

        password = "quizme(11)"
        exp_questions = 50
        exp_users = 20
        avg_answers_per_question = 3
        # avg_stars_per_question = 5

        num_authors = User.objects.all().count()
        num_questions = Question.objects.all().count()
        num_answers = Answer.objects.all().count()

        faker = Faker()

        self.stdout.write("Defalt password:" + password)
        self.stdout.write("Number of users:" + str(num_authors))
        self.stdout.write("Number of questions:" + str(num_questions))
        self.stdout.write("Number of answers:" + str(num_answers))

        if(num_authors < exp_users):
            self.stdout.write(
                "Creating " + str(exp_users-num_authors) + "Authors")
            for x in range(num_authors, exp_users):
                username = faker.name().replace(" ", ".")
                email = username+"@test.com"
                User.objects.create(username=username,
                                    email=email,
                                    password=password)
                self.stdout.write("  " + username)
            num_authors = User.objects.all().count()

        if(num_questions < exp_questions):
            self.stdout.write(
                "Creating " + str(exp_questions-num_questions) + "Questions")
            for x in range(num_questions, exp_questions):

                u = self.randomAuthor()
                title = "Test Question " + str(x)
                self.stdout.write(" [" + u.username + "] "+title)
                rec = Question()
                rec.author = u
                rec.title = title
                rec.text = faker.text()
                rec.save()
            num_questions = Question.objects.all().count()

        self.stdout.write("Answers...")
        while(num_answers < avg_answers_per_question*num_questions):
            author = self.randomAuthor()
            question = self.randomQuestion()
            rec = Answer()
            rec.author = author
            rec.question = question
            rec.text = faker.text(250)
            rec.save()
            num_answers = Answer.objects.all().count()
            self.stdout.write(str(num_answers) + ": " + author.username +
                              " gave an answer on [" + question.title + "]")

    def randomAuthor(self):
        count = User.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return User.objects.all()[random_index]

    def randomQuestion(self):
        count = Question.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return Question.objects.all()[random_index]
