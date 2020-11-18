from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import sqlite3

conn = sqlite3.connect("Litterarius.db")
df = pd.read_sql_query(" SELECT livros.titulo, generos.genero FROM livros_generos "
                       " INNER JOIN livros "
                       " on livros_generos.livros_id = livros.livros_id"
                       " INNER JOIN generos "
                       " on livros_generos.generos_id = generos.generos_id", conn)
html = df.to_html()