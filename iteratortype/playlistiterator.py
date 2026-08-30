from iterator import Iterator 
from song import Song
from typing import List
class PlaylistIterator(Iterator):
    def __init__(self, playlist: List[Song]):
        self.playlist= playlist
        self.position = 0
    def has_next(self):
        if self.position >= len(self.playlist):
            return False
        return True

    def next(self) -> Song | None:
        while self.has_next() == True:
            song = self.playlist[self.position]
            self.position +=1
            return song
        return None