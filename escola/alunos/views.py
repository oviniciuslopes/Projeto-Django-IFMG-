from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def detalhe_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    return render(request, 'alunos/detalhe_aluno.html', {'aluno': aluno})

def detalhe(request):
    return render(request, 'alunos/detalhe.html')

@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alunos/')
    else:
        form = AlunoForm()

    return render(request, 'alunos/form_aluno.html', {'form': form})
