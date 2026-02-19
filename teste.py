usuario = input(' Insira seu usuario: ')
print('Ola',usuario,', seja bem vindo a plataforma')
print()
senha = input('Insira sua senha: ')
print('Acesso permitido')
print()
dominio = input('Insira seu dominio: ')
print(usuario,' seu dominio é: ',dominio)
print()
email = (usuario + '@' + dominio)
print(usuario,'seu email é: ',email)

palavra = 'jaca'
#colocar a string em maiusculo
print ('Colocando todo o texto em maiusculo: ',palavra.upper())
palavra = 'JACA'
#colocar a string em minusculo
print ('Colocando todo o texto em minusculo: ',palavra.lower())

#contar caracteres da string
palavra_contar = 'banana'
print('Contar a letra b', palavra_contar.count('b'))
print('Contar a letra a', palavra_contar.count('a'))
print('Contar a letra n', palavra_contar.count('n'))

#exercicio,gerar senha automaticamente:
print('Senha gerada automaticamente: ')
print ('a'+str(email.count('a'))+'e'+str(email.count('e'))+'i'+str(email.count('i'))+'o'+str(email.count('o'))+'u'+str(email.count('u')))

#outra forma de fazer:
a = email.count('a')
e = email.count('e')
i = email.count('i')
o = email.count('o')
u = email.count('u')
print('a'+str(a)+'e'+str(e)+'i'+str(i)+'o'+str(o)+'u'+str(u))

