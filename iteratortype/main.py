from playlist import Playlist
from song import Song
playlist = Playlist()
playlist.add_song(Song("song1"))
playlist.add_song(Song("song2"))
playlist.add_song(Song("song3"))
playlist.add_song(Song("song4"))

iterator = playlist.createIterator()

while iterator.has_next():
    print(iterator.next().get_title())