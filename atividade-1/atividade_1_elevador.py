# Atividade 1 - Elevador
# Linguagens de Programação I

quantidade = int(input("Quantas pessoas serão entrevistadas? "))

elevador_a = 0
elevador_b = 0
elevador_c = 0

matutino = 0
vespertino = 0
noturno = 0

for i in range(quantidade):
    elevador = input("Elevador (A/B/C): ").upper()
    periodo = input("Período (M/V/N): ").upper()

    if elevador == "A":
        elevador_a += 1
    elif elevador == "B":
        elevador_b += 1
    elif elevador == "C":
        elevador_c += 1

    if periodo == "M":
        matutino += 1
    elif periodo == "V":
        vespertino += 1
    elif periodo == "N":
        noturno += 1

maior_elevador = max(elevador_a, elevador_b, elevador_c)

if maior_elevador == elevador_a:
    print("Elevador mais utilizado: A")
elif maior_elevador == elevador_b:
    print("Elevador mais utilizado: B")
else:
    print("Elevador mais utilizado: C")

maior_periodo = max(matutino, vespertino, noturno)
menor_periodo = min(matutino, vespertino, noturno)

if maior_periodo == matutino:
    print("Período mais utilizado: Matutino")
elif maior_periodo == vespertino:
    print("Período mais utilizado: Vespertino")
else:
    print("Período mais utilizado: Noturno")

diferenca = ((maior_periodo - menor_periodo) / quantidade) * 100
print("Diferença percentual:", diferenca, "%")
