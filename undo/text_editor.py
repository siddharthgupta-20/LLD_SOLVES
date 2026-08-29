from history import History
from momento import TextMomento
class TextEditor:
    def __init__(self):
        self.__text = ""

    def write(self, text: str):
        self.__text += text

    def get_text(self) -> str:
        return self.__text
    
    def save(self)  -> TextMomento :
        return TextMomento(self.__text)
    
    def undo(self,history):
        history.remove()

    def restore(self,tm: TextMomento):
        self.__text = tm.show_snapshot()