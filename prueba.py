numeros=""
letras=""

for i in raw_input("Ingrese algo >> "):
  if i.isdigit():
    numeros+=i
  else:
    letras+=i

print "letras: "+letras+" numeros "+numeros


