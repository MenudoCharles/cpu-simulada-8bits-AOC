"""
Programa (Combate RPG)
AOC 2026.2

"""

import random
from cpu import CPU


cpu = CPU()

buff_aleatorio = random.choice([0, 5])


cpu.memoria[0] = "LOAD R0, 20"  # R0 = HP inicial do monstro (20)
cpu.memoria[1] = "LOAD R1, 20"  # R1 = Dano base do jogador (20)             
cpu.memoria[2] = f"LOAD R2, {buff_aleatorio}" # R2 = Buff de ataque sorteado (0 ou 5)
cpu.memoria[3] = "ADD R1, R2"   # R1 = Dano total (Base + Buff)              
cpu.memoria[4] = "LOAD R3, 5"   # R3 = Defesa do monstro (5)              
cpu.memoria[5] = "SUB R1, R3"   # R1 = Dano final (Dano total - Defesa)              
cpu.memoria[6] = "SUB R0, R1"   # R0 = HP restante (HP monstro - Dano final)              
cpu.memoria[7] = "STORE R0, 13"  # Salva o HP restante na posição 13 da memória             
cpu.memoria[8] = "HALT" # Encerra a execução da CPU


print("======================================")
print("       CPU SIMULADA — 8 BITS - RPG")
print("======================================")
print(f"Rolagem de dado: valor do buff obtido = {buff_aleatorio}\n")

cpu.executar()

hp_restante = cpu.memoria[13]

print("======================================")
print("RESULTADO DO COMBATE")
print("======================================")

if hp_restante == 0:
    print("ATAQUE CRÍTICO! O monstro foi DERROTADO!")
    print(f"HP final do monstro: {hp_restante}")
else:
    print("O monstro resistiu ao golpe e sobreviveu!")
    print(f"HP restante do monstro: {hp_restante}")

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado()
