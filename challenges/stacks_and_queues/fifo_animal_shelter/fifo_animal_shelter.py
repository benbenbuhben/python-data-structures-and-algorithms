class Animal(object):
    def __init__(self, type=None, _next=None):
        self.type = type
        self._next = _next


class AnimalShelter(object):
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0

    def enqueue(self, type):
        newAnimal = Animal(type)
        if not self.front:
            self.front = newAnimal
        else:
            curr_animal = self.front
            while curr_animal._next:
                curr_animal = curr_animal._next
            curr_animal._next = newAnimal
            self.back = curr_animal
        self._length += 1

    def dequeue(self, pref=None):
        if not pref or pref == self.front.type:
            old_front = self.front
            self.front = old_front._next
            self._length -= 1
            return old_front.type

        elif pref == 'cat' or pref == 'dog':
            curr_animal = self.front
            while curr_animal._next.type != pref:
                curr_animal = curr_animal._next
            output = curr_animal._next.type
            curr_animal._next = curr_animal._next._next
            self._length -= 1
            return output

