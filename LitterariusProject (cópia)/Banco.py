import sqlite3
import traceback

def criarTabelas():

    banco = sqlite3.connect('Litterarius.db')
    cursor = banco.cursor()
    try:
        cursor.execute ("CREATE TABLE editoras("
                       "editoras_id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "editora           VARCHAR(100) NOT NULL);")
        print("tabela editoras criada com sucesso")
    except:
        print("Erro ao criar tabela de editoras")

    try:
        cursor.execute ("CREATE TABLE autores("
                       "autores_id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "autor              VARCHAR(100) NOT NULL);")
        print("Tabela autores criada com sucesso")
    except:
        print("Erro ao criar tabela de autores")

    try:
        cursor.execute ("CREATE TABLE generos("
                       "generos_id        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "genero            VARCHAR(50) NOT NULL);")
        print("tabela generos criada com sucesso")
    except:
        print("erro ao criar tabela generos")

    try:
        cursor.execute ("CREATE TABLE livros("
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
        cursor.execute ("CREATE TABLE livros_autores("
                       "livros_id                                INTEGER,"
                       "autores_id                               INTEGER,"
                       "FOREIGN KEY(livros_id)                   REFERENCES livros(livros_id),"
                       "FOREIGN KEY(autores_id)                  REFERENCES autores(autores_id),"
                       "PRIMARY KEY(livros_id, autores_id));")
        print("tabela livros_autores criada com sucesso")
    except:
        print("erro ao criar tabela livros_autores")

    try:
        cursor.execute ("CREATE TABLE livros_generos("
                       "livros_id                            INTEGER NOT NULL,"
                       "generos_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(livros_id)               REFERENCES livros(livros_id),"
                       "FOREIGN KEY(generos_id)              REFERENCES generos(generos_id),"
                       "PRIMARY KEY(livros_id, generos_id));")
        print("tabela livros_generos criada com sucesso")
    except:
        print("erro ao criar tabela livros_generos")

    try:
        cursor.execute ("CREATE TABLE fornecedores("
                       "fornecedores_id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "fornecedor              VARCHAR(100),"
                       "CNPJ                    VARCHAR(13));")
        print("tabela fornecedores criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores")

    try:
        cursor.execute ("CREATE TABLE transportadoras("
                       "transportadoras_id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "transportadora                  VARCHAR(100),"
                       "CNPJ                            VARCHAR(13));")
        print("tabela transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela transportadoras")

    try:
        cursor.execute ("CREATE TABLE fornecedores_transportadoras("
                       "transportadoras_id                        INTEGER NOT NULL,"
                       "fornecedores_id                           INTEGER NOT NULL,"
                       "FOREIGN KEY(transportadoras_id)           REFERENCES transportadoras(transportadoras_id),"
                       "FOREIGN KEY(fornecedores_id)              REFERENCES fornecedores(fornecedores_id),"
                       "PRIMARY KEY(transportadoras_id, fornecedores_id));")
        print("tabela fornecedores_transportadoras criada com sucesso")
    except:
        print("erro ao criar tabela fornecedores_transportadoras")

    try:
        cursor.execute ("CREATE TABLE clientes("
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
        cursor.execute ("CREATE TABLE funcionarios("
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
        cursor.execute ("CREATE TABLE vendas("
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
        cursor.execute ("CREATE TABLE det_vendas("
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
        cursor.execute ("CREATE TABLE compras("
                       "compras_id                           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "data                                 DATETIME NOT NULL,"
                       "fornecedores_fk                      INTEGER NOT NULL,"
                       "FOREIGN KEY(fornecedores_fk)         REFERENCES fornecedores(fornecedores_id));")
        print("tabela compras criada com sucesso")
    except:
        print("erro criar tabela compras ")

    try:
        cursor.execute("CREATE TABLE det_compras("
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
        cursor.execute("CREATE TABLE pagamentos("
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

    cursor.close()
    banco.close()


def selectAll(tabela):
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    valores = cursor.execute ("SELECT * FROM ?", (tabela))
    listaValores = []

    for i in valores:
        listaValores.append (i)
    cursor.close()
    banco.close ()

    return listaValores


def selectAllAutores():
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    autores = cursor.execute ("SELECT * FROM autores")
    listaAutores = []

    for i in autores:
        listaAutores.append (i)
    cursor.close()
    banco.close ()

    return listaAutores

def selectAllEDitoras():
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    editoras = cursor.execute("SELECT * FROM editoras")
    listaEditoras = []

    for i in editoras:
        listaEditoras.append(i)
    cursor.close()
    banco.close()
    return listaEditoras

def selectAllGeneros():
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    generos = cursor.execute ("SELECT * FROM editoras")
    listaGeneros = []

    for i in generos:
        listaGeneros.append (i)
    cursor.close()
    banco.close ()

    return listaGeneros
	
# def selectAllLivros():
# def selectAllClientes():
# def selectAllFuncionarios():
# def selectAllFornecedores():
# def selectAllTransportadoras():

def selectById(id, tabela):
    valor = []
    banco = sqlite3.connect ("Litterarius.db")
    cursor = banco.cursor ()
    valores = cursor.execute ("SELECT * FROM ? WHERE ?_id=?", (tabela, tabela, id,))
    for i in valores.fetchall ():
        valor.append (i)
    cursor.close()
    banco.close ()


    print("VALORES: " + str(valores))
    print("VALOR: " + str(valor))

    return valor[0]

def selectAutorById(id):
    autor = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM autores WHERE autores_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        autor.append(i)
    cursor.close()
    banco.close()

    return autor


def selectEditoraById(id):
    editora = []
    banco = sqlite3.connect("Litterarius.db")
    cursor = banco.cursor()
    query = "SELECT * FROM editoras WHERE editoras_id=" + str(id)
    dados = cursor.execute(query)
    for i in dados.fetchall():
        editora.append(i)
    cursor.close()
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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
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
    cursor.close()
    banco.close ()


    return transportadora[0]

def inserirAutor(valor):
    try:
        banco = sqlite3.connect("Litterarius.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO autores(autor) VALUES(?);", (valor,))
        banco.commit()
        cursor.close()
        banco.close()
        print("autor inserido com sucesso")
    except:
        print("erro ao inserir autor")
        traceback.print_exc ()

def inserirEditora(valor):
    try:
        banco = sqlite3.connect('Litterarius.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO editoras(descricao) VALUES(?);", (valor,))
        banco.commit()
        cursor.close()
        banco.close()
        print("editora inserido com sucesso")
    except:
        print("erro ao inserir editora")
        traceback.print_exc ()

def inserirGenero(valor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("INSERT INTO generos(descricao VALUES(?);", (valor,))
        banco.commit()
        cursor.close()
        banco.close()
        print("genero inserido com sucesso")
    except:
        print("erro ao inserir genero")
        traceback.print_exc ()

# def inserirLivro(titulo, editora, isbn, qtde, vlr, genero, autor):
    # try:
        # banco = sqlite3.connect ('Litterarius.db')
        # cursor = banco.cursor ()
        # cursor.execute("INSERT INTO livros(titulo, editora_fk, ISBN, qtde_estoque, vl_unitario)"
                      # " VALUES(?,?,?,?,?);",(titulo, editora, isbn, qtde, vlr,))
		# query = "INSERT INTO livros_generos VALUES ("
		# + "(SELECT livros_id FROM livros WHERE titulo=" + str(titulo) "),"
		# + str(genero) + ");"
		# query = "INSERT INTO livros_autores VALUES ("
		# + "(SELECT livros_id FROM livros WHERE titulo=" + str(titulo) "),"
		# + str(autor) + ");"
        # print("livro inserido com sucesso")
        # banco.commit()
        cursor.close()
        # banco.close()
    # except:
        # print("erro ao inserir livro")
        # traceback.print_exc ()
		
def inserirLivro(titulo, editora, isbn, qtde, vlr, genero, autor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("INSERT INTO livros(titulo, editora_fk, ISBN, qtde_estoque, vl_unitario)"
                       " VALUES(?,?,?,?,?);", (titulo, editora, isbn, qtde, vlr,))
        cursor.execute ("INSERT INTO livros_generos VALUES (SELECT livros_id FROM livros WHERE titulo=?),?);",
                       (titulo, genero,))
        cursor.execute ("INSERT INTO livros_autores VALUES ((SELECT livros_id FROM livros WHERE titulo=?),?);",
                       (titulo, autor))
        print ("livro inserido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()


    except:
        print ("erro ao inserir livro")
        traceback.print_exc ()


def inserirCliente(nome, cpf, telefone, endereco, rg):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("INSERT INTO clientes(nome, cpf, telefone, endereco, rg)"
                       " VALUES(?,?,?,?,?);", (nome, cpf, telefone, endereco, rg,))
        print ("cliente inserido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao inserir cliente")
        traceback.print_exc ()

def inserirTransportadoras(transportadora, cnpj):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("INSERT INTO transportadoras(transportadora, cnpj)"
                       " VALUES(?,?,?,?,?);", (transportadora, cnpj))
        print ("transportadora inserida com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao inserir transportadora")
        traceback.print_exc ()

def inserirFornecedor(fornecedor, cnpj, transportadora):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("INSERT INTO fornecedores(fornecedor, cnpj)"
                       " VALUES(?,?);", (fornecedor, cnpj,))
        cursor.execute (
            "INSERT INTO fornecedores_transportadoras VALUES ((SELECT fornecedores_id FROM fornecedores WHERE fornecedor=?),?);",
            (fornecedor, transportadora))
        print ("fornecedor inserido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()


    except:
        print ("erro ao inserir fornecedor")
        traceback.print_exc ()


def inserirFuncionario(nome, cpf, telefone, endereco, rg, salario, turno):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("INSERT INTO funcionarios(nome, cpf, telefone, endereco, rg, salario, turno)"
                       " VALUES(?,?,?,?,?);", (nome, cpf, telefone, endereco, rg, salario, turno,))
        print ("funcionario inserido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao inserir funcionario")
        traceback.print_exc ()


# TODO Updates

def alterarAutor(id, autor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE autores SET autor=? WHERE autores_id=?", (autor, id,))
        print ("autor alterado com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar autor")
        traceback.print_exc ()


def alterarGenero(id, genero):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE generos SET genero=? WHERE generos_id=?", (genero, id,))
        print ("genero alterado com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar genero")
        traceback.print_exc ()

def alterarEditora(id, editora):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE editoras SET editora=? WHERE editoras_id=?", (editora, id,))
        print ("editora alterada com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar editora")
        traceback.print_exc ()

def alterarLivro(id,titulo,editora,isbn,qtde,valor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE livros SET "
                        "titulo=?, editora_fk=?, ISBN=?, "
                        "qtde_estoque=?, vl_unitario=? "
                        "WHERE autores_id=?",
                        (titulo, editora, isbn, qtde, valor, id,))
        print ("livro alterado com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar livro")
        traceback.print_exc ()

def alterarCliente(id, nome, cpf, telefone, endereco, rg):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE clientes SET "
                        "nome=?, cpf=?, telefone=?, "
                        "endereco=?, rg=? "
                        "WHERE clientes_id=?",
                        (nome, cpf, telefone, endereco, rg, id,))
        print ("cliente alterado com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar cliente")
        traceback.print_exc ()

def alterarFuncionario(nome, cpf, telefone, endereco, rg, salario, turno):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("UPDATE funcionarios SET "
                        "nome=?, cpf=?, telefone=?, "
                        "endereco=?, rg=?, salario=?, turno=? "
                        "WHERE clientes_id=?",
                        (nome, cpf, telefone, endereco, rg, salario, turno, id,))
        print ("funcionario alterado com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao alterar funcionario")
        traceback.print_exc ()

def alterarTransportadora(id, transportadora):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("UPDATE transportadoras SET "
                       "transportadora=? "
                       "WHERE transportadoras_id=?",
                       (transportadora, id))
        print("transportadora alterada com sucesso")
        banco.commit()
        cursor.close()
        banco.close()
    except:
        print("erro ao alterar transportadora")
        traceback.print_exec()

def alterarFornecedor(id, fornecedor):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("UPDATE fornecedores SET "
                       "fornecedores=? "
                       "WHERE fornecedores_id=?")
        print("fornecedor alterado com sucesso")
        banco.commit()
        cursor.close()
        banco.close()
    except:
        print("erro ao alterar fornecedor")
        traceback.print_exec()

def excluirEditora(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("DELETE FROM editoras WHERE editoras_id=?",(id,))
        print ("editora excluida com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao excluir editora")
        traceback.print_exc ()

def excluirGenero(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("DELETE FROM generos WHERE generos_id=?",(id,))
        print ("genero excluido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao excluir genero")
        traceback.print_exc ()

def excluirAutor(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute("DELETE FROM autores WHERE autores_id=?",(id,))
        print ("autor excluido com sucesso")
        banco.commit ()
        cursor.close()
        banco.close ()

    except:
        print ("erro ao excluir autor")
        traceback.print_exc ()

def excluirLivro(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("DELETE FROM livros WHERE livros_id=?", (id,))
        print ("livro excluido com sucesso")
        banco.commit ()
        cursor.close ()
        banco.close ()

    except:
        print ("erro ao excluir livro")
        traceback.print_exc ()

def excluirFuncionario(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("DELETE FROM funcionarios WHERE funcionarios_id=?", (id,))
        print ("funcionario excluido com sucesso")
        banco.commit ()
        cursor.close ()
        banco.close ()

    except:
        print ("erro ao excluir funcionario")
        traceback.print_exc ()

def excluirCliente(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("DELETE FROM clientes WHERE clientes_id=?", (id,))
        print ("cliente excluido com sucesso")
        banco.commit ()
        cursor.close ()
        banco.close ()

    except:
        print ("erro ao excluir cliente")
        traceback.print_exc ()

def excluirFornecedor(id):
    try:
        banco = sqlite3.connect ('Litterarius.db')
        cursor = banco.cursor ()
        cursor.execute ("DELETE FROM fornecedores WHERE fornecedores_id=?", (id,))
        print ("fornecedor excluido com sucesso")
        banco.commit ()
        cursor.close ()
        banco.close ()

    except:
        print ("erro ao excluir fornecedor")
        traceback.print_exc ()


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