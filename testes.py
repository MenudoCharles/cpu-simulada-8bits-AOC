"""
TESTES
AOC 2026.2

Os testes abaixo verificam todas as partes do código.

"""

from cpu import CPU


def teste_load():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 25

    print("[OK] LOAD")


def teste_store():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "STORE R0, 10"
    cpu.memoria[2] = "HALT"

    cpu.executar()

    assert cpu.memoria[10] == 25

    print("[OK] STORE")


def teste_add():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "LOAD R1, 10"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 35

    print("[OK] ADD")


def teste_sub():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 20"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "SUB R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 12

    print("[OK] SUB")


def teste_and():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 2"
    cpu.memoria[1] = "LOAD R1, 3"
    cpu.memoria[2] = "AND R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 2

    print("[OK] AND")


def teste_or():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 2"
    cpu.memoria[1] = "LOAD R1, 3"
    cpu.memoria[2] = "OR R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 3

    print("[OK] OR")


def teste_xor():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 2"
    cpu.memoria[1] = "LOAD R1, 3"
    cpu.memoria[2] = "XOR R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 1

    print("[OK] XOR")


def teste_pc():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 1"
    cpu.memoria[1] = "LOAD R1, 2"
    cpu.memoria[2] = "HALT"

    cpu.executar()

    assert cpu.pc == 2 

    print("[OK] PC avança corretamente")


def teste_jmp():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20

    print("[OK] JMP")


def teste_halt():
    cpu = CPU()

    cpu.memoria[0] = "HALT"

    cpu.executar()

    assert cpu.halted is True

    print("[OK] HALT")


def teste_8bits():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 255"
    cpu.memoria[1] = "LOAD R1, 1"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 0

    print("[OK] Representação de 8 bits")

def teste_programa_exemplo():
    cpu=CPU()

    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"

    cpu.executar()

    assert cpu.memoria[15] == 13

    print("[OK] Programa Exemplo")



if __name__ == "__main__":

    print("Executando testes...")
    print()

    teste_load()
    teste_store()
    teste_add()
    teste_sub()
    teste_and()
    teste_or()
    teste_xor()
    teste_pc()
    teste_jmp()
    teste_halt()
    teste_programa_exemplo()
    teste_8bits()

    print()
    print("Todos os testes foram aprovados.")
