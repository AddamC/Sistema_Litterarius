import sqlite3
import traceback


def selectAll(tabela):
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    valores = cursor.execute("SELECT * FROM " + str(tabela))
    listaValores = []
    for i in valores:
        listaValores.append(i)
    banco.close()
    return listaValores

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
	
# def selectAllLivros():
# def selectAllClientes():
# def selectAllFuncionarios():
# def selectAllFornecedores():
# def selectAllTransportadoras():

def selecById(id, tabela):
    valor = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "Select * FROM " + str(tabela) + " WHERE " \
            + str(tabela) + "_id = " + str(id)
    valores = cursor.execute(query)
    for i in valores.fetchall():
        valor.append(i)

    banco.close()

    print("VALORES: " + valores)
    print("VALOR: " + valor)

    return valor[0]

def selectAutorById(id):
    autor = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM autores WHERE autores_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        autor.append(i)
    banco.close()

    return autor[0]

def selectEditoraById(id):
    editora = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM editoras WHERE editoras_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        editora.append(i)
    banco.close()

    return editora[0]

def selectGeneroById(id):
    genero = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM generos WHERE generos_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        genero.append(i)
    banco.close()

    return genero[0]

def selectLivroById(id):
    livro = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    query = "SELECT * FROM livros WHERE livros_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        livro.append (i)
    banco.close ()

    return livro[0]

def selectClienteById(id):
    cliente = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    query = "SELECT * FROM clientes WHERE clientes_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        cliente.append (i)
    banco.close ()

    return cliente[0]

def selectFuncionarioById(id):
    func = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    query = "SELECT * FROM funcionarios WHERE funionarios_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        func.append (i)
    banco.close ()

    return func[0]

def selectFornecedorById(id):
    fornecedor = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    query = "SELECT * FROM fornecedores WHERE livros_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        fornecedor.append (i)
    banco.close ()

    return fornecedor[0]

def selectTransporadoraById(id):
    transportadora = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    query = "SELECT * FROM transportadoras WHERE livros_id=" + str (id)
    dados = cursor.execute (query)
    for i in dados.fetchall ():
        transportadora.append (i)
    banco.close ()

    return transportadora[0]

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


# Inserções
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

def inserirLivro(titulo, editora, isbn, qtde, vlr, genero, autor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO livros(titulo, editoras_fk, ISBN, qtde_estoque, vl_unitario)"
                      " VALUES(?,?,?,?,?);",(titulo, editora, isbn, qtde, vlr,))
        query = "INSERT INTO livros_generos VALUES (" \
                "(SELECT livros_id FROM livros WHERE titulo=" + str(titulo) + ")," \
                + str(genero) + ");" \
                "INSERT INTO livros_autores VALUES (" \
                "(SELECT autores_id FROM autores WHERE titulo=" + str(titulo) + ")," \
                + str(autor) + ");"
        banco.execute(query)
        print("livro inserido com sucesso")
        banco.commit()
        banco.close()
    except:
        print("erro ao inserir livro")
        traceback.print_exc ()

def inserirCliente(nome, cpf, telefone, endereco, rg):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO clientes(titulo, nome, cpf, telefone, rg)"
                      " VALUES(?,?,?,?,?);",(nome, cpf, telefone, endereco, rg,))
        print("cliente inserido com sucesso")
        banco.commit()
        banco.close()
    except:
        print("erro ao inserir cliente")
        traceback.print_exc ()

def inserirFornecedor(fornecedor, cnpj):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO clientes(titulo, nome, cpf, telefone, rg)"
                      " VALUES(?,?);",(fornecedor, cnpj,))
        print("fornecedor inserido com sucesso")
        banco.commit()
        banco.close()
    except:
        print("erro ao inserir fornecedor")
        traceback.print_exc ()

def inserirFuncionario(nome,cpf,telefone,endereco,rg,salario,turno):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute("INSERT INTO funcionarios(titulo, nome, cpf, telefone, rg)"
                      " VALUES(?,?,?,?,?);",(nome, cpf, telefone, endereco, rg, salario,turno))
        print("funcionario inserido com sucesso")
        banco.commit()
        banco.close()
    except:
        print("erro ao inserir funcionario")
        traceback.print_exc ()

def inserirTransportadoras(transportadora, cnpj):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        banco.execute ("INSERT INTO transportadoras(titulo, nome, cpf, telefone, rg)"
                       " VALUES(?,?);", (transportadora, cnpj,))
        print ("transportadora inserida com sucesso")
        banco.commit ()
        banco.close ()
    except:
        print ("erro ao inserir transportadora")
        traceback.print_exc ()

# criação das tabelas
try:
    banco = sqlite3.connect ('Litterarius.db')
    cursor = banco.cursor ()
    banco.execute("PRAGMA foreign_keys = ON;")
    banco.close()
    print("ok")
except:
    print("n deu certo")

def criarTabelas():
    banco = sqlite3.connect('Litterarius.db')
    cursor = banco.cursor()
    try:
        banco.execute ("CREATE TABLE editoras("
                       "editoras_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "editora           VARCHAR(100) NOT NULL);")
        print("tabela editoras criada com sucesso")
    except:
        print("Erro ao criar tabela de editoras")

    try:
        banco.execute ("CREATE TABLE autores("
                       "autores_id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "autor              VARCHAR(100) NOT NULL);")
        print("Tabela autores criada com sucesso")
    except:
        print("Erro ao criar tabela de autores")

    try:
        banco.execute ("CREATE TABLE generos("
                       "generos_id        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "genero            VARCHAR(50) NOT NULL);")
        print("tabela generos criada com sucesso")
    except:
        print("erro ao criar tabela generos")

    try:
        banco.execute ("CREATE TABLE livros("
                       "livros_id                   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "titulo                      VARCHAR(50) NOT NULL,"
                       "editoras_fk                 INTEGER NOT NULL,"
                       "ISBN                        VARCHAR(20),"
                       "qtde_estoque                NUMERIC,"
                       "vl_unitario                 REAL NOT NULL,"
                       "FOREIGN KEY(editoras_fk)    REFERENCES editoras(editoras_id));")
        print("tabela livros criada com sucesso")
    except:
        print("erro ao criar tabela livros")

    try:
        banco.execute ("CREATE TABLE livros_autores("
                       "livros_id                                INTEGER,"
                       "autores_id                               INTEGER,"
                       "FOREIGN KEY(livros_id)                   REFERENCES livros(livros_id),"
                       "FOREIGN KEY(autores_id)                  REFERENCES autores(autores_id),"
                       "PRIMARY KEY(livros_id, autores_id));")
        print("tabela livros_autores criada com sucesso")
    except:
        print("erro ao criar tabela livros_autores")

    try:
        banco.execute ("CREATE TABLE livros_generos("
                       "livros_id                            INTEGER NOT NULL,"
                       "generos_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(livros_id)               REFERENCES livros(livros_id),"
                       "FOREIGN KEY(generos_id)              REFERENCES generos(generos_id),"
                       "PRIMARY KEY(livros_id, generos_id));")
        print("tabela livros_generos criada com sucesso")
    except:
        print("erro ao criar tabela livros_generos")

    try:
        banco.execute ("CREATE TABLE fornecedores("
                       "fornecedores_id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "fornecedor              VARCHAR(100),"
                       "CNPJ                    VARCHAR(13));")
        print("tabela fornecedores criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores")

    try:
        banco.execute ("CREATE TABLE transportadoras("
                       "transportadoras_id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "transportadora                  VARCHAR(100),"
                       "CNPJ                            VARCHAR(13));")
        print("tabela transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela transportadoras")

    try:
        banco.execute ("CREATE TABLE fornecedores_transportadoras("
                       "transportadoras_id                        INTEGER NOT NULL,"
                       "fornecedores_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(transportadoras_id)           REFERENCES transportadoras(transportadoras_id),"
                       "FOREIGN KEY(fornecedores_id)              REFERENCES fornecedores(fornecedores_id),"
                       "PRIMARY KEY(transportadoras_id, fornecedores_id));")
        print("tabela fornecedores_transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores_transportadoras")

    try:
        banco.execute ("CREATE TABLE clientes("
                       "clientes_id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
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
                       "funionarios_id      INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
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
                       "vendas_id                     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "data                          DATETIME NOT NULL,"
                       "clientes_fk                   INTEGER NOT NULL,"
                       "funcionarios_fk               INTEGER NOT NULL,"
                       "FOREIGN KEY(clientes_fk)      REFERENCES clientes(clientes_id),"
                       "FOREIGN KEY(funcionarios_fk)  REFERENCES funcionarios(funionarios_id));")
        print("tabela vendas criada com sucesso")
    except:
        print("erro ao criar tabela vendas")
        traceback.print_exc ()

    try:
        banco.execute ("CREATE TABLE det_vendas("
                       "qtde                                    NUMERIC NOT NULL,"
                       "valor                                   REAL NOT NULL,"
                       "vendas_id                               INTEGER NOT NULL,"
                       "livros_id                               INTEGER NOT NULL,"
                       "FOREIGN KEY(vendas_id)                  REFERENCES vendas(vendas_id),"
                       "FOREIGN KEY(livros_id)                  REFERENCES livros(livros_id)"
                       "PRIMARY KEY(vendas_id, livros_id));")
        print("tabela det_vendas criada com sucesso")
    except:
        print("erro ao criar tabela det_vendas")
        traceback.print_exc ()

    try:
        banco.execute ("CREATE TABLE compras("
                       "compras_id                           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "data                                 DATETIME NOT NULL,"
                       "fornecedores_fk                      INTEGER NOT NULL,"
                       "FOREIGN KEY(fornecedores_fk)         REFERENCES fornecedores(fornecedores_id));")
        print("tabela compras criada com sucesso")
    except:
        print("erro criar tabela compras ")

    try:
        banco.execute("CREATE TABLE det_compras("
                      "livros_id                            INTEGER NOT NULL,"
                      "compras_id                           INTEGER NOT NULL,"
                      "data                                 DATETIME NOT NULL,"
                      "FOREIGN KEY(livros_id)               REFERENCES livros(livros_id),"
                      "FOREIGN KEY(compras_id)              REFERENCES compras(compras_id)"
                      "PRIMARY KEY(livros_id, compras_id));")
        print("tabela det_compras criada com sucesso")
    except:
        print("erro ao criar tabela det_compras")

    try:
        banco.execute("CREATE TABLE pagamentos("
                      "compras_id                                INTEGER NOT NULL,"
                      "parcelas_id                               INTEGER NOT NULL,"
                      "data_vencimento                           DATETIME NOT NULL,"
                      "vl_parcela                                REAL NOT NULL,"
                      "pago                                      BOOL NOT NULL,"
                      "FOREIGN KEY(compras_id)                   REFERENCES vendas(vendas_id),"
                      "PRIMARY KEY(compras_id, parcelas_id));")
        print("tabela pagamentos criada com sucesso")
    except:
        print("erro ao criar tabela pagamentos")

    banco.close()


criarTabelas()

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