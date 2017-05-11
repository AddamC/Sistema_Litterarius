import sqlite3
import traceback


def selectAllAutores():
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor()
    autores = cursor.execute("SELECT * FROM autores")
    listaAutores = []

    for i in autores:
        listaAutores.append(i)
    banco.close()
    return listaAutores

def selectAllEDitoras():
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    editoras = cursor.execute("SELECT * FROM editoras")
    listaEditoras = []

    for i in editoras:
        listaEditoras.append(i)
    banco.close()
    return listaEditoras

def selectAllGeneros():
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    generos = cursor.execute ("SELECT * FROM editoras")
    listaGeneros = []

    for i in generos:
        listaGeneros.append (i)
    banco.close ()
    return listaGeneros
	
def selectAllLivros():
def selectAllClientes():
def selectAllFuncionarios():
def selectAllFornecedores():
def selectAllTransportadoras():

def selectAutorById(id):
    autor = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM autores WHERE autor_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        autor.append(i)
    banco.close()

    return autor[0]

def selectEditoraById(id):
    editora = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM editoras WHERE editora_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        editora.append(i)
    banco.close()

    return editora[0]

def selectGeneroById(id):
    genero = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.execute()
    query = "SELECT * FROM generos WHERE genero_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        genero.append(i)
    banco.close()

    return genero[0]

def selectLivrosById(id):
    livro = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.execute ()
    query = "SELECT * FROM livros WHERE livro_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        livro.append (i)
    banco.close ()

    return livro[0]

# def selectLivroById:
# def selectClienteById:
# def selectFuncionarioById:
# def selectFornecedorById:
# def selectTransporadoraById:

def inserirAutor(valor):
    try:
        banco = sqlite3.connect("Litterarius.db")
        banco.execute("INSERT INTO autores(descricao) VALUES(?);", (valor,))
        banco.commit()
        banco.close()
        print("autor inserido com sucesso")
    except:
        print("erro ao inserir autor")
        traceback.print_exc ()



def inserirEditora(valor):
    try:
        banco = sqlite3.connect('Litterarius.db')
        cursor = banco.cursor()
        banco.execute("INSERT INTO editoras(descricao) VALUES(?);", (valor,))
        banco.commit()
        banco.close()
        print("editora inserido com sucesso")
    except:
        print("erro ao inserir editora")
        traceback.print_exc ()

def inserirGenero(valor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO generos(descricao VALUES(?);", (valor,))
        banco.commit()
        banco.close()
        print("genero inserido com sucesso")
    except:
        print("erro ao inserir genero")
        traceback.print_exc ()

def inserirLivro(titulo, editora, isbn, qtde, vlr):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO livros(titulo, editora_fk, ISBN, qtde_estoque, vl_unitario)"
                      " VALUES(?,?,?,?,?);",(titulo, editora, isbn, qtde, vlr,))
        print("livro inserido com sucesso")
        banco.commit()
        banco.close()
    except:
        print("erro ao inserir livro")
        traceback.print_exc ()

def inserirCliente():
def inserirFornecedor():
def inserirFuncionario():
def inserirTransportadoras():

try:
    banco = sqlite3.connect ('Litterarius.db')
    cursor = banco.cursor ()
    banco.execute("PRAGMA foreign_keys = ON;")
    banco.close()
    print("ok")
except:
    print("n deu certo")

def criarTabelas():
    try:
        banco.execute ("CREATE TABLE editoras("
                       "editora_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "editora          VARCHAR(100) NOT NULL);")
        print("tabela editoras criada com sucesso")
    except:
        print("Erro ao criar tabela de editoras")

    try:
        banco.execute ("CREATE TABLE autores("
                       "autor_id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "autor            VARCHAR(100) NOT NULL);")
        print("Tabela autores criada com sucesso")
    except:
        print("Erro ao criar tabela de autores")

    try:
        banco.execute ("CREATE TABLE generos("
                       "genero_id        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "genero           VARCHAR(50) NOT NULL);")
        print("tabela generos criada com sucesso")
    except:
        print("erro ao criar tabela generos")

    try:
        banco.execute ("CREATE TABLE livros("
                       "livro_id                 INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "titulo                   VARCHAR(50) NOT NULL,"
                       "editora_fk               INTEGER NOT NULL,"
                       "ISBN                     VARCHAR(20),"
                       "qtde_estoque             NUMERIC,"
                       "vl_unitario              REAL NOT NULL,"
                       "FOREIGN KEY(editora_fk)  REFERENCES editoras(editora_id));")
        print("tabela livros criada com sucesso")
    except:
        print("erro ao criar tabela livros")

    try:
        banco.execute ("CREATE TABLE livros_autores("
                       "livro_id                            INTEGER,"
                       "autor_id                            INTEGER,"
                       "FOREIGN KEY(livro_id)               REFERENCES livros(livro_id),"
                       "FOREIGN KEY(autor_id)               REFERENCES autores(autor_id),"
                       "PRIMARY KEY(livro_id, autor_id));")
        print("tabela livros_autores criada com sucesso")
    except:
        print("erro ao criar tabela livros_autores")

    try:
        banco.execute ("CREATE TABLE livros_generos("
                       "livro_id                            INTEGER NOT NULL,"
                       "genero_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(livro_id)               REFERENCES livros(livro_id),"
                       "FOREIGN KEY(genero_id)              REFERENCES generos(genero_id),"
                       "PRIMARY KEY(livro_id, genero_id));")
        print("tabela livros_generos criada com sucesso")
    except:
        print("erro ao criar tabela livros_generos")

    try:
        banco.execute ("CREATE TABLE fornecedores("
                       "fornecedor_id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "descricao        VARCHAR(100),"
                       "CNPJ             VARCHAR(13));")
        print("tabela fornecedores criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores")

    try:
        banco.execute ("CREATE TABLE transportadoras("
                       "transportadora_id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "descricao            VARCHAR(100),"
                       "CNPJ                 VARCHAR(13));")
        print("tabela transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela transportadoras")

    try:
        banco.execute ("CREATE TABLE fornecedores_transportadoras("
                       "transportadora_id                INTEGER NOT NULL,"
                       "fornecedor_id                    INTEGER NOT NULL,"
                       "FOREIGN KEY(transportadora_id)   REFERENCES transportadoras(transportadora_id),"
                       "FOREIGN KEY(fornecedor_id)       REFERENCES fornecedores(fornecedor_id),"
                       "PRIMARY KEY(transportadora_id, fornecedor_id));")
        print("tabela fornecedores_transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores_transportadoras")

    try:
        banco.execute ("CREATE TABLE clientes("
                       "cliente_id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "nome         VARCHAR(100) NOT NULL,"
                       "cpf          VARCHAR(12) NOT NULL,"
                       "telefone     VARCHAR(20) NOT NULL,"
                       "endereco     VARCHAR(100) NOT NULL,"
                       "rg           VARCHAR(15) NOT NULL);")
        print("tabela clientes criada com sucesso")
    except:
        print("erro ao criar tabela clientes")

    try:
        banco.execute ("CREATE TABLE funcionarios("
                       "funcionario_id      INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "nome                VARCHAR(100) NOT NULL,"
                       "cpf                 VARCHAR(12) NOT NULL,"
                       "telefone            VARCHAR(20) NOT NULL,"
                       "endereco            VARCHAR(100) NOT NULL,"
                       "rg                  VARCHAR(15) NOT NULL,"
                       "salario             REAL NOT NULL,"
                       "turno               VARCHAR(10));")
        print("tabela funcionarios criada com sucesso")
    except:
        print("erro ao criar tabela funcionarios")

    try:
        banco.execute ("CREATE TABLE vendas("
                       "venda_id                     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "data                         DATETIME NOT NULL,"
                       "cliente_fk                   INTEGER NOT NULL,"
                       "funcionario_fk               INTEGER NOT NULL,"
                       "FOREIGN KEY(cliente_fk)      REFERENCES clientes(cliente_id),"
                       "FOREIGN KEY(funcionario_fk)  REFERENCES funcionarios(funcionario_id));")
        print("tabela vendas criada com sucesso")
    except:
        print("erro ao criar tabela vendas")
        traceback.print_exc ()

    try:
        banco.execute ("CREATE TABLE det_vendas("
                       "qtde                               NUMERIC NOT NULL,"
                       "valor                              REAL NOT NULL,"
                       "venda_id                           INTEGER NOT NULL,"
                       "livro_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(venda_id)              REFERENCES vendas(venda_id),"
                       "FOREIGN KEY(livro_id)              REFERENCES livros(livro_id)"
                       "PRIMARY KEY(venda_id, livro_id));")
        print("tabela det_vendas criada com sucesso")
    except:
        print("erro ao criar tabela det_vendas")
        traceback.print_exc ()

        banco.execute("CREATE TABLE recebimentos("
                      "venda_id                             INTEGER NOT NULL,"
                      "parcela_id                           INTEGER NOT NULL,"
                      "data_vencimento                      DATETIME NOT NULL,"
                      "vl_parcela                           REAL NOT NULL,"
                      "pago                                 BOOL NOT NULL,"
                      "FOREIGN KEY(venda_id)                REFERENCES vendas(venda_id),"
                      "PRIMARY KEY(venda_id, parcela_id));")

    try:
        banco.execute ("CREATE TABLE compras("
                       "compra_id                          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "data                               DATETIME NOT NULL,"
                       "fornecedor_fk                      INTEGER NOT NULL,"
                       "FOREIGN KEY(fornecedor_fk)         REFERENCES fornecedores(fornecedor_id));")
        print("tabela compras criada com sucesso")
    except:
        print("erro criar tabela compras ")

    try:
        banco.execute("CREATE TABLE det_compras("
                      "livro_id                 INTEGER NOT NULL,"
                      "compra_id                INTEGER NOT NULL,"
                      "data                     DATETIME NOT NULL,"
                      "FOREIGN KEY(livro_id)    REFERENCES livros(livro_id),"
                      "FOREIGN KEY(compra_id)   REFERENCES compras(compra_id)"
                      "PRIMARY KEY(livro_id, compra_id));")
        print("tabela det_compras criada com sucesso")
    except:
        print("erro ao criar tabela det_compras")

    try:
        banco.execute("CREATE TABLE pagamentos("
                      "compra_id                            INTEGER NOT NULL,"
                      "parcela_id                           INTEGER NOT NULL,"
                      "data_vencimento                      DATETIME NOT NULL,"
                      "vl_parcela                           REAL NOT NULL,"
                      "pago                                 BOOL NOT NULL,"
                      "FOREIGN KEY(compra_id)               REFERENCES vendas(venda_id),"
                      "PRIMARY KEY(compra_id, parcela_id));")
        print("tabela pagamentos criada com sucesso")
    except:
        print("erro ao criar tabela pagamentos")

# criarTabelas()

# inserirAutor("maze sei la o que")
# inserirAutor("yxyxy")
#
# inserirEditora("edit1")
# inserirEditora("edit2")

# qtdeLivros = input("Informe a qtde de livros para cadastrar: ")
# for i in range(int(qtdeLivros)):
#     livro = input("informe o livro que deseja incluir: ")
#     inserirLivro(livro, i)
#
# livros = cursor.execute("SELECT * FROM editoras")
# livros = cursor.execute("SELECT * FROM autores")
# valores = []
# for i in livros.fetchall():
#     valores.append(i)
#
# print(valores)
#
# banco.close()