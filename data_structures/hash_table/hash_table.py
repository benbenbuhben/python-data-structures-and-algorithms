class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.size = size
        self.hashtable = [None] * self.size

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

    def _set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        try:
            index = self._hash_key(key)
            self.hashtable[index] = value
            self.entries_count += 1
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
            return self.hashtable[index]
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
            value = self.hashtable[index]
            self.hashtable[index] = None
            self.entries_count -= 1
            return value
        except TypeError:
            return 'Remove method only accepts strings as keys'
