def dividir_arquivo_por_palavras(input_file, output_prefix, max_palavras_por_arquivo):
    with open(input_file, 'r', encoding='utf-8') as file:
        contador_palavras = 0  # Conta o total de palavras escritas no arquivo atual
        contador_arquivos = 1  # Conta quantos arquivos de saída foram criados
        output_file = f"{output_prefix}_{contador_arquivos}.txt"  # Nome do primeiro arquivo de saída
        output = open(output_file, 'w', encoding='utf-8')  # Abre o primeiro arquivo de saída

        for linha in file:  # Percorre cada linha do arquivo de entrada
            palavras = linha.split()  # Divide a linha em uma lista de palavras
            num_palavras = len(palavras)  # Conta quantas palavras tem nessa linha

            if contador_palavras + num_palavras <= max_palavras_por_arquivo:
                # Se somar as palavras da linha atual ao total não ultrapassa o limite
                output.write(linha)  # Escreve a linha inteira no arquivo de saída
                contador_palavras += num_palavras  # Atualiza a contagem de palavras
            else:
                # Se adicionar as palavras ultrapassa o limite de 500.000
                palavras_restantes = max_palavras_por_arquivo - contador_palavras
                # Escreve só as palavras que cabem para atingir 500.000
                output.write(' '.join(palavras[:palavras_restantes]) + '\n')

                output.close()  # Fecha o arquivo atual pois atingimos o limite

                # Incrementa o contador de arquivos e abre um novo arquivo
                contador_arquivos += 1
                output_file = f"{output_prefix}_{contador_arquivos}.txt"
                output = open(output_file, 'w', encoding='utf-8')

                # Escreve as palavras restantes da linha no novo arquivo
                output.write(' '.join(palavras[palavras_restantes:]) + '\n')
                
                # Atualiza a contagem de palavras para as que foram para o novo arquivo
                contador_palavras = num_palavras - palavras_restantes

        output.close()  # Fecha o último arquivo de saída

# Exemplo de uso:
input_file = 'EQUIPE.txt'  # Arquivo de entrada
output_prefix = 'output_EQUIPE'  # Prefixo para os arquivos de saída
max_palavras_por_arquivo = 100000  # Número máximo de palavras por arquivo

dividir_arquivo_por_palavras(input_file, output_prefix, max_palavras_por_arquivo)
