from django.db import models

USER_CHOICES = (
    ("EMPRESA", "Empresa"),
    ("CANDIDATO", "Candidato")
)

class Usuario(models.Model):
    usuario = models.CharField(max_length=100, help_text='Usuario')
    senha = models.CharField(max_length=100, help_text='Senha')
    tipo = models.CharField(choices=USER_CHOICES, max_length=10)

    def __str__(self):
        return self.usuario

class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome')
    email = models.EmailField(help_text='Email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI da empresa', max_length=20)
    endereco = models.CharField(max_length=254, help_text='Endereço')
    descricao = models.CharField(help_text='Descrição', max_length=254)
    #foto = models.ImageField(help_text = 'Foto')

    def __str__(self):
        return self.nome

class Candidato(models.Model):
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