"""Exercicio com arquivos
Faça um progama como um formulário que solicite ao usuário:Nome,Idade,Sexo[M ou F] e Telefone.
Coloque o código dentro de uma função, e este código deve repetir até o usuário digitar 'O' (para o nome) informando que ele deseja encerrar.
Dica:
Salve esses dados em um arquivo, separando cada dado pela barra vertical (pipe)
No final da linha (após telefone) adicionar um \n
verifique se o arquivo foi criado corretamente e se os dados foram armazenados da maneira que desejada."""

def formulario():
    cont = 0
    while True:
        try:
            nome = (input('Qual é o seu nome?: (digite [0 ou O] para encerrar o progama!)'))
            if nome == '0' or nome.upper().strip() == 'O':
                break

            idade = int(input('Qual é a sua idade?:'))

            sexo = input('Qual seu sexo? [M/F]:')
            if sexo.upper() not in ['M', 'F']:
                raise ValueError('Sexo inválido! Digite M ou F.')
            
            telefone = int(input('Digite seu número de telefone:'))
            cont +=1
        except Exception as e:
            print(f'Ocorreu um erro! {e}')
            continue

        dados_form = f'Nome: {nome} | Idade: {idade} | Sexo: {sexo} | Telefone {telefone}\n'
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

def main():
    formulario()

if __name__ == "__main__":
    main()