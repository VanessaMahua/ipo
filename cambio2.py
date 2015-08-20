print ("EL cambio")
a = raw_input("ingresar numero: ")
b = " "
c = len(a)-1
for i in range(c+1):
	b+=a[c]
	c-=1
print "el cambio se realiso"+str(b)
