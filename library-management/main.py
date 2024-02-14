import sys
from os import system as console
from management import Library


lib = Library()

while 1:
	menu="""
	
Main Menu
---------------

 1. List Books
 2. Add Book
 3. Remove Book
 q. Exit
""" 
	
	
	case = input("%s\nEnter a choice (1-3):" % menu)
	

	while 2:
		
		
		if case == "2" : 
			attr = "title: ", "book author: ", "published date: ", "pages: "
			
			
			
			attr = ( input( item )  for item in attr )
			# add_book(self, attr, count=10)
			
			res = lib.add_book(attr)
			if res:
				console("clear")
				break
		elif case == "1" : 
			console("clear")
			lib.list_book()
			break
			
		elif case == "3" : 
			title = input( "book title: " )
			lib.remove_book(title)
			console("clear")
			break
		else:
			if case == "q": 
				sys.exit(1)
			else:
				console("clear")
				break
		
		
