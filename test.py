class MyHashMap:

    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


hashMap = MyHashMap()

hashMap.put(1, 1)
hashMap.put(2, 2)

print(hashMap.get(1))
print(hashMap.get(3))

hashMap.put(2, 1)

print(hashMap.get(2))

hashMap.remove(2)

print(hashMap.get(2))