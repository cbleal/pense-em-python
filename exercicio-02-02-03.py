"""
    Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
    (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
    (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro
    lugar, que horas chego em casa para o café da manhã?

    R. Hora de chegada: 07:30:06
"""

# transforma tudo para segundos
inicio = (6 * 3600) + (52 * 60)
passo_lento = (8 * 60 + 15) * 2
passo_rapido = (7 * 60 + 12) * 3
corrida = passo_lento + passo_rapido

# soma dos dois momentos
chegada = inicio + corrida

# converte o total de segundos para h, m, s
horas = chegada // 3600
minutos = (chegada % 3600) // 60
segundos = (chegada % 3600) % 60

print(f'Hora de chegada: {horas:0>2d}:{minutos:0>2}:{segundos:0>2d}')
