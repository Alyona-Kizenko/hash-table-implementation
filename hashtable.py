class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  
    
    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1
        if self.count / self.size > 0.7:
            self._resize()
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False
    
    def _resize(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        old_table = self.table
        self.size = new_size
        self.table = new_table
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    
    print(ht.get("banana"))
    print(ht.get("kiwi"))  

    ht_resize = HashTable(5)
    for i in range(10):
        ht_resize.insert(f"key{i}", f"value{i}")
    
    print("\nПосле добавления 10 элементов:")
    print(f"Размер таблицы: {ht_resize.size}")
    print(f"Количество элементов: {ht_resize.count}")
    
    for i in range(10):
        assert ht_resize.get(f"key{i}") == f"value{i}"
    print("Все тесты пройдены успешно!")

    def string_hash(input_string):
        return sum(ord(c) for c in input_string)
print(string_hash("hello")) 


class StringHashDictionary:
    def __init__(self):
        self.dictionary = {}
    
    def add(self, key, value):
        hash_value = string_hash(key)
        self.dictionary[key] = (value, hash_value)
    
    def get(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        return None
    
    def get_hash(self, key):
        if key in self.dictionary:
            return self.dictionary[key][1]
        return None

def test_string_dictionary():
    sh_dict = StringHashDictionary()
    sh_dict.add("apple", "A sweet fruit")
    sh_dict.add("banana", "A yellow fruit")
    sh_dict.add("cherry", "A small red fruit")
    print(sh_dict.get("apple"))  
    print(sh_dict.get_hash("banana")) 
    print(sh_dict.get("orange"))

test_string_dictionary()