import yagmail


class Notify(object):
    def sendemail(self, recipient, subject, body):
        self.configure("questionbox18@gmail.com", "fanmorondave")
        yag = yagmail.SMTP('questionbox18@gmail.com')
        yag.send(recipient, subject, body)

    def configure(self, account, password):
        yagmail.register(account, password)
