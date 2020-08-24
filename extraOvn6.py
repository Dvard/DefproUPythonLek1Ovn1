saldo = float(input('Saldo: '))
savings_saldo = float(input('Saldo (savings account): '))

serice_cost_in_cents = 15

if saldo > 1000 or savings_saldo > 1500:
	serice_cost_in_cents = 0

print(f'Service cost: {serice_cost_in_cents} cents.')
