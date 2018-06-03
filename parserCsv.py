import csv
import json
import mysql.connector
csvfile = open('movies.csv', 'wb')
spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)


fname = "movies_metadata.csv"
file = open(fname, "rb")

try:
    reader = csv.reader(file)
    for row in reader:
        idMovie = row[5]
        nameMovie = row[8]
        genres =  row[3]
        genres = genres.replace(genres[:3], '')
        genres = genres.replace(genres[-3:], '')
        genres = genres.split('}')
        genres = genres[:2]
        x = 0
        newgenre = ''
        while x < len(genres):
            genre = genres[x].split()
            if not genre:
                print('empty')
            else:
                if x == 0:
                    genre = genre[3]
                else:
                    genre = genre[4]
                genre = genre.replace(genre[:1], '')
                if x == 0:
                    newgenre += genre
                else:
                    newgenre += "|" + genre
            x += 1
        idMovie = ''.join(idMovie)
        nameMovie = ''.join(nameMovie)
        newgenre = ''.join(newgenre)

        sendData = "" +str(idMovie)+","+str(newgenre)+","+str(nameMovie)
        spamwriter.writerow([sendData])

finally:
    file.close()
