def fac (toNum):
	tmp = 1
	
	for num in range(1, toNum  + 1):
		tmp = tmp * num

	return tmp

print fac(5)
print fac(6)
