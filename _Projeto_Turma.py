import sqlite3


class Turma:
    def __init__(self, periodo, inicio, fim, codigo_curso, matricula_professor, alunos):
        self.__codigo = 0
        self.periodo = periodo
        self.inicio = inicio
        self.fim = fim
        self.alunos = alunos

        self.codigo_curso = codigo_curso
        self.matricula_professor = matricula_professor

        self.banco_dados()

        # self.__alunos = []

    @property
    def codigo(self):
        return self.__codigo

    # def adicionar_aluno(self, aluno):
    # self.__alunos.append(aluno)

    # def retorna_alunos(self):
    # return self.__alunos

    def banco_dados(self):

        # self.verificador()

        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
          INSERT INTO Turmas (
              Periodo,
              Data_inicio,
              Data_fim,
              Codigo_Professor,
              Codigo_Curso
          ) 
          VALUES (
              "{self.periodo}",
              "{self.inicio}",
              "{self.fim}",
              "{self.matricula_professor}",
              "{self.codigo_curso}"       
          )
          """
        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        for aluno in self.alunos:
            sql = f""" 
                INSERT INTO Turmas_Alunos (
                    Codigo_Turma,
                    Matricula_Aluno
                )
                VALUES (
                    '{self.__codigo}',
                    '{aluno}'
                )
            """

            cursor.execute(sql)

            conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT tm.codigo, tm.periodo, tm.data_inicio,
                tm.data_fim, tm.codigo_curso, cs.nome, tm.codigo_professor, pf.nome
            FROM Turmas AS tm
            INNER JOIN Cursos AS cs ON tm.codigo_curso = cs.codigo
            INNER JOIN Professores AS pf ON tm.codigo_professor = pf.matricula
        """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        listaTurmas = cursor.fetchall()

        conexao.close()

        return listaTurmas

    @classmethod
    def listarAlunos(cls, codigo_turma):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT an.matricula, an.nome, an.cpf, an.telefone, an.email 
            FROM Alunos AS an
            INNER JOIN Turmas_Alunos AS tm_an ON an.matricula = tm_an.matricula_aluno
            WHERE tm_an.codigo_turma = "{codigo_turma}"
        """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        listaAlunos = cursor.fetchall()

        conexao.close()

        return listaAlunos


    def verificador(self):
        conexao = connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        # Nesse SELECT ESTOU VERIFICANDO SE TEM INTERVALO ENTRE AS DATAS
        # SE A DATA_INICIO ESTIVER NO INTERVELAO ENTRE AS DATAS QUE ESTÃO NO BANCO DE DADOS
        # E SE TIVEREM NO MESMO PERIODO E PROFESSOR
        # A TURMA NÃO É CRIADA

        sql = f"""
                SELECT codigo FROM Turmas
                WHERE Data_inicio AND Data_fim
                BETWEEN '{self.inicio}'
                AND '{self.fim}'
                AND Codigo_Professor = '{self.matricula_professor}'
                AND Periodo = '{self.periodo}'
        """

        cursor.execute(sql)

        codigo = cursor.fetchall()

        if codigo != []:
            raise ValueError("Professor já possui uma turma nesse periodo.")

        conexao.close()

    def __repr__(self):
        return f"""Código: {self.codigo} -> {self.periodo} | {self.inicio} - {self.fim} | {self.codigo_curso} | {self.matricula_professor}"""


if __name__ == '__main__':
    python_caldeira = Turma(
        periodo='Tarde',
        inicio='2022-10-01',
        fim='2022-12-01',
        codigo_curso='3',
        matricula_professor='1'
    )
    print(python_caldeira)
