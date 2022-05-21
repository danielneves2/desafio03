# use esta parte de cima para declarar a 4 funções #
from unicodedata import name
from webbrowser import get

 
def add_food(nome=0,descrição=0):
    
    if type(nome) is not str or type(descrição) is not str:
        print("Ambas tem que ser string")
    
    if nome == 0 or descrição==0:
        print("você precisa passar o nome e a descrição da comida")
    
    if nome in food_list:
        print("Já existe essa comida na lista.")
    
    else:
        food_list[nome]= descrição
    
    
    print(food_list) 


def delete_food(nome=0):
    if type(nome) is not str:
        print("O nome deve ser uma string ")
    
    if nome==0:
        print("Você precisa passar o nome da comida para que possa ser deletada")
    
    if nome not in food_list:
        print("Essa comida não existe na lista, não tem como ser removida senhor.")   
    
    else:
        del food_list[nome] 

def update_food(nome=0,descrição=0):
     if type(nome) is not str or type(descrição) is not str:
         print("Ambos tem que ser uma string")
    
     if nome == 0 or descrição==0:
        print("você precisa passar  o nome e a descrição da comida")
     
     if nome not in food_list:
         print('Sorvete não está na lista')
    
     
     else:
       food_list[nome]=descrição 
def get_food(nome=0):
    if type(nome) is not str:
        print("O nome deve ser uma string")
    
    if nome==0:
        print("Você precisa passar o nome da comida para descobrir a descrição") 
    
    if nome not in food_list:
        print(f'{nome} não esta na lista')
    
    else:
        description=food_list[nome]
        print(f"a descrição de {nome} é {description}")
        

#####################################################
#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

#criação da food_list
food_list = {
  'paçoquinha': 'Um doce de amendoím brasileiro',
  'brigadeiro': 'Um doce muito delicioso',
  'pizza': 'um tipo de comida da italia',
  'hamburguer': 'comida dos USA'
}

 #####################################
######## TESTES ADD_FOOD #########
#####################################

# ADD_FOOD - TESTE 1
print("\n#### ADD_FOOD - TESTE 1")
print("Usando add_food com valores sendo int")
print("add_food(100, 23)\n")
#excuta:
add_food(100, 23)

# ADD_FOOD - TESTE 2
print("\n#### ADD_FOOD - TESTE 2")
print("Usando add_food sem passar a descrição.")
print("add_food('pizza')\n")
#excuta:
add_food('pizza')

# ADD_FOOD - TESTE 3
print("\n#### ADD_FOOD - TESTE 3")
print("Usando add_food com comida já existente.")
print("add_food('brigadeiro', 'Um doce brasileiro')\n")
#excuta:
add_food('brigadeiro', 'Um doce brasileiro')

# ADD_FOOD - TESTE 4
print("\n#### ADD_FOOD - TESTE 4")
print("Usando add_food adicionando uma comida.")
print("add_food('lasanha', 'Camadas de massa e molho')\n")
#excuta:
add_food('lasanha', 'Camadas de massa e molho') 


 #####################################
######## TESTES DELETE_FOOD #########
#####################################

# DELETE_FOOD - TESTE 1
print("\n#### DELETE_FOOD - TESTE 1")
print("Usando delete_food com valor sendo int")
print("delete_food(100)\n")
#excuta:
delete_food(100)

# DELETE_FOOD - TESTE 2
print("\n#### DELETE_FOOD - TESTE 2")
print("Usando delete_food sem nenhum valor.")
print("delete_food()\n")
#excuta:
delete_food()

# DELETE_FOOD - TESTE 3
print("\n#### DELETE_FOOD - TESTE 3")
print("Usando delete_food com comida que não existe na lista.")
print("delete_food('massa')\n")
#excuta:
delete_food('massa')

# DELETE_FOOD - TESTE 4
print("\n#### DELETE_FOOD - TESTE 4")
print("Usando delete_food removendo uma comida.")
print("delete_food('paçoquinha')\n")
#excuta:
delete_food('paçoquinha') 

 #####################################
## TESTES UPDATE_FOOD ##
#####################################

# UPDATE_FOOD - TESTE 1
print("\n#### UPDATE_FOOD - TESTE 1")
print("Usando update_food com valores sendo int")
print("update_food(100, 23)\n")
#excuta:
update_food(100, 23)

# UPDATE_FOOD - TESTE 2
print("\n#### UPDATE_FOOD - TESTE 2")
print("Usando update_food sem passar a descrição.")
print("update_food('pizza')\n")
#excuta:
update_food('pizza')

# UPDATE_FOOD - TESTE 3
print("\n#### UPDATE_FOOD - TESTE 3")
print("Usando update_food com comida não existente.")
print("update_food('sorvete', 'Um doce gelado da italia')\n")
#excuta:
update_food('sorvete', 'Um doce gelado da italia')


# UPDATE_FOOD - TESTE 4
print("\n#### UPDATE_FOOD - TESTE 4")
print("Usando update_food e atualizando uma comida.")
print("update_food('brigadeiro', 'Melhor doce do mundo.')\n")
#excuta:
update_food('brigadeiro', 'Melhor doce do mundo.') 

 #####################################
## TESTES GET_FOOD ##
#####################################

# GET_FOOD - TESTE 1
print("\n#### GET_FOOD - TESTE 1")
print("Usando get_food com valor sendo int")
print("get_food(505)\n")
#excuta:
get_food(505)

# GET_FOOD - TESTE 2
print("\n#### GET_FOOD - TESTE 2")
print("Usando get_food sem passar a comida.")
print("get_food()\n")

get_food()

# GET_FOOD - TESTE 3
print("\n#### GET_FOOD - TESTE 3")
print("Usando get_food com comida não existente.")
print("get_food('noodle')\n")
get_food('noodle')

# GET_FOOD - TESTE 4
print("\n#### GET_FOOD - TESTE 4")
print("Usando get_food e pesquisando a descrição uma comida.")
print("get_food('hamburguer')\n")
get_food('hamburguer')
  

#####!!!!!!!!!!!!!! THE END !!!!!!!!!!!!!!#####


## Linha de Chegada ##
print("\n Winners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2022 Maratona Python. Todos os direitos reservados.
# https://brunofraga.com 