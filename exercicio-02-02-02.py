'''

Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias
recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro
exemplar e 75 centavos para cada exemplar adicional.
Qual é o custo total de atacado para 60 cópias?

R. 945.45

'''

custo_livro = 24.95 * 0.60
qtde_compra = 60
valor_trans = 3.00 + ((qtde_compra - 1) * 0.75)
total_compra = custo_livro * 60 + valor_trans

print(f'Total da compra foi R${total_compra:.2f}')
