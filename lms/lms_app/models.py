from django.db import models
class Professor(models.Model):
    def __str__(self):
        return self.nome + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        print('estou salvando')
        if(self.login == ""):
            raise Exception("ERRO: Sem Login")
        if(self.email == ""):
            self.email = "email nao fornecido"  
        if (Professor.objects.filter(login=self.login).exists()):
            raise Exception("ERRO: Sem Email")
            
            
        super(Professor,self).save()
        
class Disciplina(models.Model):
    def __str__(self):
        return self.nome + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)
    def save(self):
        print('estou salvando')
        if (Disciplina.objects.filter(nome=self.nome).exists()):
            raise Exception("ERRO: Disciplina Repetida")
        super(Disciplina,self).save()

class DisciplinaOfertada(models.Model):
    def __str__(self):
        return self.curso + self.turma
    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida

    def save(self):
        print('estou salvando')
        if (self.curso not in ('ADS', 'SI', 'BD')):
            raise Exception('ERRO: Curso Inválido')
        super(DisciplinaOfertada,self).save()