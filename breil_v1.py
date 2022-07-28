import json
import sys


class JsonData:
    def __init__(self, filename):
        try:
            with open(filename, mode="r") as jsonFile:
                self.data = json.load(jsonFile)
            
        except OSError as e:
            print(f'{filename} NOT FOUND!')
            exit()

class JsonDB(JsonData):
    def __init__(self, searchItem):
        self.filename = 'db.json'
        self.searchItem = searchItem
        super().__init__(self.filename)

    def findChar(self):
        return self.data[1][self.searchItem]

    def findBinary(self):
        return self.data[0][self.searchItem]

def programErrors(ErrorCode):
    if ErrorCode == 1:
        return f'usage: python3 {sys.argv[0]} -c ඈ \nOR\nusage: python3 {sys.argv[0]} -b 010100'

def main():
    if len(sys.argv) == 3:
        json_db = JsonDB(sys.argv[2])
        if sys.argv[1] == '-c':
            return json_db.findBinary()
        elif sys.argv[1] == '-b':
            return json_db.findChar()
        else:
            return programErrors(1)
    else:
        return programErrors(1)

if __name__ == '__main__':
    theOutput = main()
    print(theOutput)