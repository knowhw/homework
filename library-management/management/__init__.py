

class Library:


	def add_book(self, attr, count=10):
		# input -> attr: title, author, published, pages
		from time import sleep
		title, author, published, pages = attr
		
		
		with open("books.txt", "a+") as string:
			string.write("%s,%s,%s,%s\n" % (title, author, published, pages))
			# yeni kayit ve son satira bir bos satir ekle
			
		while count:
			
			sleep(.1)
			print (end=".",  flush=1)
			
			count -=1

		return 1

	def list_book(self):
		

		for line in open("books.txt").read().splitlines():
			
			title, author, published, pages = line.split(chr(44))
			print("#", title, '"%s"' % author)
			
			
	def save(self, string):
		string = string.strip()
		# alt satirdaki bos satirlari sil
		with open("books.txt", "w") as file: file.write( "%s\n" % string )
		# son satira bir bos satir ekle
	def remove_book(self, inputext):
		string=''
		# main -> input: title
		
		
		arr = [ [item] for item in open("books.txt").read().splitlines() if item ]
		# son satirdaki bos satirlari listeye alma
		for index, line in enumerate(arr):
			
			title, author, published, pages = line [0].split(chr(44)) 
			
			if inputext == title:
				del arr [index] [:]
		
		for line in arr : 
			if line:
				string += '%s\n' % ''.join(line)
		
		self.save(string)
				
				
				
				
