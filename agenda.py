agenda = {}

agenda ['Larissa']=['4444-5555','larissabarbosa@iesb.edu.br']
agenda ['franscisco']=['5555-6666', 'franscisco@iesb.edu.br']

print(agenda)

#adicionando um usuário a mais
agenda ['Cesar']=['7777-77777', 'cesar@iesb.edu.br']

#visualizando as chaves do dicionário com o comando .keys{}
agenda.keys()

#formatando a visualização da agenda
#podemos percorrer os elementos do dicionário usando o elemento for

for i in agenda.keys():
  print('Nome do usuário:', i) #i vai alterar a cada execução do for
  print('Email:', agenda[i][1]) #i como índice do dicionário e mostrando a segunda posição da lista, o email
  print('Telefone:', agenda[i][0]) #i como índice do dicionário e mostrando a primeira posição da lista, o tel

  #apresentação desses dados em formato de relatório

print('Nome \t\t Email \t\t\t\t Telefone')
for i in agenda.keys():
  print('{} \t {} \t\t {}'.format(i,agenda[i][1], agenda[i][0]))

  #apresentação desses dados em formato de relatório

def mostra_Usuario():
  print('Nome \t\t Email \t\t\t\t Telefone')
  for i in agenda.keys():
    print('{} \t {} \t\t {}'.format(i,agenda[i][1], agenda[i][0]))
    
    
print(mostra_Usuario())

def mostra_Usuario_bombada(dicionario):
  print('Nome \t\t Email \t\t\t Telefone')
  for i in dicionario.keys():
    print('{} \t {} \t {}'.format(i,dicionario[i][1], dicionario[i][0]))

print(mostra_Usuario_bombada)    

#Cadastrando novos usuários na agenda

def novosUsuarios(nome, email, telefone):
  #gravando os dados do noso usuário na VARIÁVEL GLOBAL AGENDA
  agenda[nome]=[telefone, email]

#adicionando novo usuário a partir da função 

nome = input('Qual é o nome do novo usuário: ')
telefone = input('Qual é o telefone do novo usuário: ')
email = input('Qual é o email do novo usuário: ')
novosUsuarios(nome, email, telefone)  

#função para alterar os dados de um usuário 

def alterarTelefone(nome, telefone):

  if nome in agenda.keys():
    agenda[nome][0]=telefone
    print('Telefone alterado com sucesso! {} {}'.format(nome,agenda[nome][0]))

  else:
    print('Usuário não encontrado.') 

nome = input('Informe o nome do usuário que deseja alterar o telefone: ')
telefone = input('Informe o telefone que deve ser alterado: ')
alterarTelefone(nome,telefone)    

mostra_Usuario_bombada(agenda)