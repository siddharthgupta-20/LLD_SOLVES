from typing import List
from momento import TextMomento
class History:
    def __init__(self):
        self.__history: List[TextMomento]=[]

    def add_history(self,txt:TextMomento):
        self.__history.append(txt)

    def show_history(self):
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].show_snapshot()}"); 

    def remove(self):
        if len(self.__history)<0:
            return TextMomento("")
        self.__history.pop()
        if len(self.__history)<0:
            return TextMomento("")
        return self.__history[-1]