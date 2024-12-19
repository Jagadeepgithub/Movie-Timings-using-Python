current_movies={"BRO":"11:00 AM","THE TITAN":"3:00 PM","THE OSTRICH":"5:00 PM","BANG BANG":"7:00 PM"}
print("The showing movies today are:")
for key in current_movies:
    print(key)
movie=input("What movie do you want to watch of the showtime for?\n")
showtime=current_movies.get(movie) 
if showtime==None:
    print("Requestwd movie isn't playing")
else:
    print("The movie",movie,"is  playing",showtime)