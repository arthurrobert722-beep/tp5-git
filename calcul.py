moyenne(valeurs):
	total = 0
	for i in range(len(valeurs)):
		total += valeurs[i]
	return total/i+1

print(moyenne([1,2,3,4,5]))
