from registration.views import RegistrationView


class CustomRegistrationView(RegistrationView):
    success_url = 'home'
