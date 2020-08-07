from simple_mail.mailer import BaseSimpleMail, simple_mailer

class WelcomeMail(BaseSimpleMail):
    email_key = 'lcomieuer'

welcome_mail = WelcomeMail()
simple_mailer.register(WelcomeMail)
