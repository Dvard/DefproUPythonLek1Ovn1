def c_to_f(c):
	return str((9 / 5) * c + 32) + ' F'


def f_to_c(f):
	return str((5 / 9) * (f - 32)) + ' °C'


degrees = float(input('Degrees: '))
action = input('Convert to Celcius or Farenheit? (c/f): ')

action = action.lower()

result = ''

if action == 'f':
	print(c_to_f(degrees))
elif action == 'c':
	print(f_to_c(degrees))
