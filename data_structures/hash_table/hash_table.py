class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192, allow_collisions=True):
        self.size = size
        self.hashtable = [None] * self.size
        self.allow_collisions = allow_collisions

    def __len__(self):
        return self.entries_count

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.size

    def _set(self, key, value=1):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        # This probably needs to be updated so that key/value pairs are stored in an array or linked list. Or if you wanna be a badass, have the data structure as a variable input.
        try:
            if type(key) == 'int':
                key = str(key)
            index = self._hash_key(key)
            key_value = [key, value]
            if self.hashtable[index] is None:
                self.hashtable[index] = [key_value]
                self.entries_count += 1
            else:
                for el in self.hashtable[index]:
                    if el[0] == key:
                        if self.allow_collisions:
                            el[1] = value
                            return 'Updated Value'
                        else:
                            return 'Collision Not Allowed'
                self.hashtable[index].append([key_value])
        except TypeError:
            return 'Set method only accepts strings as keys'

    def _get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        try:
            index = self._hash_key(key)
            if self.hashtable[index] is not None:
                for el in self.hashtable[index]:
                    if el[0] == key:
                        return el[1]
            else:
                return None
        except TypeError:
            return 'Get method only accepts strings as keys'

    def _remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        try:
            index = self._hash_key(key)
            if self.hashtable[index] is not None:
                for i, el in enumerate(self.hashtable[index]):
                    if el[0] == key:
                        value = el[1]
                        self.hashtable[index].pop(i)
                        self.entries_count -= 1
                        return value
                return None
        except TypeError:
            return 'Remove method only accepts strings as keys'
