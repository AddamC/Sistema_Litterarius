BEGIN TRANSACTION;

CREATE TABLE "vendas" (
	`vendas_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`dataVenda`	DATETIME NOT NULL,
	`precoVenda` REAL NOT NULL,
	`clientes_fk` INTEGER NOT NULL,
	`funcionarios_fk` INTEGER NOT NULL
);

CREATE TABLE transportadoras(
	transportadoras_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	transportadora VARCHAR(100),
	CNPJ VARCHAR(13)
);

CREATE TABLE recebimentos(
	vendas_id INTEGER NOT NULL,
	parcelas_id INTEGER NOT NULL,
	data_vencimento DATETIME NOT NULL,
	vl_parcela REAL NOT NULL,
	pago BOOL NOT NULL,
	FOREIGN KEY(vendas_id) REFERENCES vendas(vendas_id),
	PRIMARY KEY(vendas_id, parcelas_id)
);

CREATE TABLE pagamentos(
	compras_id INTEGER NOT NULL,
	parcelas_id INTEGER NOT NULL,
	data_vencimento DATETIME NOT NULL,
	vl_parcela REAL NOT NULL,
	pago BOOL NOT NULL,
	FOREIGN KEY(compras_id)	REFERENCES vendas(vendas_id),
	PRIMARY KEY(compras_id, parcelas_id)
);

CREATE TABLE livros_generos(
	livros_id INTEGER NOT NULL,
	generos_id INTEGER NOT NULL,
	FOREIGN KEY( livros_id) REFERENCES livros(livros_id),
	FOREIGN KEY(generos_id) REFERENCES generos(generos_id),
	PRIMARY KEY(livros_id, generos_id)
);

CREATE TABLE "livros_autores" (
	`livros_id`	INTEGER NOT NULL,
	`autores_id` INTEGER NOT NULL,
	PRIMARY KEY(`livros_id`,`autores_id`)
);

CREATE TABLE "livros" (
	`livros_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`titulo` NUMERIC NOT NULL UNIQUE,
	`editoras_fk` INTEGER NOT NULL,
	`ISBN` VARCHAR(20),
	`qtde_estoque` NUMERIC NOT NULL,
	`vl_unitario` REAL NOT NULL,
	`consignado` boolean,
	FOREIGN KEY(`editoras_fk`) REFERENCES `editoras`(`editoras_id`)
);

CREATE TABLE generos(
	generos_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	genero VARCHAR(50) NOT NULL
);

CREATE TABLE "funcionarios" (
	`funcionarios_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nome` VARCHAR(100) NOT NULL,
	`cpf` VARCHAR(12) NOT NULL,
	`telefone` VARCHAR(20) NOT NULL,
	`endereco` VARCHAR(100) NOT NULL,
	`rg` VARCHAR(15) NOT NULL,
	`salario` REAL NOT NULL,
	`turno`	VARCHAR(10)
);

CREATE TABLE fornecedores_transportadoras(
	transportadoras_id INTEGER NOT NULL,
	fornecedores_id INTEGER NOT NULL,
	FOREIGN KEY(transportadoras_id) REFERENCES transportadoras(transportadoras_id),
	FOREIGN KEY(fornecedores_id) REFERENCES fornecedores(fornecedores_id),
	PRIMARY KEY(transportadoras_id,fornecedores_id)
);

CREATE TABLE fornecedores(
	fornecedores_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	fornecedor VARCHAR(100),
	CNPJ VARCHAR(13)
);

CREATE TABLE editoras(
	editoras_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	editora VARCHAR(100) NOT NULL
);

CREATE TABLE det_vendas(
	qtde NUMERIC NOT NULL,
	valor REAL NOT NULL,
	vendas_id INTEGER NOT NULL,
	livros_id INTEGER NOT NULL,
	FOREIGN KEY(vendas_id) REFERENCES vendas(vendas_id),
	FOREIGN KEY(livros_id) REFERENCES livros(livros_id),
	PRIMARY KEY(vendas_id, livros_id)
);

CREATE TABLE "det_compras" (
	`qtde`	NUMERIC NOT NULL,
	`valor`	REAL NOT NULL,
	`compras_id` INTEGER NOT NULL,
	`livros_id`	INTEGER NOT NULL,
	PRIMARY KEY(`compras_id`,`livros_id`)
);

CREATE TABLE "compras" (
	`compras_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`dataCompra` DATETIME NOT NULL,
	`precoCompra` REAL NOT NULL,
	`fornecedores_fk` INTEGER NOT NULL
);

CREATE TABLE clientes(
	clientes_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	nome VARCHAR(100) NOT NULL,
	cpf VARCHAR(12) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	endereco VARCHAR(100) NOT NULL,
	rg VARCHAR(15) NOT NULL
);

CREATE TABLE autores(
	autores_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	autor VARCHAR(100) NOT NULL
);

COMMIT;