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
"""
def menu():
    while True:
        print('Digite 1 para preencher o formulário')
        print('Digite 2 para ler algum formulário')
        print('Digite 3 para encerrar o progama!')

        try:
            escolha = int(input('Faça sua escolha!:'))
            if escolha not in [1,2,3]:
                raise ValueError('Número inválido! Escolha uma das opções!.')

            if escolha == 1:
                formulario()
            elif escolha == 2:
                ler()
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
                sexo == 'Feminino'
            telefone = int(input('Digite seu número de telefone:'))
            cont +=1
        except Exception as e:
            print(f'Ocorreu um erro! {e}')
            continue

        dados_form = f'Nome: {nome} |Idade: {idade} anos|Sexo: {sexo}|Telefone: {telefone}\n'
        if cont == 1:
            with open('meu_arquivo.txt','w') as arquivo:
                arquivo.write(dados_form)
                print('Operacão concluida com êxito!')
        else:
            try:
                escolha_nome = input('Digite o nome do seu arquivo de texto!:')
            except Exception as e:
                print(f'Ocorreu um erro! {e}')

            with open(f'{escolha_nome}.txt','w') as arquivo:
                arquivo.write(dados_form)
                print('Operacão concluida com êxito!')

def ler():
    while True:
        try:
            nome_arquivo = input('Digite o nome do arquivo que você deseja ler sem o [.txt]:')
            with open(f"{nome_arquivo}.txt","r",encoding="utf-8") as arquivo:
                nomes = arquivo.read()
                lista = nomes.split('|')
                for n in lista:
                    print(n)
            escolha = input('Deseja continuar a ver informações de arquivos?[S/N]:')
            while escolha.upper() not in ['S','N']:
                print('Apenas [S ou N]!!!')
                escolha = input('Deseja continuar a ver informações de arquivos?[S/N]:')
            if escolha.upper() == 'N':
                break
        except Exception as e:
            print(f'Ocorreu um erro! {e}')
            



def main():
    menu()
    
if __name__ == "__main__":
    main()
