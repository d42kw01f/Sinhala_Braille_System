
class theSperetor():
    def __init__(self, theString) -> None:
        self.theArray = [b'\xe0\xb6\xad\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xba', b'\xe0\xb6\x9a\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb', b'\xe0\xb6\xb8\xe0\xb7\x8a', b'\xe0\xb6\xb8\xe0\xb7\x8f', b'\xe0\xb6\xb8', b'\xe0\xb6\xba', b'\xe0\xb6\x85',b'\xe0\xb7\x80',b'\xe0\xb6\x85']
        self.theString = theString
        self.stringByte = bytes(self.theString, "utf-8")
        self.returnArray = []
    
    def sperator(self):
        StringLength = len(self.stringByte)
        i = 0

        while StringLength != 0:
            compareByte = self.stringByte[:StringLength]
            for theBytes in self.theArray:
                i += 1
                if compareByte == theBytes:
                    self.returnArray.append(theBytes.decode())
                    self.stringByte = self.stringByte[StringLength:]
                    StringLength = len(self.stringByte) + 1
                    break
            StringLength -= 1
        
        return self.returnArray

def main():
    string = 'යක්‍රම'
    splitter = theSperetor(string)
    theArray = splitter.sperator()
    print(theArray)


main()

