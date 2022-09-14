import sqlite3


class Cursos:
    def __init__(self, nome, classificacao, descricao=None):
        self.nome = nome
        self.__codigo = 0
        self.classificacao = classificacao
        self.descricao = descricao

        self.banco_dados()

    @property
    def codigo(self):
        return self.__codigo

    def banco_dados(self):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Cursos (
                Nome,
                Classificacao,
                Descricao
            )
            VALUES (
                '{self.nome}',
                '{self.classificacao}',
                '{self.descricao}'
            )
        """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Cursos
            ORDER BY nome
            """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        lista_cursos = cursor.fetchall()

        conexao.close()

        return lista_cursos

    def __repr__(self):
        impressao = f'''
        --- Cadastro Cursos ---
        Código Curso: {self.__codigo}
        Nome: {self.nome}
        Classificação: {self.classificacao}
        Descrição: {self.descricao}
        '''
        return impressao
        
    @classmethod
    def listaCursosMatricula(cls, codigo):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Cursos WHERE codigo = {codigo}
                """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        listaCursos = cursor.fetchone()

        conexao.close()

        return listaCursos

    @classmethod
    def atualizar(cls, codigo, nome, classificacao, ativo, descricao):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            UPDATE Cursos SET 
                nome = '{nome}', 
                classificacao = '{classificacao}', 
                ativo = '{ativo}', 
                descricao = '{descricao}'
                WHERE codigo = '{codigo}'
            """
        cursor.execute(sql)

        conexao.commit()

        conexao.close()

if __name__ == '__main__':
    # Python = Cursos(nome='Python', classificacao='Programação')
    print(Cursos.listar())
