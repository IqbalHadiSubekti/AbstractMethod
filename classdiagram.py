from abc import ABC, abstractmethod

class BangunRuang(ABC):
	@abstractmethod
	def luas(): pass
	@abstractmethod
	def volume(): pass
	
class Balok(BangunRuang):
	def __init__(self,panjang,lebar,tinggi):
		self.panjang = panjang
		self.lebar = lebar
		self.tinggi = tinggi
	def luas(self):
		return 2*(self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
	def volume(self):
		return self.panjang * self.lebar * self.tinggi
		
class Lingkaran(BangunRuang):
	def __init__(self,phi,r):
		self.phi = phi
		self.r = r
	def luas(self):
		return self.phi * self.r**2
	def volume(self):
		pass
	
b = Balok(2,3,4)
print(b.volume())
print(b.luas())
c = Lingkaran(22/7,21)
print(c.luas())
