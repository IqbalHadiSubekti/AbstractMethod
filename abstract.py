from abc import ABC, abstractmethod
class AbstractClassExample(ABC):

	def __init__(self,value):
		self.value = value
		super().__init__()
		
	def do_public_method(self):
		print("This is as public method")
	
	''' contoh abstract method '''
	@abstractmethod
	def do_something(self):
		pass
	
class ImplementationAbstractExample(AbstractClassExample):
	''' method ini wajib diimplementasikan, karena do_public_method
		AbstractClassExample.do_something() dideklarasikan
		sebagai abstract method
	'''
	def do_something(self):
		return self.value+2
		
a = ImplementationAbstractExample(2)
a.do_public_method()
print(a.do_something())