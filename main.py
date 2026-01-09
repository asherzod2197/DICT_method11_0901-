# FROMKEYS
class MyDict:
    @classmethod
    def fromkeys(cls, keys, value=None):
        yangi = {}
        for key in keys:
            yangi[key] = value
        return yangi

keys = ["a", "b", "c"]

d = MyDict.fromkeys(keys, 0)
print(d)
