import Movies_db


print('''
	Welcome to movies collection!!
	Choices available:
	1.Show all movies available
	2.Lookup details using movie name
	3.Lookup details using actor
	4.Lookup details using actress
	5.Lookup details using director
	6.Lookup details using year of release
	''')
#Get choice
choice = int(input("Enter a number according to your choice:"))

#Lookup 
if choice == 1:
	Movies_db.show_all()
elif choice == 2:
	Movies_db.movie_lookup(input(("Enter movie name:")))
elif choice == 3:
	Movies_db.actor_lookup(input(("Enter actor name:")))
elif choice == 4:
	Movies_db.actress_lookup(input(("Enter actress name:")))
elif choice == 5:
	Movies_db.director_lookup(input(("Enter director name:")))
elif choice == 6:
	Movies_db.year_lookup(int(input(("Enter year:"))))

#Movies_db.movie_lookup(input("Enter the movie name:"))


