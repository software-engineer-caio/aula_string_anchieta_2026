nome = input ('Insira seu nome: ')
sobrenome = input ('Insira seu sobrenome: ')
nomecompleto = nome+' '+sobrenome
dianascimento = input ('Insira seu dia de nascimento: ')
mesnascimento = input ('Insira seu mes de nascimento: ')
anonascimento = input ('Insira seu ano de nascimento: ')
universidade = input ('Insira o nome da sua universidade:' )
email = (nome+'.'+sobrenome+'@'+universidade+'.br')
print (nomecompleto.lower(),'o seu email de acesso é: ',email.lower())
a = email.count('a')
e = email.count('e')
i = email.count('i')
o = email.count('o')
u = email.count('u')
senha='Sua senha é:''a'+str(a)+'e'+str(e)+'i'+str(i)+'o'+str(o)+'u'+str(u)
print (senha)
#outra forma de colocar as variaveis no meio de texto
print ('Sua senha e seu email são: {}:{}'.format(senha,email))

#remover espaçao do input do usuario
var_str_problematica = '               Melancia            '
var_str_sem_espaco = var_str_problematica.strip()
print(var_str_problematica)
print(var_str_sem_espaco)

#remover sem criar outra variavel
var_str_com_espaco = '       A           '
var_str_com_espaco = var_str_com_espaco.strip()
print (var_str_com_espaco)

#colocando direto no input
var_str_espaco_print= '           B         '
print (var_str_espaco_print.strip())

#substituir dando replace
#variavel.replace('antigo','novo')
x_str = 'AAEEIIOOUU'
print(x_str.replace('A','j'))
print(x_str.replace('E','f'))

