🧮 Calculadora Escalável em Python
---
Este projeto é uma evolução de um script básico de calculadora, refatorado para aplicar conceitos de Modularização, Dicionários de Funções (Dispatch Tables) e Tratamento de Exceções.

🚀 Evolução do Projeto
---
O objetivo desta nova versão foi aplicar feedbacks de melhoria recebidos em estudos anteriores, focando em:

Reutilização de Código: Operações matemáticas isoladas em funções independentes.

Escalabilidade: Uso de um dicionário para mapear operações, eliminando condicionais if/elif excessivas.

Robustez: Implementação de tratamento de erros para entradas não numéricas (ValueError) e divisão por zero (ZeroDivisionError).

🛠️ Tecnologias Utilizadas
---
Python 3.x


🏗️ Estrutura do Código
---
1. Funções de Operação: As funções soma, subtracao, multiplicacao e divisao são puras, facilitando testes unitários futuros.

```python
def soma (number1, number2):
    return number1 + number2
```

2. Mapeamento por Dicionário: A lógica de seleção foi simplificada. Em vez de percorrer vários ifs, o programa acessa diretamente a função necessária através da chave do dicionário:

```Python
operacoes = {'1': soma, '2': subtracao, '3': multiplicacao, '4': divisao}
```

3. Tratamento de Erros: A função ler_numero garante que o sistema não trave caso o usuário digite letras, mantendo o loop até que um valor válido seja inserido.

```Python
def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print('Entrada invalida.\nDigite um número.')
```

🔧 Como Executar
---
Certifique-se de ter o Python instalado.

Clone o repositório:

```Bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Execute o script:

```Bash
python Calculadora.py
```

📈 Próximos Passos (Roadmap)
---
[ ] Adicionar operações avançadas (Potência, Raiz Quadrada).

[ ] Criar uma interface gráfica (GUI) com Tkinter ou PySide.

[ ] Implementar histórico de operações realizadas.