# hackathonAguas
Projeto submetido no Hackaton das Águas. 
```
=======================================================================================================
			 _                _         _   _                    _                         
			| |__   __ _  ___| | ____ _| |_| |__   ___  _ __    / \   __ _ _   _  __ _ ___ 
			| '_ \ / _` |/ __| |/ / _` | __| '_ \ / _ \| '_ \  / _ \ / _` | | | |/ _` / __|
			| | | | (_| | (__|   < (_| | |_| | | | (_) | | | |/ ___ \ (_| | |_| | (_| \__ \
			|_| |_|\__,_|\___|_|\_\__,_|\__|_| |_|\___/|_| |_/_/   \_\__, |\__,_|\__,_|___/
						                                             |___/ Equipe: "Os Caça Vazamentos"  
	Github: https://github.com/gabrielkirsten/hackathonAguas
	              
=======================================================================================================	
```

##### Imagem do software: 
![alt tag]

O software é responsável por receber os dados do banco de dados, e analisar de maneira básica algumas relações de comportamento do sistema, como coorelações entre diferentes resposta de trasdutores de pressão. 

Linguagem: Python
Sistema Operacional: Ubuntu 16.04 LTS

BIBLIOTECAS ADICIONAIS:
  - Tkinter
  - matplotlib
  - sys
  - math
  - psycopg2
  - json
  - numpy
  - scipy

------------------------------------------------------------------------		
### Estrutura de diretórios
	.
	|-- hackathonAguas
	|	|-- hackathon.py (codigo em python)
	|	|-- configBD(example).json (template do arquivo de configuração com o BD)


------------------------------------------------------------------------		
### Estrutura de BD
O banco de dados tem a função básica de obter dados dos sensores. 
O campo de *tipo* na tabela *sensor* armazena o tipo de sensor e tem sua semântica dada por:
	0 - Pressão	
	1 - Vazão 
	2 - Umidade
	
![alt tag]

------------------------------------------------------------------------		
### O Hardware

