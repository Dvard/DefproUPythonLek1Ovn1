my_bool = False

a = False
b = True
c = True

state = int(a) + int(b) + int(c)

if state == 0 or state == 3:
	my_bool = True
elif a or b:
	my_bool = True


print(my_bool)
