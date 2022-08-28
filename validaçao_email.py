def email (agenda):
    emails=[]
    lista=[]
    for c,v in enumerate(agenda):
        emails.append(v['email'])
    for i,v2 in enumerate(emails):
        if '@' in emails[i]:
            sobra=emails[i].split('@')
            res=sobra[1] #gmaii.com
        
            arroba=emails[i].split('@')
            antes_arroba=arroba[0]

            if len(antes_arroba) >1:
                com=emails[i].endswith('.com')
                br=emails[i].endswith('.com.br')

                if com == True or br == True:
                    sobra_res=res.split('.com') #['gmail', '']
                    res_final=sobra_res[0]
                    if len(res_final) >1:
                        continue
                
                
                    else:
                        print('Email invalido')
                        print(f'{i} = {v2}')
                        lista.clear()
                        m=0
                        while m == 0:
                            indice=int(input("Digite o indice do email: "))
                            del agenda[indice] ['email']
                            x=input('Digite o novo email: ')
                            agenda [indice] ['email']=x
                        
                        
                            if '@' in x:
                                sobra=x.split('@')
                                res=sobra[1] #gmaii.com
                                
                                arroba=x.split('@')
                                antes_arroba=arroba[0]

                                if len(antes_arroba) >1:
                                    com=x.endswith('.com')
                                    br=x.endswith('.com.br')
                                    if com == True or br == True:
                                        sobra_res=res.split('.com') #['gmail', '']
                                        res_final=sobra_res[0]
                                        if len(res_final) >1:
                                            lista.append(x)
                                            agenda[indice] ['email']=lista
                                            
                                            m=1

                                        else:
                                            print('email errado')
                                            print(f'indice = {1}')
                                            m=0

                    

                                    else:
                                        print('email errado')
                                        print(f'indice = {i} ')
                                        m=0

                                else:
                                    print('email errado')
                                    print(f'indice = {i} ')
                                    
                                    m=0

                            else:
                                print('email errado')
                                print(f'indice = {i} ')
                                m=0


                        
                        while len(lista) <5:
                            tamanho=len(lista)
                            pergunta=input('Gostaria de adicionar mais emails? (S/N) ').upper() [0]
                            if pergunta == 'S':
                                print(f'So tem {5 - tamanho} espaços.')
                                novo=input('Adicione novo email: ')
                                if '@' in novo:
                                    sobra=novo.split('@')
                                    res=sobra[1] #gmaii.com
                                    
                                    arroba=novo.split('@')
                                    antes_arroba=arroba[0]

                                    if len(antes_arroba) >1:
                                        com=novo.endswith('.com')
                                        br=novo.endswith('.com.br')
                                        if com == True or br == True:
                                            sobra_res=res.split('.com') #['gmail', '']
                                            res_final=sobra_res[0]
                                            if len(res_final) >1:
                                                lista.append(novo)
                                                agenda[indice] ['email']=lista
                                            

                                            else:
                                                print('email errado')

                                        else:
                                            print('email errado')
                                            
                                            
                        
                                    else:
                                        print('email errado')
                                        
                                        

                                else:
                                    print('email errado')
                                    
                                    
                            else:
                                agenda [indice] ['email']= lista.copy()
                                if len(lista)>5:
                                    del agenda [indice] ['email'][6]
                                    break
                                break
                    

                else:
                    print('Email invalido')
                    print(f'{i} = {v2}')
                    lista.clear()
                    m=0
                    while m == 0:
                        indice=int(input("Digite o indice do email: "))
                        del agenda[indice] ['email']
                        x=input('Digite o novo email: ')
                        agenda [indice] ['email']=x
                    
                    
                        if '@' in x:
                            sobra=x.split('@')
                            res=sobra[1] #gmaii.com
                            arroba=x.split('@')
                            antes_arroba=arroba[0]

                            if len(antes_arroba) >1:
                                com=x.endswith('.com')
                                br=x.endswith('.com.br')
                                if com == True or br == True:
                                    sobra_res=res.split('.com') #['gmail', '']
                                    res_final=sobra_res[0]
                                    if len(res_final) >1:
                                        lista.append(x)
                                        agenda[indice] ['email']=lista
                                        
                                        m=1

                                    else:
                                        print('email errado')
                                        print(f'indice {i}')
                                        m=0

                

                                else:
                                    print('email errado')
                                    print(f'indice = {i} ')
                                    m=0

                            else:
                                print('email errado')
                                print(f'indice = {i} ')
                                
                                m=0

                        else:
                            print('email errado')
                            print(f'indice = {i} ')
                            m=0


                    
                    while len(lista) <5:
                        tamanho=len(lista)
                        pergunta=input('Gostaria de adicionar mais emails? (S/N) ').upper() [0]
                        if pergunta == 'S':
                            print(f'So tem {5 - tamanho} espaços.')
                            novo=input('Adicione novo email: ')
                            if '@' in novo:
                                sobra=novo.split('@')
                                res=sobra[1] #gmaii.com
                            
                                arroba=novo.split('@')
                                antes_arroba=arroba[0]

                                if len(antes_arroba) >1:
                                    com=novo.endswith('.com')
                                    br=novo.endswith('.com.br')

                                    if com == True or br == True:
                                        sobra_res=res.split('.com') #['gmail', '']
                                        res_final=sobra_res[0]
                                        if len(res_final) >1:
                                            lista.append(novo)
                                            agenda[indice] ['email']=lista

                                        else:
                                            print('email errado')    
                                        
                                    else:
                                        print('email errado')
                                        
                    
                                else:
                                    print('email errado')
                                    

                            else:
                                print('email errado')
                                
                        else:
                            agenda [indice] ['email']= lista.copy()
                            if len(lista)>5:
                                del agenda [indice] ['email'][6]
                                break
                            break




            else:
                print('Email invalido')
                print(f'{i} = {v2}')
                lista.clear()
                m=0
                while m == 0:
                    indice=int(input("Digite o indice do email: "))
                    del agenda[indice] ['email']
                    x=input('Digite o novo email: ')
                    agenda [indice] ['email']=x
                
                
                    if '@' in x:
                        sobra=x.split('@')
                        res=sobra[1] #gmaii.com
                        
                        arroba=x.split('@')
                        antes_arroba=arroba[0]

                        if len(antes_arroba) >1:
                            com=x.endswith('.com')
                            br=x.endswith('.com.br')
                            if com == True or br == True:
                                sobra_res=res.split('.com') #['gmail', '']
                                res_final=sobra_res[0]
                                if len(res_final) >1:
                                    lista.append(x)
                                    agenda[indice] ['email']=lista
                                    m=1
                                    

                                else:
                                    print('email errado')
                                    print(f'indice {i} ')
                                    m=0

            

                            else:
                                print('email errado')
                                print(f'indice = {i} ')
                                m=0

                        else:
                            print('email errado')
                            print(f'indice = {i} ')
                            
                            m=0

                    else:
                        print('email errado')
                        print(f'indice = {i} ')
                        m=0


                
                while len(lista) <5:
                    tamanho=len(lista)
                    pergunta=input('Gostaria de adicionar mais emails? (S/N) ').upper() [0]
                    if pergunta == 'S':
                        print(f'So tem {5 - tamanho} espaços.')
                        novo=input('Adicione novo email: ')
                        if '@' in novo:
                            sobra=novo.split('@')
                            res=sobra[1] #gmaii.com
                            
                            arroba=novo.split('@')
                            antes_arroba=arroba[0]

                            if len(antes_arroba) >1:
                                com=novo.endswith('.com')
                                br=novo.endswith('.com.br')

                                if com == True or br == True:
                                    sobra_res=res.split('.com') #['gmail', '']
                                    res_final=sobra_res[0]
                                    if len(res_final) >1:
                                        lista.append(novo)
                                        agenda[indice] ['email']=lista

                                    else:
                                        print('email errado')
                                    


                                else:
                                    print('email errado')
                                    
                
                            else:
                                print('email errado')
                                

                        else:
                            print('email errado')
                            
                    else:
                        agenda [indice] ['email']= lista.copy()
                        if len(lista)>5:
                            del agenda [indice] ['email'][6]
                            break
                        break                



        else:
            print('Email invalido')
            print(f'{i} = {v2} ')
            lista.clear()
            m=0
            while m == 0:
                indice=int(input("Digite o indice do email : "))
                del agenda[indice] ['email']
                x=input('Digite o novo email: ')
                agenda [indice] ['email']=x
            
            
                if '@' in x:
                    sobra=x.split('@')
                    res=sobra[1] #gmaii.com
                    arroba=x.split('@')
                    antes_arroba=arroba[0]

                    if len(antes_arroba) >1:
                        com=x.endswith('.com')
                        br=x.endswith('.com.br')
                        if com == True or br == True:
                            sobra_res=res.split('.com') #['gmail', '']
                            res_final=sobra_res[0]
                            if len(res_final) >1:
                                lista.append(x)
                                agenda[indice] ['email']=lista
                                
                                m=1
                            else:
                                print('email errado')
                                print(f'indice = {i}')
                                m=0

        

                        else:
                            print('email errado')
                            print(f'indice = {i} ')
                            m=0

                    else:
                        print('email errado')
                        print(f'indice = {i} ')
                        
                        m=0

                else:
                    print('email errado')
                    print(f'indice = {i} ')
                    m=0


            
            while len(lista) <5:
                tamanho=len(lista)
                pergunta=input('Gostaria de adicionar mais emails? (S/N) ').upper() [0]
                if pergunta == 'S':
                    print(f'So tem {5 - tamanho} espaços.')
                    novo=input('Adicione novo email: ')
                    if '@' in novo:
                        sobra=novo.split('@')
                        res=sobra[1] #gmaii.com
                        arroba=novo.split('@')
                        antes_arroba=arroba[0]

                        if len(antes_arroba) >1:
                            com=novo.endswith('.com')
                            br=novo.endswith('.com.br')
                            if com == True or br == True:
                                sobra_res=res.split('.com') #['gmail', '']
                                res_final=sobra_res[0]
                                if len(res_final) >1:
                                    lista.append(novo)
                                    agenda[indice] ['email']=lista
                                else:
                                    print('email errado')
                                


                            else:
                                print('email errado')
                                
            
                        else:
                            print('email errado')
                                

                    else:
                        print('email errado')
                        
                else:
                    agenda [indice] ['email']= lista.copy()
                    if len(lista)>5:
                        del agenda [indice] ['email'][6]
                        break
                    break     
            
    return agenda
                






#Programa Principal
agenda = []
contato = {}

while True:
    contato.clear()
    contato['nome'] = input("Nome: ")
    contato['idade'] =int(input("idade: "))
    contato['contato'] = int(input("Numero do celular:  "))
    contato['email'] = input("Email: ")
    contato['ultimo_emprego'] = input("Qual foi seu ultimo emprego: ")
    contato['cidade'] = input("Nome da cidade onde mora: ")
    agenda.append(contato.copy())
    resp = input('Quer continuar? S/N : ').upper()[0]
    if resp == 'N':
        break


res=email(agenda)

print(res)



#FUNCAO CONSULTA 
def consulta(agenda):
    pergunta=input('Gostaria de fazer sua consulta por idade[I] ou cidade[C]? ').upper()[0]
    if pergunta == 'I':
        per=int(input('Digite a idade: '))

        print(f'Pessoas com idades maiores que {per}. ')
        for i in agenda:
            if i['idade'] > per:
                print(f'{i["nome"]} = {i["idade"]}')
            
        print(' ')

        print (f'Pessoas com idades iguais a {per}. ')
        for i in agenda:
            if i['idade'] == per:
                print(f'{i["nome"]} = {i["idade"]}')

    elif pergunta == 'C':
        per=str(input('Digite a cidade: '))
        pessoas=[]
        for c in agenda:
            if c['cidade'] == per :
                pessoas.append(c['nome'])


        if len(pessoas) >= 1:
            print(f'A pessoas que moram na cidade  {per} sao')
            for i in pessoas:
                print(i)
        else:
            print('Nao tem niguem dessa cidade.')
 

while True:
    x=input('Gostaria de consulta os contatos? S/N ').upper()[0]
    if x == 'S':
        p=consulta(agenda)
        
    else:
        break



#FUNÇAO EDICAO
def editar(agenda):
    for i,v in enumerate(agenda):
        print(f'{i} = {v}')

    indice=int(input('Digite o indice do contato que você quer editar: '))
    print(agenda [indice] )
    print(' ')
    escolha=str(input('O que você quer editar? contato/ultimo_emprgo/cidade: ').lower())
    del agenda[indice] [escolha]
    novo=str(input(f'Digite o(a) novo {escolha}: '))
    agenda[indice] [escolha]=novo
    return agenda



#PROGRAMA PRINCIPAL 
while True:
    print(' ')
    e=input('Gostaria de editar algum contato? S/N ').upper()[0]
    if e == 'S':
        f=editar(agenda)
        print(f)
    else:
        break

print(f)