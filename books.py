

class Library:
	

		
	def add_book(self, string):
		# main -> input: title, author, published, pages
		
		title, author, published, pages = string
		
		
		with open("books.txt", "a+") as file:
			file.write("%s,%s,%s,%s\n" % (title, author, published, pages))
			
		return 1
			
			
	def list_book(self):
		
		for line in open("books.txt").read().splitlines():
			
			title, author = line.split(",") [0:2]
			print(title, author)


	def save(self, string):
		with open("books.txt", "w") as file:
			file.write( string )
			

	def remove_book(self, _title):
		# main -> input: title
		
		string = open("books.txt").read().splitlines()
		
		for index, line in enumerate(string):
			
			title, author, published, pages = line.split(',')
			
			if _title == title:
				del string[index]
	
		self.save("\n".join(string))
				
