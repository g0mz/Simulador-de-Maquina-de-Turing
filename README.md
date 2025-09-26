# Simulador de Máquina de Turing

## Descrição

Este projeto implementa um simulador de Máquina de Turing em Python. O programa recebe a definição da máquina em um arquivo JSON e uma entrada em um arquivo TXT, simulando a execução da máquina e indicando se a entrada é aceita ou rejeitada. O simulador é voltado para fins acadêmicos, permitindo o estudo de linguagens formais, autômatos e teoria da computação.

## Funcionamento

1. **Entrada da Máquina**: A máquina de Turing é definida em um arquivo `.json`, contendo:
    - Estados da máquina
    - Alfabeto da fita
    - Símbolos de entrada
    - Estado inicial
    - Estados de aceitação
    - Função de transição  

   A entrada a ser processada é fornecida em um arquivo `.txt`, contendo a cadeia de símbolos a ser analisada.

2. **Simulação**:
    - A máquina processa a cadeia símbolo a símbolo, conforme definido na função de transição.
    - Movimentos da cabeça de leitura podem ser:
        - `R` → mover para a direita
        - `L` → mover para a esquerda
        - `S` → parar
    - A execução termina quando a máquina alcança um estado de aceitação ou não encontra transição válida.

3. **Saída**: O programa exibe na linha de comando:
    - `1` → Entrada aceita
    - `0` → Entrada rejeitada  

## Estrutura dos Arquivos

### Arquivo de Especificações


```json
{
    "initial" : 0,
    "final" : [4],
    "white" : "_",
    "transitions" : [
        {"from": 0, "to": 1, "read": "a", "write": "A", "dir":"R"},
        {"from": 1, "to": 1, "read": "a", "write": "a", "dir":"R"},
        {"from": 1, "to": 1, "read": "B", "write": "B", "dir":"R"},
        {"from": 1, "to": 2, "read": "b", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "B", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "a", "write": "a", "dir":"L"},
        {"from": 2, "to": 0, "read": "A", "write": "A", "dir":"R"},
        {"from": 0, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 4, "read": "_", "write": "_", "dir":"L"}      
    ]
}
```
### Arquivo de Entrada

#### Exemplo:

```
aabb
```

### Saída 

#### Exemplo de saída esperada:

```
1 (Aceita) ou 0 (Rejeita)
```

## Conclusão
Este projeto fornece uma ferramenta prática para estudar e simular Máquinas de Turing, permitindo compreender o funcionamento de autômatos e a teoria da computação de forma aplicada. Ele é útil para estudantes e pesquisadores que desejam testar conceitos de linguagens formais e decidibilidade de problemas.