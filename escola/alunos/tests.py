from django.test import TestCase
from .models import Aluno

class AlunoModelTest(TestCase):

    def test_criar_aluno(self):
        aluno = Aluno.objects.create(
            nome="Teste",
            idade=20,
            email="teste@email.com"
        )

        self.assertEqual(aluno.nome, "Teste")
        self.assertTrue(aluno.matriculado)  

        from django.urls import reverse

    def test_verificar_idade(self):
        aluno = Aluno.objects.create(
            nome="João",
            idade=15,
            email="joao@teste.com"
        )
        self.assertEqual(aluno.idade, 15)

class AlunoViewTest(TestCase):

    def test_lista_alunos_status(self):
        response = self.client.get('/alunos/')
        self.assertEqual(response.status_code, 200)