class bitwise:
	array=list
	string=str
	
	
	
	def __test(numb, shift, array=[], radix=2, bit=64):

		push=array.append

		if array and array [-1][1] < radix - 1:
				
				
				kb = array [::-1]
				""" kb: tuple => bit and kb (type: int) """
				blist = list( map( lambda x: str(x [-2]), kb ))
				""" blist: array => bit (type: str)  """
				
\
				
				blist = blist + bitwise.array(bitwise.string().zfill(shift))
				return [ int(b) for b in blist ]
		m, kb = (numb % radix, numb // radix)
		push((m,kb))
		return bitwise.__test(kb, shift)
	def __ (left, enum=[1]):
		
		if len(enum) == len(left): return enum [::-1]
			
		enum.append(enum[-1] * 2)
		
		
		return bitwise.__ (left) 
	def __items(items, index): 
		return items [index]
	def shiftleft(numb, 
	shift=0):
		
		
		if shift < 0: 
			raise ValueError("negative shift count")
		left = bitwise. __test (numb if numb > 0 else - numb, shift)
		

		res = sum([ item [0] * item [1] for item in zip( left,bitwise.__ (left) ) ])
		return res if numb > 0 else -1 * res
		""" sayi sifirdan kucukse -1 ile carp degilse 1 ile carp """
	def shiftrigth(numb):
		
		return 
