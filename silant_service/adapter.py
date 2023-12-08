from allauth.account.adapter import DefaultAccountAdapter


class Silant_serviceAccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return False
