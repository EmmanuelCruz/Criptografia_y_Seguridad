f=open("imagen.enc","rb")

dato=f.read()

imagen=open("imagen.jpg","w")
for j in range(len(dato)):
	imagen.write(chr((ord(dato[j])+155)%256))
imagen.close()
