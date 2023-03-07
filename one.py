class Test:
    def __init__(self, text):
        self.text = text 

    def getList(self):
        return list(self.text)
    
    def __str__(self):
        return f'{self.getList()}'

atest = Test('edgar muyomba')
print(atest)