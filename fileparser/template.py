from abc import abstractmethod,ABC
class DataParser(ABC):
    def parse(self):
        self._open()
        self.dataparser()
        self._close()

    def _open(self):
        print("open the file")

    def _close(self) :
        print("close the file")

    @abstractmethod
    def dataparser(self):
        pass

