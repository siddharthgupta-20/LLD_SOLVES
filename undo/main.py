from history import History
from momento import TextMomento
from text_editor import TextEditor

history = History()
text_editor = TextEditor()

text_editor.write("hello")
text_editor.write(" world")
history.add_history(text_editor.save())
text_editor.write(" good")
text_editor.write(" bye")
history.add_history(text_editor.save())
history.show_history()
print("------------------")
print(history.remove().show_snapshot())
text_editor.get_text()