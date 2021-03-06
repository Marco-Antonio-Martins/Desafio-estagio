from http import client
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):

  usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
  nome = models.CharField(max_length=150)
  cpf = models.CharField('CPF : Somente números', max_length=14, unique=True, blank=True, null=True)
  tipos_usuario = (
    ('O', 'Operador'),
    ('C', 'Cliente'),
  )
  tipo_usuario = models.CharField(max_length=1, choices=tipos_usuario)

  def __str__(self):
      return self.nome
      

class Horario(models.Model):
  
  criador = models.ForeignKey(Usuario, related_name='operador_criou', on_delete=models.CASCADE)
  cliente = models.ManyToManyField(Usuario, related_name='horarios', default=None, blank=True)
  dataInicio = models.DateTimeField()
  dataFim = models.DateTimeField(blank=True, null=True) 
  duracao = models.IntegerField('Duração por atendimento')
  qtVagas = models.IntegerField('Quantidade de vagas por dia')
  
  def contains(self, user):
    for c in self.cliente:
      if c == user:
        return True

  def __str__(self):
      return str(self.dataInicio)