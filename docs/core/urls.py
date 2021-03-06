from django.urls import path, include
from core.views import index,lista,cursos,alunos, disciplinas, coordenadores,atividades,mensagens,professores,detalhes_diciplinas,detalhes_curso,login,novo_aluno, novo_curso, nova_disciplina, novo_coordenador,nova_atividade,nova_mensagem,novo_professor,matricula,pagina_disciplina, ads,gti,bd, logica,devops,tecweb,d_ads,d_gti,d_bd,alunos,atualizar_aluno, atualizar_coordenador, atualizar_professor, atualizar_curso, atualizar_disciplina,atualizar_atividade,atualizar_mensagem
from curriculo.views import listaCursos, curso, incluirCurso, alterarCurso, listarDisciplinas, incluirDisciplina, alterarDisciplina
urlpatterns = [
    path('',index),
    path('cursos/', listaCursos),
    path('cursos/incluir/', incluirCurso),
    path('cursos/alterar/<int:id>', alterarCurso),
    path('disciplinas/', listarDisciplinas),
    path('disciplinas/incluir/', incluirDisciplina),
    path('disciplinas/alterar/<int:id>', alterarDisciplina),
    path('cursos.html',cursos),
    path('listagem',lista),
    path('alunos', alunos),
    #path('disciplinas', disciplinas),
    path('coordenadores', coordenadores),
    path('atividades', atividades),
    path('mensagens', mensagens),
    path('professores', professores),
    path('index.html',index),
    path('login',login),
    path('novo_aluno', novo_aluno, name='novo_aluno'),
    path('novo_coordenador', novo_coordenador, name='novo_coordenador'),
    path('novo_professor', novo_professor, name='novo_professor'),
    path('novo_curso', novo_curso, name='novo_curso'),
    path('nova_disciplina', nova_disciplina, name='nova_disciplina'),
    path('nova_atividade', nova_atividade, name='nova_atividade'),
    path('nova_mensagem', nova_mensagem, name='nova_mensagem'),
    path('matricula.html',matricula),
    path('pagina_disciplina.html',pagina_disciplina),
    path('ads', ads),
    path('gti',gti),
    path('bd',bd),
    path('logica', logica),
    path('tecweb', tecweb),
    path('devops', devops),
    path('d_ads', d_ads),
    path('d_gti', d_gti),
    path('d_bd', d_bd),
    path('alunos', alunos),
    path('atualizar_aluno/<int:id>/', atualizar_aluno, name="atualizar_aluno"),
    path('atualizar_coordenador/<int:id>/', atualizar_coordenador, name="atualizar_coordenador"),
    path('atualizar_professor/<int:id>/', atualizar_professor, name="atualizar_professor"),
    path('atualizar_curso/<int:id>/', atualizar_curso, name="atualizar_curso"),
    path('atualizar_disciplina/<int:id>/', atualizar_disciplina, name="atualizar_disciplina"),
    path('atualizar_atividade/<int:id>/', atualizar_atividade, name="atualizar_atividade"),
    path('atualizar_mensagem/<int:id>/', atualizar_mensagem, name="atualizar_mensagem"),
]
