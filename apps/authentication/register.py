from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as Usuario, Group as UserGroup
import random

char_low = "abcdefghijklmnñopqrstuvwyz"
class SetAuthGroup():
    # * Crear un nombre de usuario para nuevos usuarios
    def username(self, first_name, last_name):
        _first_name = first_name
        _last_name = last_name.split(" ")
        _username_length = len(f'{first_name}{last_name}')
        username = f'{_first_name[:4]}{_last_name[-1][:4]}{_username_length}{random.choice(char_low)}'
        return username.lower()

    # * Creacion de usuarios
    @transaction.atomic()
    def create_user(self, first_name, last_name, username=None, password=None, email=None):
        with transaction.atomic():
            Usuario.objects.update_or_create(
                username = username,
                defaults = {
                    'username': username,
                    'password': make_password(password),
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email
                }
            )
            return Usuario.objects.get(username=username)

    def create_group(self, name):
        UserGroup.objects.get_or_create(name=name)
        return UserGroup.objects.get(name=name)

    def user_group_add(self, user, group):
        # Add user to authgroup
        group = group
        group.user_set.add(user)
