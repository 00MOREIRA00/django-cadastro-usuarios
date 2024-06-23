from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvando os dados da tela para o banco de dados
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuários Já cadastrados em uma nova página 
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }

    # Retornar os dados para a página de listagem de usuário
    return render(request, 'usuarios/usuarios.html', usuarios)