#! /usr/bin/env python
# coding: utf-8

"""
=======================================================================================================
			 _                _         _   _                    _                         
			| |__   __ _  ___| | ____ _| |_| |__   ___  _ __    / \   __ _ _   _  __ _ ___ 
			| '_ \ / _` |/ __| |/ / _` | __| '_ \ / _ \| '_ \  / _ \ / _` | | | |/ _` / __|
			| | | | (_| | (__|   < (_| | |_| | | | (_) | | | |/ ___ \ (_| | |_| | (_| \__ \
			|_| |_|\__,_|\___|_|\_\__,_|\__|_| |_|\___/|_| |_/_/   \_\__, |\__,_|\__,_|___/
						                                             |___/ Equipe: "Os Caça Vazamentos"  
	Github: https://github.com/gabrielkirsten/hackathonAguas
	              
=======================================================================================================	
	
"""

# Importação de bibliotecas
from Tkinter import *                               # biblioteca para interface gráfica
import matplotlib									# bibliotecas para plot
from ttk import *									# biblioteca para interface de abas
import sys

# Configuração necessária para utilização do matplot no Tkinter
import matplotlib.pyplot as plt						    
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import psycopg2, json								# biblioteca para conexão com banco de dados, e leitura de arquivos JSON
import numpy as np									# biblioteca para operações matemáticas
from scipy.signal import savgol_filter				# biblioteca para aplicação do filtro de Savitzky-Golay
import math

# Função para calculo de média
def average(x):
	assert len(x) > 0
	j = 0
	for k in x:
		if(k != None):
			j += k
	return float(k) / len(x)

# Função para calculo de coorelação de Pearson
def pearson_def(x, y):
	assert len(x) == len(y)
	n = len(x)
	assert n > 0
	avg_x = average(x)
	avg_y = average(y)
	diffprod = 0
	xdiff2 = 0
	ydiff2 = 0
	for idx in range(n):
		if(x[idx] != None):
			xdiff = x[idx] - avg_x
		if(y[idx] != None):	
			ydiff = y[idx] - avg_y
		diffprod += xdiff * ydiff
		xdiff2 += xdiff * xdiff
		ydiff2 += ydiff * ydiff

	return diffprod / math.sqrt(xdiff2 * ydiff2)

"""
	Classe Gui - Classe de interface para visualização de componentes
	
"""
class Gui():
	# Construtor da classe Gui
	def __init__(self, root):
		self.root = root							# criação de janela
		#self.root.attributes('-fullscreen', True)
		self.root.title("Aguas - Sistema de Análise de Dados") # titulo da janela	

		self.abas = Notebook(self.root)
		self.frame_aba1 = Frame(self.abas)
		self.frame_aba2 = Frame(self.abas)
		self.frame_aba3 = Frame(self.abas)
		self.abas.add(self.frame_aba1,text="Pressão")
		self.abas.add(self.frame_aba2,text="Condutância do solo")
		self.abas.add(self.frame_aba3,text="Vazão")
		self.abas.pack(expand="true", fill="both", side="top")
		
		self.alertas = LabelFrame(text="ALERTAS:")
		self.alertas.pack(expand="true", fill="both", side="bottom", pady=5, padx=5)
		
		self.msgAlerta = Label(self.alertas, text="")
		
		self.conectaBD()							# inicia a conexão com o banco de dados
		self.root.mainloop()						# exibe a interface
		
	# Método de criação dos gráficos
	def plotarGraficos(self):
		print "Gerando gráficos..."
		fig = plt.figure(1)								# cria um vetor de figuras para serem exibidos os gráficos
		self.mainContainerPressao = Frame(self.frame_aba1, relief=RAISED, borderwidth=1)
		self.mainContainerPressao.pack(expand="true", fill="both", side="top")
		self.mainContainerCondutancia = Frame(self.frame_aba3, relief=RAISED, borderwidth=1)
		self.mainContainerCondutancia.pack(expand="true", fill="both", side="top")  
		
		for i in range(1, 7):
			for j in range(i+1, 7):
				aux = pearson_def(self.valor[i], self.valor[j])	
				if aux < 97:
					self.msgAlerta.config(text="Anomalia na coorelação entre " + str(self.descricao[i]) + " e " + str(self.descricao[j]) + "\n")
					self.msgAlerta.pack()			
		
		
		for i in range(1, 7):						# adiciona os gráficos no vetor
			plot = plt.subplot(230+i)
			plt.title(str(self.descricao[i]), fontsize=11)
			plot.tick_params(axis='both', which='major', labelsize=6)
			plot.tick_params(axis='both', which='minor', labelsize=7)
			tempLim = savgol_filter(self.valor[i], 27, 2)	# aplica o filtro de Savitzky-Golay
			# A linha abaico comentada apresenta junto com a linha de dados do gráfico, os limiares superiores e inferiores aceitaveis calculados pelo filtro de Savitzky-Golay, esta função se encontra em testes 
			#plt.plot(self.data_mensagem[i], self.valor[i], 'r', self.data_mensagem[i], [x + 0.25*x for x in tempLim], 'b',  self.data_mensagem[i], [x - 0.25*x for x in tempLim], 'b', linewidth=1.0)
			plt.plot(self.data_mensagem[i], self.valor[i], 'r', linewidth=1.0)
			plt.grid(True)
			
		canvas = FigureCanvasTkAgg(fig, master=self.mainContainerPressao)
		plot_widget = canvas.get_tk_widget().pack(side='top', fill='both', expand='true')
		
		fig = plt.figure(2)	
		for i in range(7, 8):						# adiciona os gráficos no vetor
			plt.title(str(self.descricao[i]), fontsize=11)
			tempLim = savgol_filter(self.valor[i], 27, 2)	# aplica o filtro de Savitzky-Golay
			plt.plot(self.data_mensagem[i], self.valor[i], 'r', linewidth=1.0)
			plt.grid(True)
			
		canvas = FigureCanvasTkAgg(fig, master=self.mainContainerCondutancia)
		plot_widget = canvas.get_tk_widget().pack(side='top', fill='both', expand='true')
	
	# Método para conexão com o banco de dados
	def conectaBD(self):
		print "Conectando ao BD..."
		try: 								#try do JSON
			with open('configBD.json', 'r') as outfile:
				data = json.load(outfile)
		except:
			print("ERRO! JSON")
			sys.exit(1)
			
		try:								#try conexão banco
			conn = psycopg2.connect("dbname='"+data['dbname']+"' user='"+data['user']+"' host='"+data['host']+"' password='"+data['password']+"'")
		except:
			print("ERRO! Falha na conexão com o banco de dados!")
			sys.exit(1)
			
		self.descricao = [[]]			# declaração de uma matriz de mensagem de respostas obtidas do BD (descricao)	
		self.data_mensagem = [[]]			# declaração de uma matriz de mensagem de respostas obtidas do BD (data)
		self.valor = [[]]					# declaração de uma matriz de mensagem de respostas obtidas do BD (valor)
		
		cur = conn.cursor()					# criação de um cursor para execução de query no BD
		for i in range(1, 8):
			cur.execute("SELECT * FROM mensagem m JOIN sensor s ON m.id_sensor = s.id_sensor WHERE m.id_sensor = " + str(i) + " ORDER BY data DESC LIMIT 1000;") 
			
			self.descricao.append([])		# adiciona um novo registro na resposta (descricao)
			self.data_mensagem.append([])	# adiciona um novo registro na resposta (data)
			self.valor.append([])			# adiciona um novo registro na resposta (valor)
				
			fetch = cur.fetchall()
			self.descricao[i].append([[]])
			
			for j in range(0, len(fetch)):			# recebe todos os dados do BD
				self.descricao[i] = (fetch[j][5])
				self.data_mensagem[i].append(fetch[j][3])
				self.valor[i].append(fetch[j][2])

		self.plotarGraficos()					# exibe os gráficos dos valores coletados
		
# Método MAIN			
def main():
	root = Tk()									# criação de janela
	gui = Gui(root)								# inicia a interface	
	sys.exit(1)
if __name__ == "__main__": main()
sys.exit(1)


