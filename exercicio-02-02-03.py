"""
    Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
    (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
    (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro
    lugar, que horas chego em casa para o café da manhã?

    R. Hora de chegada: 07:30:06
"""

# transforma tudo para segundos
inicio = (6 * 3600) + (52 * 60)
corrida = ((8 * 60 + 15) * 2) + ((7 * 60 + 12) *3)
# soma dos dois momentos
chegada = inicio + corrida
# converte o total de segundos para h, m, s
hora = chegada // 3600
segundos = chegada % 3600
minuto = segundos // 60
segundo = segundos % 60

print(f'Hora de chegada: {hora:0>2d}:{minuto:0>2}:{segundo:0>2d}')
