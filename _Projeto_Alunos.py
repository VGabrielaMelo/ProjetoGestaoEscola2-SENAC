import sqlite3


class Aluno:

    def __init__(self, nome, cpf, email, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.__matricula = 0
        # Só a classe pode alterar esse metodo
        self.telefone = telefone
        self.email = email

        self.banco_dados()

    @property
    def matricula(self):
        return self.__matricula

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if '@' in email:
            self.__email = email
        else:
            raise ValueError('E-mail inválido')

    def banco_dados(self):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Alunos (
                nome,
                cpf,
                telefone,
                email
            )
            VALUES (
                '{self.nome}',
                '{self.cpf}',
                '{self.telefone}',
                '{self.email}'
            )
        """
        cursor.execute(sql)

        self.__matricula = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Alunos
            ORDER BY nome
            """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        lista_alunos = cursor.fetchall()

        conexao.close()

        return lista_alunos

    @classmethod
    def listaAlunosMatricula(cls, matricula):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Alunos WHERE matricula = {matricula}
                """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        listaAlunos = cursor.fetchone()

        conexao.close()

        return listaAlunos

    @classmethod
    def atualizar(cls, matricula, nome, cpf, telefone, email):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            UPDATE Alunos SET 
                nome = '{nome}', 
                cpf = '{cpf}', 
                telefone = '{telefone}', 
                email = '{email}'
                WHERE matricula = '{matricula}'
            """
        cursor.execute(sql)

        conexao.commit()

        conexao.close()

    def __repr__(self):
        return f'{self.matricula}: {self.nome} - {self.cpf} - {self.telefone} - {self.email}'


if __name__ == '__main__':
    Gabi = Aluno(nome='Gabi', cpf=8790, email='vgm@vgm')
    print(Gabi.listar())
