# CPU Simulada
## AOC 2026.2


### 1. Objetivo

Este pacote contém o código para o projeto de CPU Simulada.

A CPU possui:

- dados de 8 bits;
- quatro registradores: R0, R1, R2 e R3;
- memória com 16 posições;
- PC (Program Counter);
- ULA;
- ciclo Fetch → Decode → Execute.

### 2. Arquivos

- `ula.py` — ULA e operações aritméticas/lógicas.
- `cpu.py` — estrutura principal da CPU.
- `main.py` — programa de demonstração.
- `testes.py` — testes das partes já implementadas.

### 3. O que foi implementado

Todas as funções requisitadas para a CPU foram implementadas com sucesso:

- registradores;
- memória;
- PC;
- limitação para 8 bits;
- `LOAD`;
- `JMP`;
- `HALT`;
- estrutura do ciclo Fetch → Decode → Execute.
- `STORE`;
- `ADD`;
- `SUB`;
- `AND`;
- `OR`;
- `XOR`;
- operações da ULA em `ula.py`;
- testes adicionais.

### 5. Como executar

No terminal, dentro da pasta:

```bash
python main.py
```

Para executar os testes:

```bash
python testes.py
```

### 6. Programa (Combate RPG) 

O `main.py` contém:

```text
0: LOAD R0, 20               # R0 = HP inicial do monstro (20)
1: LOAD R1, 20               # R1 = Dano base do jogador (20)
2: LOAD R2, {buff_aleatorio} # R2 = Buff de ataque sorteado (0 ou 5)
3: ADD R1, R2                # R1 = Dano total (Base + Buff)
4: LOAD R3, 5                # R3 = Defesa do monstro (5)
5: SUB R1, R3                # R1 = Dano final (Dano total - Defesa)
6: SUB R0, R1                # R0 = HP restante (HP monstro - Dano final)
7: STORE R0, 13              # Salva o HP restante na posição 13 da memória
8: HALT                      # Encerra a execução da CPU
```

A instrução `STORE R0, 13` salva o valor final do HP do monstro na memória, que é lido pelo código Python ao término da execução da CPU.

Portanto, dependendo da rolagem do dado:
```text
Se o buff for 5: Dano total = 25 | Defesa = 5 | Dano líquido = 20 | HP restante na posição 13 = 0 (Ataque Crítico)
Se o buff for 0: Dano total = 20 | Defesa = 5 | Dano líquido = 15 | HP restante na posição 13 = 5 (Monstro sobreviveu)
```

### 7. Regras

Não alterar:

- os nomes dos arquivos;
- a assinatura da função `ula()`;
- a estrutura dos registradores;
- o tamanho da memória;
- a representação de 8 bits.
