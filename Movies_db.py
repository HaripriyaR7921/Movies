import sqlite3

#Query THE DB and return all records

def show_all():
	conn = sqlite3.connect('Movieslist.db')

	#Create a cursor
	c= conn.cursor()
	#QUERY 
	c.execute("SELECT rowid,* FROM movies")
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()

	#Close our connection
	conn.close()

#Add new record
def addmovie(movie,actor,actress,director,year):

	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("INSERT INTO movies VALUES (?,?,?,?,?)",(movie,actor,actress,director,year))
	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()

#Delete record
 
	c.execute("DELETE FROM movies WHERE rowid =7")
	

	

#Lookup

def movie_lookup(movie):
	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("SELECT * FROM movies WHERE Movie_name =(?)",(movie,))
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()

def actor_lookup(actor):
	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("SELECT * FROM movies WHERE Actor =(?)",(actor,))
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()

def actress_lookup(actress):
	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("SELECT * FROM movies WHERE Actress =(?)",(actress,))
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()

def director_lookup(director):
	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("SELECT * FROM movies WHERE Director =(?)",(director,))
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()

def year_lookup(year):
	conn = sqlite3.connect('Movieslist.db')
	c = conn.cursor()
	c.execute("SELECT * FROM movies WHERE Year = (?)",(year,))
	items = (c.fetchall())
	
	for item in items:
		print(item)

	# Commit the command
	conn.commit()
	#Close our connection
	conn.close()




