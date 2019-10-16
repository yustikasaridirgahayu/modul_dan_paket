import rumusrumus as rms

def main():
	m = 100
	a = 25
	g = 10
	w = 50
	v = 29


	gayanewton = rms.HukumNewton2(m,a)
	gayaberat = rms.GayaBerat(m,g)
	beratsejenis = rms.BeratSejenis(w,v)

	print("HUKUM NEWTON 2")
	print("Massa Benda\t: ",m)
	print("Percepatan\t: ",a)
	print("Gaya\t\t= ",gayanewton)

	print("\nGAYA BERAT")
	print("Massa Benda\t\t: ",m)
	print("Gaya Gravitasi\t\t: ",g)
	print("Gaya Berat Benda\t= ",gayaberat)

	print("\nBERAT SEJENIS")
	print("Berat Benda\t: ",w)
	print("Volume Benda\t: ",v)
	print("Berat Sejenis\t= ",beratsejenis)

if __name__ == "__main__":
	main()