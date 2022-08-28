def leiavalor(msg):
    valor=0
    if msg == 'Q':
        q1=int(input('Digite aresta 1:' ))
        q2=int(input('Digite aresta 2:' ))
        valor = q1*q2

        if q1 == q2:
            print(f'É um quadrado e a sua area é de {valor}') 
        else:
            print(f'É um retangulo e a sua area é de {valor}')
            
    elif msg == 'T':
        t1=int(input("Digite aresta 1: "))
        t2=int(input("Digite aresta 2: "))
        t3=int(input("Digite aresta 3: "))
        if t1+t2>t3 and t2+t3>t1 and t3+t1>t2:
            print('é triangulo')
            if t1>t2 and t1>t3:
                h=t1
                co=t2
                ca=t3
            elif t2>t1 and t2>t3:
                h=t2
                co=t1
                ca=t3
            else:
                h=t3
                co=t1
                ca=t2
            
            if h**2 == (co**2 + ca**2):
                print('é triangulo retangulo')
            else:
                print('Nao é triangulo retangulo')    

            if t1==t2==t3:
                import math
                raiz=math.sqrt(3)
                valor = ((4**2) * raiz)/4
                print(f'É triangulo equilatero e a sua area é de {valor}')
                    

            elif t1 !=t2 != t3 != t1:
                import math
                soma=(t1+t2+t3)/2
                valor=math.sqrt(soma*(soma-t1) * (soma-t2)  *(soma-t3))
                print(f'É um triangulo escaleno e a sua area é de {valor}')
				

            else:
                if t1!=t2 and t1!=t3:
                    div=t1/2
                    h=t2**2- div**2
                    altura= h**(1/2)
                    valor= 1/2 * t1 * altura
                    print(f'É um triângulo isoceles e a sua area é de {valor}')
                elif t2!=t1 and t2!=t3:
                    div=t2/2
                    h=t1**2- div**2
                    altura= h**(1/2)
                    valor=1/2 * t2 * altura
                    print(f'É um triângulo isoceles e a sua area é de {valor}')
                else:
                    div=t3/2
                    h=t1**2- div**2
                    altura= h**(1/2)
                    valor=1/2 * t3 * altura
                    print(f'É um triângulo isoceles e a sua area é de {valor}')

        else:
            print('Não é triangulo')



#Programa principal
per=input('Digite (Q) para quadrado ou (T) para triangulo : ').upper()[0]
leiavalor(per)