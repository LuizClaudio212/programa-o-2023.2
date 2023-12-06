"""Exercicio com arquivos
Faça um progama como um formulário que solicite ao usuário:Nome,Idade,Sexo[M ou F] e Telefone.
Coloque o código dentro de uma função, e este código deve repetir até o usuário digitar 'O' (para o nome) informando que ele deseja encerrar.
Dica:
Salve esses dados em um arquivo, separando cada dado pela barra vertical (pipe)
No final da linha (após telefone) adicionar um \n
verifique se o arquivo foi criado corretamente e se os dados foram armazenados da maneira desejada.
• Agora, no mesmo arquivo, crie uma função para ler estes dados,
imprimindo de forma organizada, algo como:
• Nome: José da Silva
• Idade: 20 anos #concatene “anos” sempre depois da idade
• Sexo: Masculino #Isso mesmo, deve ter um IF para verificar se é M
ou F
• Telefone: 88888888
• Você pode colocar um loop nesta função para ler todos os dados

Para ver se você é bom mesmo, no mesmo arquivo, crie uma função
que recebe como parâmetro o sexo e RETORNA uma lista com todos
os cadastros do sexo especificado:
• Dica:
• A função pode ficar assim:

def busca_usuario_pelo_sexo(sexo):
#código para fazer a busca por sexo

• No mesmo arquivo, crie uma função que recebe como parâmetro um
nome, ou parte dele, e RETORNA uma lista com todos os cadastros
que tenham o nome igual ao valor passado como parâmetro ou
possuam parte do nome com o valor passado como parâmetro:
• Ex. Se houver um cadastro com nome “Leonardo” e o parâmetro for
“leo” deve retornar o cadastro Leonardo
• Dica:
• A função pode ficar assim:
def busca_usuario_pelo_nome(nome_procurado):
#código para fazer a busca por nome
"""
def menu():
    while True:
        print('Digite 1 para preencher o formulário.')
        print('Digite 2 para ler os dados do arquivo.')
        print('Digite 3 para buscar usuarios por sexo.')
        print('Digite 4 para buscar usuarios nome.')
        print('Digite 5 para encerrar o progama!.')

        try:
            escolha = int(input('Faça sua escolha!:'))
            if escolha not in [1,2,3,4]:
                raise ValueError('Número inválido! Escolha uma das opções!.')

            if escolha == 1:
                formulario()
            elif escolha == 2:
                ler()
            elif escolha == 3:
                print('1. Para ver pessoas do sexo Masculino.')
                print('2. Para ver pessoas do sexo Feminino.')
                try:
                    opcao = int(input('Faça sua escolha:'))
                    if opcao == 1:
                        sexo = 'Masculino'
                        busca_usuario_pelo_sexo(sexo)
                    else:
                        sexo = 'Feminino'
                        busca_usuario_pelo_sexo(sexo)
                except Exception as e:
                    print(f'Ocorreu um erro! {e}')
            elif escolha == 4:
                nome = input('Digite o nome para fazer a busca:')
                nome_procurado = nome
                busca_usuario_pelo_nome(nome_procurado)
            else:
                break
        except Exception as e:
                print(f'Ocorreu um erro! {e}')


def formulario():
    cont = 0
    while True:
        try:
            nome = (input('Qual é o seu nome?: (digite [0 ou O] para voltar ao menu!)'))
            if nome == '0' or nome.upper().strip() == 'O':
                break

            idade = int(input('Qual é a sua idade?:'))

            sexo = input('Qual seu sexo? [M/F]:')
            if sexo.upper() not in ['M', 'F']:
                raise ValueError('Sexo inválido! Digite M ou F.')
            if sexo.upper() == 'M':
                sexo = 'Masculino'
            else:
                sexo = 'Feminino'
            telefone = int(input('Digite seu número de telefone:'))
            cont +=1
        except Exception as e:
            print(f'Ocorreu um erro! {e}')
            continue

        dados_form = f'Nome: {nome} |Idade: {idade} anos|Sexo: {sexo}|Telefone: {telefone}\n'
        if cont == 1:
            with open(f'meu_arquivo.txt','w',encoding='utf-8') as arquivo:
                arquivo.write(dados_form)
                print('Operacão concluida com êxito!')

        else:
            
            try:
                with open(f'meu_arquivo.txt','a',encoding='utf-8') as arquivo:
                    arquivo.write(dados_form)
                print('Operacão concluida com êxito!')
            except Exception as e:
                print(f'Ocorreu um problema! {e}')    



def ler():
        try:
            with open(f"meu_arquivo.txt","r",encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

                for linha in linhas:
                    dados = linha.split('|')

                    for dado in dados:
                        print(dado.strip())


                    print()
        except Exception as e:
            print(f'Ocorreu um erro! {e}')
            


def busca_usuario_pelo_sexo(sexo):
    try:
        with open('meu_arquivo.txt') as arquivo:
            for linha in arquivo.readlines():
                if f'Sexo: {sexo}' in linha:
                    print(linha.strip())
    except Exception as e:
            print(f'Ocorreu um erro! {e}')

                
def busca_usuario_pelo_nome(nome_procurado):
    try:
        with open('meu_arquivo.txt') as arquivo:
            for linha in arquivo.readlines():

                if f'Nome: {nome_procurado}' in linha:
                    print(linha.strip())
                    
    except Exception as e:
            print(f'Ocorreu um erro! {e}')


def main():
    menu()
    
if __name__ == "__main__":
    main()
