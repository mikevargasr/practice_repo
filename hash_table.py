class HashTable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.arr = [None for i in range(self.MAX_SIZE)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.MAX_SIZE
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

t = HashTable()
t['Mike'] = 5
t['Peter'] = 6

print(t.arr)