## controle-de-niveis-de-agua 🧪
---
# Objetivo do programa 📃
O programa tem o objetivo de servir como um medidor do nivel da agua em um reservatorio. Mostrando o nivel, a situação do nivel (exemplo: muito baixo, alto, médio) e uma cor que sugere o perigo do nivel.

---
## Como funciona o programa 🛠
O programa utiliza a biblioteca Colorama para aplicar formatação de cores na saída do terminal, por meio de Fore (cores) e Style.RESET_ALL (reset de estilo).

Define-se uma lista niveis, utilizada para armazenar os valores de níveis de água processados durante a execução. Em seguida, são criados dois dicionários: situacao, que realiza o mapeamento entre inteiros (1 a 5) e descrições textuais dos níveis, e cores, que associa esses mesmos inteiros a constantes de cor da biblioteca.

A função verificar_nivel(nivel: int) implementa a lógica principal. Inicialmente, realiza validação verificando se a chave nivel pertence ao dicionário situacao. Em caso negativo, exibe uma mensagem de erro e encerra a execução da função com return.

Para valores válidos, o nível é adicionado à lista niveis. Em seguida, ocorre a recuperação da descrição (situacao_atual) e da cor (cor) via acesso direto por chave. Por fim, é realizada a saída formatada no terminal utilizando f-string, combinando o valor, sua descrição e a cor correspondente.

A execução do programa ocorre por meio da chamada direta da função com um argumento literal, caracterizando ausência de entrada dinâmica de dados pelo usuário.

---
## Como usar o programa ⚙
Para usar o programa, a única coisa que precisa ser feita é ir ao final do programa até que ache uma parte escrita dessa forma:verificar_nivel(5). Após ter encontrado essa parte, a única coisa que deve ser feita é trocar o número e esse número tem que estar entre 1 a 5 (exemplo: verificar_nivel(5), verificar_nivel(3), verificar_nivel(1), verificar_nivel(2)).

---
