import datetime
import random
from prettytable import PrettyTable
from copy import deepcopy
import json

class Song:
    songs = []

    def __init__(self, title, artist, album, length_):
        self.title = title
        self.artist = artist
        self.album = album
        self.length_ = length_

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        if hash(self.title) == hash(other.title)\
                and hash(self.artist) == hash(other.artist)\
                and hash(self.album) == hash(other.album)\
                and hash(self.length) == hash(other.length):
            return True
        return False

    def __hash__(self):
        return hash(self.artist) + hash(self.title)\
            + hash(self.album) + hash(self.length_)

    def length(self, **kwargs):
        time_list = [int(i) for i in self.length_.split(':')]
        if kwargs:
            dict_ = dict(**kwargs)
            for key, value in dict_.items():
                if key == 'seconds' and value:
                    if len(time_list) == 2:
                        return time_list[0] * 60 + time_list[1]
                if key == 'minutes' and value:
                    if len(time_list) == 2:
                        return time_list[0]
                    elif len(time_list) == 3:
                        return time_list[0] * 60 + time_list[1]
                if key == 'hours' and value:
                    if len(time_list) == 3:
                        return time_list[0]
        else:
            return self.length_

    def get_time(self):
        return self.length_


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_of_songs = []
        self.list_of_times = []
        self.songs = []
        self.played = []

    def __str__(self):
        return '{}'.format(self.name)

    def add_song(self, song):
        self.list_of_songs.append(song)
        self.songs.append(song)

    def remove_song(self, song):
        self.list_of_songs.remove(song)

    def total_length(self):
        fin_result = []
        for song in self.list_of_songs:
            self.list_of_times.append(song.get_time())
        for i in self.list_of_times:
            try:
                hour, min, sec = i.split(':')
                hour = int(hour)
                min = int(min)
                sec = int(sec)
            except ValueError:
                return 0
            result = hour * 60 * 60 + min * 60 + sec
            fin_result.append(result)
        return str(datetime.timedelta(seconds=sum(fin_result)))

    def print_artists(self):
        return self.list_of_songs

    def artists(self):
        dict_of_artists = dict()
        for i in self.list_of_songs:
            dict_of_artists[i.artist] = 0
        for i in self.list_of_songs:
            dict_of_artists[i.artist] += 1
        return dict_of_artists

    def next_song(self):
        if self.repeat:
            if len(self.songs) == 0:
                self.songs = self.list_of_songs
        if self.shuffle:
            if len(self.songs) == 0:
                return 'All songs are'
            try:
                curr_song = random.choice(self.songs)
            except IndexError:
                return ('All songs are played')
            self.songs.remove(curr_song)
            self.played.append(curr_song)
            return curr_song
        else:
            try:
                curr_song = self.songs[0]
                self.songs.remove(curr_song)
                self.played.append(curr_song)
            except IndexError:
                return ('All songs are played')
            return curr_song

    def pprint_playlist(self):
        x = PrettyTable()
        x.field_names = ['title', 'artist', 'album', 'length']
        for song in self.list_of_songs:
            x.add_row([song.title, song.artist, song.album, song.length_])

        return x

    def save(self):
        my_dict_ = dict()
        key = self.name
        my_dict_[key] = []
        for i in self.list_of_songs:
            my_dict_[key].append(i.__dict__)
        result = json.dumps(my_dict_)
        return result






s = Song("Odin", "Manowar", "The Sons of Odin", "10:44")
s1 = Song("Odin", "Manowar", "The Sons of Odin", "8:44")
s3 = Song("TotoV", "Toto", "Lea", "0:5:44")
s4 = Song("87", "Whitesnake", "Is this love", "0:7:44")
print(s.artist)

a = s.length(minutes=True)
my_list = Playlist('Boby Playlist', shuffle=True, repeat=True)
#print(my_list)
my_list.add_song(s)
my_list.add_song(s1)
my_list.add_song(s3)
my_list.add_song(s4)
print(my_list.pprint_playlist())


#print(my_list.total_length())
#print(my_list.artists())
#print(my_list.next_song())
#print(my_list.next_song())
#print(my_list.next_song())
#print(my_list.next_song())
#print(my_list.next_song())
#print(my_list.next_song())
#print(my_list.next_song())

print(my_list.save())

