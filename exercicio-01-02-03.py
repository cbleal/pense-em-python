'''

Se você correr 10 quilômetros em 42 minutos e 42 segundos,
qual é o seu passo médio (tempo por milha em minutos e segundos)?
Qual é a sua velocidade média em milhas por hora?

R: 22.62284485786952

'''

miles = 10 * 1.61
time_hours = round(((42 * 60) + 42) / 3600, 5)
velocity_mph = miles / time_hours
print(velocity_mph)
