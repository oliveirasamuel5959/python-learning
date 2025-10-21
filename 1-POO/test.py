class Test:
    def __init__(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
test = Test("Working")
print(test.get_status())