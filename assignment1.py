""" Name: Saaipranav Subramanian
    ID: Jc927790

github.com/JCUS-CP1404/assignment-1---songs-saaieee"""

import csv  # imports Songs.csv


def main():
    file_input = open("Songs.csv", "r")  # Opens csv in read mode
    read_data = file_input.readlines()

    songs = []
    for n in read_data:
        values = n.strip().split(',')
        songs.append(values)  # appends the data

    for i in range(len(songs)):
        songs[i][1] = str(songs[i][1])
    songs.sort()
    file_input.close()  # closes the csv file
    songs_at_start = len(songs)
    print("""Songs To Learn 1.0 - by Saaipranav Subramanian
{} songs loaded""".format(songs_at_start))  # to display number of songs loaded

    user_input = main_menu()  # gets users option
    while user_input != "Q":  # the loop goes on as long as the user doesnt choose to Quit
        if user_input == "L":
            load(songs)
            user_input = main_menu()
        elif user_input == "A":
            songs.append(add_new_songs())
            songs.sort()
            user_input = main_menu()
        elif user_input == "C":
            # Making sure all songs arent already learnt
            number_of_l = 0

            for i in range(len(songs)):
                if 'l' in songs[i][3]:
                    number_of_l = number_of_l + 1
            if number_of_l == len(songs):
                print("There are no songs to learn")

            else:

                print("Enter the number of a song to mark as learned")
                songs = complete_songs(songs)
            user_input = main_menu()

        else:
            print("Invalid menu choice")  # in case the user picks any invalid choice
            user_input = main_menu()

    songs_to_Csv(songs, songs_at_start)


def main_menu():
    """Function to display the Menu"""
    print("""Menu:
L - List Songs
A - Add a new Songs
C - Complete a Song
Q - Quit""")
    user_input = input(">>> ").upper()
    return user_input


def load(songs):  # loads in the songs from csv

    songs_completed = 0
    songs_uncompleted = 0
    while songs_completed < len(songs):
        if songs[songs_completed][3] == "u":
            print("{:2}. *{:30} - {:25} ({})".format(songs_completed + 0, songs[songs_completed][0],
                                                     songs[songs_completed][1], songs[songs_completed][2]))
            songs_uncompleted = songs_uncompleted + 1  # To display the number of songs songs_uncompleted later
        else:
            print("{:2}.  {:30} - {:25} ({})".format(songs_completed + 0, songs[songs_completed][0],
                                                     songs[songs_completed][1], songs[songs_completed][2]))
        songs_completed = songs_completed + 1
    songs_completed = len(songs) - songs_uncompleted
    print("{} Songs learned, {} Songs still to learn ".format(songs_completed, songs_uncompleted))


def add_new_songs():
    """Function for adding new songs to list"""
    new_song = []

    while True:

        song_name = str(input("Title: "))
        if song_name == '' or song_name == ' ':  # Making sure the song's name isnt left blank
            print("Input can not be blank")
            continue
        break

    while True:

        song_artist = str(input("Artist: "))
        if song_artist == '' or song_artist == ' ':  # Making sure the artist's name isnt left blank
            print("Input can not be blank")
            continue
        break

    while True:
        try:
            song_year = int(input("Year: "))
            if song_year < 0:  # Making sure the song year is valid
                print("Number must be >= 0")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")

    new_song.append(song_name)  # Updating new_song list with the new inputs
    new_song.append(song_artist)
    new_song.append(song_year)
    new_song.append('u')
    print("{} by {} ({}) added to Songs list".format(song_name, song_artist,
                                                     song_year))  # formatting to show the user their recent append
    return new_song


def complete_songs(songs):
    """Function to learn a song after the user inputs the song number, it finds whether the song is already learn or
    not. if yes it states that it is already learnt if not then it registers it is now learnt """

    while True:
        try:

            complete_song = int(input(">>> "))

            if complete_song < 0:  # making sure the input is valid
                print("Number must be >= 0")
                continue

            elif complete_song >= len(songs):
                print("Invalid song number")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    if 'l' in songs[complete_song]:
        print("You have already Learned {} ".format(songs[complete_song][0]))
        return songs
    songs[complete_song][3] = 'l'
    print("{} from {} learned".format(songs[complete_song][0], songs[complete_song][1]))
    return songs


def songs_to_Csv(songs, songs_at_start):
    """Function to save the new information to the Csv file"""
    songs_added = len(songs) - songs_at_start
    songs_final = songs_added + songs_at_start
    print("""{} Songs saved to Songs.csv
Have a nice day!""".format(songs_final))
    for i in range(len(songs)):
        songs[i][1] = str(songs[i][1])
    out_file = open("songs.csv", 'w', newline='')
    writer = csv.writer(out_file)
    writer.writerows(songs)  # input the new list in csv
    out_file.close()


# calls main function
if __name__ == '__main__':
    main()
