from flask import Flask, render_template, request, redirect, url_for

from _Projeto_Alunos import Aluno

from _Projeto_Professor import Professor

from _Projeto_Cursos import Cursos

from _Projeto_Turma import Turma

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Rotas Alunos
@app.route("/listar/alunos")
def listar_alunos():
    alunos = Aluno.listar()

    return render_template("listar_alunos.html", alunos=alunos)

@app.route("/cadastro/aluno", methods=("GET", "POST"))
def cadastro_aluno():
    if request.method == "POST":
        nome = request.form["nome_aluno"]
        
        cpf = request.form["cpf_aluno"]
        
        email = request.form["email_aluno"]
        
        telefone = request.form["telefone_aluno"]

        Aluno(nome = nome, cpf = cpf, email=email, telefone = telefone)

        return redirect(url_for("listar_alunos"))

    return render_template("cadastro_aluno.html")

@app.route("/editar/aluno/<matricula>", methods=("GET", "POST"))
def editar_aluno(matricula):

    aluno = Aluno.listaAlunosMatricula(matricula)

    if request.method == "POST":
        nome = request.form["nome_aluno"]
        
        cpf = request.form["cpf_aluno"]

        telefone = request.form["telefone_aluno"]
        
        email = request.form["email_aluno"]

        Aluno.atualizar(matricula, nome, cpf, telefone, email)

        return redirect(url_for("listar_alunos"))

    return render_template("editar_aluno.html", aluno=aluno)

# Rotas Professores
@app.route("/listar/professores")
def listar_professores():
    professores = Professor.listar()

    return render_template("listar_professores.html", professores=professores)

@app.route("/cadastro/professores", methods=("GET", "POST"))
def cadastro_professor():
    if request.method == "POST":
        nome = request.form["nome_professor"]
        
        cpf = request.form["cpf_professor"]
        
        email = request.form["email_professor"]
        
        telefone = request.form["telefone_professor"]

        formacao = request.form["formacao_professor"]

        especialidade = request.form["especialidade_professor"]

        Professor(nome = nome, cpf = cpf, email = email, telefone = telefone, formacao = formacao, especialidade = especialidade)

        return redirect(url_for("listar_professores"))

    return render_template("cadastro_professor.html")

@app.route("/editar/professor/<matricula>", methods=("GET", "POST"))
def editar_professor(matricula):

    professor = Professor.listaProfessorMatricula(matricula)

    if request.method == "POST":
        nome = request.form["nome_professor"]

        cpf = request.form["cpf_professor"]

        ativo = 0

        if "ativo_professor" in request.form:
            ativo = 1

        email = request.form["email_professor"]

        telefone = request.form["telefone_professor"]

        formacao = request.form["formacao_professor"]

        especialidade = request.form["especialidade_professor"]

        Professor.atualizar(matricula, nome, cpf, ativo, telefone, email, formacao, especialidade)

        return redirect(url_for("listar_professores"))

    return render_template("editar_professor.html", professor=professor)

# Rotas Cursos
@app.route("/listar/cursos")
def listar_cursos():
    cursos = Cursos.listar()

    return render_template("listar_cursos.html", cursos=cursos)

@app.route("/cadastro/cursos", methods=("GET", "POST"))
def cadastro_curso():
    if request.method == "POST":
        nome = request.form["nome_curso"]

        classificacao = request.form["classificacao_curso"]

        descricao = request.form["descricao_curso"]

        Cursos(nome = nome, classificacao = classificacao, descricao = descricao)

        return redirect(url_for("listar_cursos"))

    return render_template("cadastro_curso.html")

@app.route("/editar/curso/<codigo>", methods=("GET", "POST"))
def editar_curso(codigo):
    curso = Cursos.listaCursosMatricula(codigo)

    if request.method == "POST":
        nome = request.form["nome_curso"]

        classificacao = request.form["classificacao_curso"]

        ativo = 0
        if "ativo_curso" in request.form:
            ativo = 1

        descricao = request.form["descricao_curso"]

        Cursos.atualizar(codigo, nome, classificacao, ativo, descricao)

        return redirect(url_for("listar_cursos"))

    return render_template("editar_curso.html", curso=curso)

# Rotas Turma
@app.route("/listar/turmas")
def listar_turmas():
    turmas = Turma.listar()

    return render_template("listar_turmas.html", turmas=turmas)

@app.route("/cadastro/turma", methods=('GET', 'POST'))
def cadastro_turma():
    professores = Professor.listar()

    cursos = Cursos.listar()

    alunos = Aluno.listar()

    # Casdatro das turmas
    if request.method == 'POST':

        periodo = request.form['periodo']

        data_inicio = request.form['data_inicio']

        data_fim = request.form['data_fim']

        matricula_professor = request.form['professor']

        codigo_curso = request.form['cursos']

        # Lista de matriculas dos alunos
        alunos_selecionados = request.form.getlist('alunos')

        if len(alunos_selecionados) >= 3:
        # Enviando os dados para Classe Turma
            Turma(periodo = periodo, inicio = data_inicio , fim = data_fim, codigo_curso = codigo_curso, matricula_professor = matricula_professor, alunos=alunos_selecionados)

            return redirect(url_for('listar_turmas'))

        # A função render_template tem o propósito de ler os arquivos
        # Que estão disponíveis na pasta "templates" e apresentar no navegador do usuário
        # NOTE: o nome do arquivo é um texto
        else: 
            mensagem = "Selecione pelo menos 3 alunos"
            return render_template("cadastro_turmas.html", professores=professores, cursos=cursos, alunos=alunos,mensagem=mensagem)
    
    return render_template("cadastro_turmas.html", professores=professores, cursos=cursos, alunos=alunos, mensagem=None)
    

@app.route("/listar/turmas_alunos/<codigo_turma>")
def listar_turmas_alunos(codigo_turma):
    alunos = Turma.listarAlunos(codigo_turma)

    return render_template("listar_turmas_alunos.html", alunos=alunos, codigo_turma=codigo_turma)
