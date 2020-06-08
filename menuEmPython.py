
def tarefa1():
	print("Tarefa 1 selecionada!")

def tarefa2():
    print("Tarefa 2 selecionada!")

def tarefa3():
    print("Tarefa 3 selecionada!")

def tarefa4():
    print("Tarefa 4 selecionada!")


def tarefa5():
    print("Tarefa 5 selecionada!")

def pause():
    print("")
    espera = input("Pressione qualquer tecla para continuar. . .")



def main():

    menuAtivo = True

    # Enquanto menuAtivo = True  fica mostrando o menu
    while (menuAtivo):
        print("")
        print("                           MENU DE TAREFAS                            ")
        print("======================================================================")
        print("* 1. Tarefa 1                                                        *")
        print("* 2. Tarefa 2                                                        *")
        print("* 3. Tarefa 3                                                        *")
        print("* 4. Tarefa 4                                                        *")
        print("* 5. Tarefa 5                                                        *")
        print("* 6. Sair                                                            *")
        print("======================================================================")
       

        opc = input("Escolha uma opção: ")
        print("")

        if opc == '1':
            tarefa1()
            pause()
        elif opc == '2':
            tarefa2()
            pause()
        elif opc == '3':
            tarefa3()
            pause()
        elif opc == '4':
           tarefa4()
           pause()
        elif opc == '5':
            tarefa5()
            pause()        
        elif opc == '6':
            menuAtivo = False
        else:
            print("")
            print("Opcao Invalida! Escolha outra opcao do menu")
            print("")
            pause() 

    print("")
    print("Programa finalizado")
            
        

# Executa o programa (O programa começa aqui)
if __name__ == "__main__":
    main()

