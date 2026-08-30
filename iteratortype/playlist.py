from song import Song
from typing import List
from playlistiterator import PlaylistIterator
class Playlist:
    def __init__(self):
        self.__playlist:List = []

    def add_song(self,song: Song):
        self.__playlist.append(song)

    def createIterator(self) -> PlaylistIterator:
        return PlaylistIterator(self.__playlist)