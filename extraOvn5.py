product_choice = input('Produkt: ')
product_price = float(input('Pris: '))
delivery = float(input('Hemleverans (0 = nej, 1 = ja): '))

delivery_cost = 0

if delivery:
	delivery_cost = 2

	if product_price > 10:
		delivery_cost = 3

print('Faktura')
print('-------------------')
print(f'{product_choice}: \t {product_price}')

if delivery_cost:
	print(f'Hemleverans: \t {delivery_cost}')

print('-------------------')
print(f'Totalpris: \t {product_price + delivery_cost}')
