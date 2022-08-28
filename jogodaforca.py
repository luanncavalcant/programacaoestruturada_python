jogador_1=input('Digite seu nome jogador 1: ').capitalize()
jogador_2=input('Digite seu nome jogador 2: ').capitalize()

while True:
	plvr=input(f'{jogador_1}, entre com a palavra a ser descoberta: ').lower()
	verif=plvr.split(" ")
		
	if len(verif) <=1:
		print('ERRO!, O nome deve ser composto. EX: Cristiano Ronaldo.')
	else:	
		import time
		import os
		time.sleep(10)
		os.system('clear')

		break
palavra= []
palavra= list(plvr)
palavra.remove(' ') #luancavalcante

letras_diferentes=set(palavra) #lua ncv te

quantos_falta=[]

letras_usadas_que_ntem=[" "]

letras_usadas_que_tem=[""]

chances=len(letras_diferentes) * 4

tentativas=['_'] * len(palavra)

palavra_join=''.join(palavra)


print('-='*30)
print(f'{"JOGO DA FORCA":^50}')
print('-='*30)

print(f'Sua palavra tem {len(palavra)} letras.')

while chances>1:
	for i in range(chances):
		print(f'Você tem {chances} chances agora.')
		print(''.join (tentativas))
	
		jogada=str(input("Digite um letra: ")).lower()
		print(' ')
		
		chances-=1

		if jogada in letras_usadas_que_ntem:
				print(f'Ops.. A letra ({jogada}) ja foi escolhida.')

		elif jogada not in palavra:
			letras_usadas_que_ntem.append(jogada)
			print(f'Sinto muito, a letra ({jogada}) não tem na palavra.')

			
		if jogada in letras_usadas_que_tem:
			print(f'A letra ({jogada}) tem mas você ja escolheu antes.')
	
	
		elif jogada in palavra:
			quantas_letras_tem=palavra.count(jogada)
			quantos_falta.append(quantas_letras_tem)
			soma_quantos_falta=sum(quantos_falta)
			letras_usadas_que_tem.append(jogada)
			print(f'Parabéns a letra ({jogada}) aparece {palavra.count(jogada)} vezes, agora falta {len(palavra) - soma_quantos_falta } letras.')
			for j in range (len(palavra)):
				if palavra[j] == jogada:
					tentativas[j] = jogada
					resposta=''. join (tentativas)
					
		

		if palavra_join == resposta:
			break
		elif chances<1:
			break

	if palavra_join == resposta:
		print(f'AEEE!. {jogador_2} você acertou a palavra era ({palavra_join})')
		break
	elif chances<1:
			print('Sinto muito, suas chances acabaram.')

print('OBRIGADO POR JOGAR.')
