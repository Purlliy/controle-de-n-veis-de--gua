from colorama import Fore, Style

niveis = []

situacao = {
    1: "Nível de água muito baixo (crítico)",
    2: "Nível de água baixo",
    3: "Nível de água médio",
    4: "Nível de água alto",
    5: "Nível de água muito alto (alerta)"
}

cores = {
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.GREEN,
    4: Fore.CYAN,
    5: Fore.BLUE
}

def verificar_nivel(nivel): # Função para verificar o nível de água e retornar a mensagem correspondente.
    if nivel not in situacao:
        print(f"{Fore.WHITE}Nível inválido! Use valores de 1 a 5.{Style.RESET_ALL}")
        return
    
    niveis.append(nivel) # Adiciona o nível informado à lista de níveis.

    situacao_atual = situacao[nivel]
    cor = cores[nivel]
    print(f"{cor}Nível de água informado: {nivel} - {situacao_atual}{Style.RESET_ALL}")

verificar_nivel(5) # Exemplo de uso da função para verificar o nível de água. Você pode alterar o valor para testar outros níveis (Sendo esses valores de 1 a 5).