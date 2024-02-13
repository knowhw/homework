from os import system as console
import sys



class Library:
	
	def __init__(self):
		
		self.xyz = "Title: ", "Book Author: ", "Published date: ", "Pages: "
		# title, author, date, pages
		
		
		
	def save(self, data, count=13):
		
		
		import time
		print
		for item in range(count):
			
			time.sleep(.1)
			print (end=".",  flush=1)
		console("touch books.txt && echo '%s' >> books.txt" % ",".join(data)+"\n")
		console("clear")
		
		return True
		
		
	def booklist(self):
		
		console("clear")
		print
		
		__=10
		
		books = open("books.txt", mode="r").read()
		
		
		for index, item in enumerate([item for item in books.splitlines() if item], 1): 
			
			title, author = item.split(",") [0:2]
			
			
			books = "%s) %s %s" % (index, title, author )
			__ = len(books) if __ < len(books) else __
			
			
			print (books)
			
		print("-" *__)


	def add_book(self):
		
		# self.booklist()
		
		return self.save([ input( item )  for item in self.xyz ])
		
	
	
		
	def remove_book(self):
		string=[]
		append=string.append
		_title = input("Book Title: ").lower()
		
		test = open("books.txt", mode="r").read().splitlines()
		books = test if test else []
		count = len([ item for item in books if _title in item.split(",") [0]  ])
		# test,test,1234,100
		
		
			
		for index, (title, 
	author, date, pages) in enumerate([ item.split(",") for item in books if item]):
			
		
			
			if _title == title.lower():
					
				try:
					del books[index]
				except:
					pass
				
			else:
				append("%s,%s,%s,%s" % (title, author, date, pages))
			
	
				
		console("echo '%s' > books.txt" % "\n".join(string))
		return self.booklist()
		
		
	def quit(self):
		pass
	


	def main(self):
		while 1:
			menu="""
			
Main Menu
---------------

 1. Add Book
 2. Remove Book
 3. List Books
 q. Exit
""" 


			
			lib = Library()
			
			
			
			case = input("%s\nEnter a choice (1-3):" % menu)
			
				
				 
			while 2:
				
				
				if case == "1" : 
					
					res = lib.add_book()
					if res:
						break
				elif case == "3" : 
				
					lib.booklist()
					break
					
				elif case == "2" : 
					
					lib.remove_book()
					break
				else:
					if case == "q": 
						sys.exit(1)
					else:
						console("clear")
						break
				
				
			










	
	
