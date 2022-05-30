

# from bs4 import BeautifulSoup
# import requests

# response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# web_archive =response.text

# soup = BeautifulSoup(web_archive, "html.parser")
# movies = soup.find_all(name="h3", class_="title")


# movie_list = [movie.getText() for movie in movies]
# with open("movie_list.txt", "w") as f:
#         f.write('\n' .join(movie_list))
# f.close()
# print("Done")

import secrets

clubs = {"A": 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}

def play(home, away):
    possible_scores = [0, 1, 2, 3, 4, 5, 6]

    home_score = secrets.choice(possible_scores)
    away_score = secrets.choice(possible_scores)

    if home_score > away_score:
        clubs[home] += 3
    elif home_score < away_score:
        clubs[away] += 3
    else:
        clubs[home] += 1
        clubs[away] += 1

    # return max(clubs, key=clubs.get)
    return clubs
count = 0
for i in clubs:
    for j in clubs:
        if i != j:
            print(play(i, j))
            count += 1
print(count)
            

