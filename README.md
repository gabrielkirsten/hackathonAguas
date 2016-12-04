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
![alt tag](https://cloud.githubusercontent.com/assets/15522193/20866077/ffcc81e0-ba01-11e6-9f8b-b39d8b02a13e.png)
![alt tag](https://cloud.githubusercontent.com/assets/15522193/20866080/065106f8-ba02-11e6-9158-9d64529a4d09.png)
![alt tag](https://cloud.githubusercontent.com/assets/15522193/20866078/02652e98-ba02-11e6-945f-b2f562f84748.png)

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
	|	|-- README.md (descrição do sistema)
	

------------------------------------------------------------------------		
### Estrutura de BD
O banco de dados tem a função básica de obter dados dos sensores. 
O campo de *tipo* na tabela *sensor* armazena o tipo de sensor e tem sua semântica dada por:
	
	0 - Pressão	
	1 - Vazão 
	2 - Umidade
	
![alt tag](https://cloud.githubusercontent.com/assets/15522193/20866076/fcf410a0-ba01-11e6-9438-97484d89a8e1.png)

------------------------------------------------------------------------		
### O Hardware
O hardaware consiste em um protótipo para coleta de dados, com um microcontrolador atmel na plataforma arduino com um transdutores de pressão conectados em sua porta analógica, juntamente com sensores Higrometro que é capaz de obter o fator de condutância do solo, que é relacionado á umidade do solo. 
