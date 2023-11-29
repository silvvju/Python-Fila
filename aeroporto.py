from collections import deque


menu = """
-----------------------------------------
            PISTA DE DECOLAGEM
-----------------------------------------
1. Adicionar avião à fila principal
2. Autorizar decolagem na fila principal
3. Listar aviões aguardando nas filas de decolagem
4. Listar as características do primeiro avião da fila
5. Abortar decolagem na pista principal
6. Autorizar decolagem na pista alternativa
7. Encerrar o programa e emitir relatório final
"""

pista_principal = deque() #Aviões que estão aguardando decolagem na pista principal
total_principal = 0 #Total de aviões que decolaram da pista principal

pista_alternativa = deque() #Aviões que estão aguardando decolagem na pista alternativa
total_alternativa = 0 #Total de aviões que decolaram da pista alternativa

while True:
    print(menu)
    opcao = input ("Insira a opção desejada: ")
 
# Adicionar um avião à fila de espera
    if opcao == '1':
        aeronave = input("Insira a placa de identificação da aeronave: ")
        pista_principal.append(aeronave)
        len(pista_principal)
        print ("Avião adicionado à fila de espera!")
# Autorizar a decolagem do primeiro avião da fila
    if opcao == '2': 
        if len(pista_principal) > 0:
            aeronave = pista_principal[0]
            confirmacao = input (f"Você confirma a decolagem do avião {aeronave}? (S/N)")
            if confirmacao.upper() == 'S':
                pista_principal.popleft()
                len(pista_principal)
                total_principal += 1
                print (f"O avião {aeronave} decolou da pista principal.")
            else:
                print ("Decolagem adiada.")
        else:
            print ("Não há aviões na fila para decolagem na pista principal.")
# Listar aviões aguardando nas filas de decolagem
    if opcao == '3':
        if len(pista_principal) > 0:
            print ("\nPISTA PRINCIPAL")
            print ("Aviões aguardando: ", (list(pista_principal)))
            print ("Quantidade: ", len(pista_principal))
        else:
            print ("\nNão há aviões aguardando para decolagem na pista principal.")
        if len(pista_alternativa) > 0:
            print ("\nPISTA ALTERNATIVA")
            print ("Aviões aguardando: ", (list(pista_alternativa)))
            print ("Quantidade: ", len(pista_alternativa))
        else:
            print ("\nNão há aviões aguardando para decolagem na pista alternativa.")
# Listar as características do primeiro avião da fila
    if opcao == '4':
        if len(pista_principal) > 0:
            primeiro_principal = pista_principal[0]
            print ("\nPrimeira aeronave (Pista Principal):", primeiro_principal)
        else: 
            print ("\nNão há aeronaves na pista principal.")
        if len(pista_alternativa) > 0:
            primeiro_alternativa = pista_alternativa[0]
            print ("\nPrimeira aeronave (Pista Alternativa):", primeiro_alternativa)
        else:
            print ("\nNão há aeronaves na pista alternativa.")
# Abortar decolagem na pista principal 
    if opcao == '5':
        if len(pista_principal) > 0:
            aeronave = pista_principal[0]
            abortar = input (f"Você deseja abortar a decolagem do avião {aeronave}? (S/N)")
            if abortar.upper() == 'S':
                elemento = pista_principal.popleft()
                pista_alternativa.append(elemento)
                print (f"\nDecolagem cancelada! O avião {aeronave} foi transferido para a Pista Alternativa.")
            else:
                print (f"\nO avião {aeronave} continua aguardando decolagem na Pista Principal.")
# Autorizar decolagem na fila alternativa
    if opcao == '6': 
        if len(pista_alternativa) > 0:
            elemento = pista_alternativa[0]
            confirmacao = input (f"Você confirma a decolagem do avião {elemento}? (S/N)")
            if confirmacao.upper() == 'S':
                pista_alternativa.popleft()
                len(pista_alternativa)
                total_alternativa += 1
                print (f"\nO avião {elemento} decolou da pista alternativa.")
            else:
                print ("\nDecolagem adiada.")
        else:
            print ("\nNão há aviões na fila para decolagem na pista alternativa.")
# Relatório final
    if opcao == '7':
        print (f"\nTotal de aeronaves que decolaram da Pista Principal: {total_principal}")
        print (f"Total de aeronaves que decolaram da Pista Alternativa: {total_alternativa}")
        print ("\nDia finalizado com sucesso!")
        break


