
f=open("audio.enc","rb")

dato=f.read()
nuevo=open("audio.mp3","w")
for i in range(len(dato)):
	nuevo.write(chr(((ord(dato[i])-255)*197)%256))
nuevo.close()
f.close()