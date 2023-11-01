#Suraya Malek
#CIS 261
#Movie Guide Project Part 1


def movie_guide():
    print("The Movie List Program")
    print()
    print("Command Menu")
    print("list --> List all movies")
    print("add --> Add a movie")
    print("delete --> Delete a movie")
    print("exit --> Exit program")
          
def list(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
        print()
    
def add(movie_list):
    movie=input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added .\n")
    
def delete(movie_list):
    number = int(input("Number: "))
   
    if number < 1 or number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted. \n")
        
def main():
    movie_list =["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]
    movie_guide()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
            
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command.Please try again .\n")
    print("Bye!")
if __name__ == "__main__":
    main()
       
            
        

