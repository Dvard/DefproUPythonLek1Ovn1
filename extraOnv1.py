num_1 = int(input('Mata in det första talet: '))
num_2 = int(input('Mata in det andra talet: '))

bigger = num_2
smaller = num_1

if num_1 > num_2:
	bigger = num_1
	smaller = num_2

print(f'{bigger} är större än {smaller}')
