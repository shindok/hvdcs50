from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
""" 
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.user_type == 'regular':
                # Use email authentication
                if user.email == kwargs.get('email'):
                    if user.check_password(password):
                        return user
            elif user.user_type == 'premium':
                # Use social media authentication
                # Authenticate the user using social media API
                # Return the user object if authentication is successful
                pass
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
 """