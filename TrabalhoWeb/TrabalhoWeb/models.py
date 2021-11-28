from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

USER_CHOICES = (
    ("EMPRESA", "Empresa"),
    ("CANDIDATO", "Candidato")
)

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, tipo, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not usuario:
            raise ValueError('Users must have an username')

        user = self.model(
            usuario=self.usuario,
            tipo=tipo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    usuario = models.CharField(max_length=100, help_text='Usuario', primary_key=True)
    tipo = models.CharField(choices=USER_CHOICES, max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "usuario"

    def __str__(self):
        return self.usuario

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Empresa(models.Model):
    usuario = models.CharField(max_length=100, help_text='Nome', primary_key=True)
    nome = models.CharField(max_length=100, help_text='Nome')
    email = models.EmailField(help_text='Email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI da empresa', max_length=20)
    endereco = models.CharField(max_length=254, help_text='Endereço')
    descricao = models.CharField(help_text='Descrição', max_length=254)
    #foto = models.ImageField(help_text = 'Foto')

    def __str__(self):
        return self.nome

class Candidato(models.Model):
    usuario = models.CharField(help_text='Usuario', max_length=254, primary_key=True)
    nome = models.CharField(max_length=100, help_text='Nome')
    email = models.EmailField(help_text='Email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(verbose_name='Data de Nascimento', help_text='Nascimento no formado DD/MM/AAAA')
    cidade = models.CharField(max_length=254, help_text='Cidade')
    estado = models.CharField(max_length=254, help_text='Estado') 
    pais = models.CharField(max_length=254, help_text='País')
    #foto = models.ImageField(help_text = 'Foto')
    descricao = models.CharField(help_text='Descrição', max_length=254)
    experiencia = models.CharField(help_text='Experiências', max_length=254)
    formacao = models.CharField(help_text='Formação', max_length=254)
    cargo = models.CharField(help_text='Cargo', max_length=254)
    estadoCivil = models.CharField(help_text='Estado civil', max_length=254)
    sexo = models.CharField(help_text='Sexo', max_length=254)
    endereco = models.CharField(max_length=254, help_text='Endereco')

    def __str__(self):
        return self.nome