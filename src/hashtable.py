# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def insertList(node, key, value):
    if node.key == key:
        node.value = value
    elif node.next is not None:
        insertList(node.next,key, value)
    else:
        node.next = LinkedPair(key, value)

def deleteList(prev_node, current_node, key):
    if current_node.key == key:
        prev_node.next = current_node.next
        return True
    elif current_node.next is not None:
        deleteList(current_node, current_node.next, key)
    else:
        return False

def retrieveList(node, key):
    if node.key == key:
        return node.value
    elif node.next is not None:
        return retrieveList(node.next, key)
    else:
        return None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:
            insertList(self.storage[index], key, value)
        else:
            self.storage[index] = LinkedPair(key,value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:
            if self.storage[index].key != key and self.storage[index].next != None:
                deleted = deleteList(self.storage[index], self.storage[index].next, key)
                if deleted == False:
                    print("Key is not found")
            else:        
                self.storage[index] = None
        else:
            print("Key is not found")
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:
            return retrieveList(self.storage[index], key)
        else:
            return None
        
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        for i in old_storage:
            if i is not None:
                node = i
                while node is not None:
                    self.insert(node.key, node.value)
                    node = node.next




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
