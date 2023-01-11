from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    data_nascimento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='users/%Y/%m/%d/',
                             blank=True)

    def __str__(self):
        return f'Perfil do usuário {self.user.username}'
