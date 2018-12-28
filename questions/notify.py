import yagmail

#https://support.google.com/accounts/answer/185833

#https://support.google.com/accounts/answer/6010255


class Notify(object):
    def sendemail(self, recipient, subject, body):
        yag = yagmail.SMTP('questionbox18@gmail.com')
        yag.send(recipient, subject, body)

    def configure(self, emailAccount, Password):
        yagmail.register(emailAccount, Password)


# questionbox18@gmail.com,
#     email = EmailMultiAlternatives(
#         from_email='questionbox18@gmail.com',
#         to=[self.question.author.email],
#         subject='You have a new answer',
#         body=f"""
#         You have a new answer on QuestionBox. {{ self.author.username }}
#         just answered you!
#         """)
#     email.send()
