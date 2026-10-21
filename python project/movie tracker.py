import json
File="movies.json"
def load_movies():
    try:
        with open (File,"r") as file:
         return json.load(file)
    except FileNotFoundError:
         return []

def save_movies(movies):
      with open(File,"w")as file:
          json.dump(movies,file,indent=4)

movies=load_movies()
while True:
    print("movie tracker")
    print("1. Add a movie:")
    print("2. view a movie:")
    print("3. search a movie:")
    print("4. exit")
    choice=input("enter your choice (1/2/3/4): ")
    if choice=="1":
        title=input("enter a title:")
        genre=input("enter a genre:")
        rating=float(input("enter a rating out of 10: "))
        movie={
            "Title":title,
            "genre":genre,
            "rating":rating
        }
        movies.append(movie)
        save_movies(movies)
        print("movie added successfully")
    elif choice=="2":
        if len(movies)==0:
            print("not movie found")
        else:
            print("/n----All movie-----")

            for movie in movies:
                print("Title:", movie["Title"])
                print("genre:", movie["genre"])
                print("rating:", movie["rating"])
                print("------------------")
    elif choice=="3":
        search=input("enter a input a title and genre to search:")
        found=False
        for movie in movies:
            if(search in movie["Title"] or
                 search in movie["genre"]):
                print("Title:",movie["Title"])
                print("genre:",movie["genre"])
                print("rating:",movie["rating"])
                found=True
        if found==False:
            print("movie not found")
    elif choice=="4":
        print("Thank you for using movie a movie tracker")
        break
    else:
        print("Invalid choice")





       



