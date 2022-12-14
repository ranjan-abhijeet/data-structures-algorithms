class InvalidIndexException(Exception):
    """ Raised when queried index is not in linked list"""
    pass

class Node():
    def  __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            while itr:
                if itr.next is None:
                    itr.next = node
                    break
                itr = itr.next

    def print(self):
        arrow = '-->'
        if self.head is None:
            print(arrow)
            print('Empty linked list')
        else:
            ll_str = ''
            itr = self.head
            while itr:
                ll_str += str(itr.data) + str(arrow)
                itr = itr.next
            print(ll_str)

    def delete_head(self):
        if self.head is None:
            print('Empty linked list')
        else:
            new_head = self.head.next
            self.head = new_head

    def delete_end(self):
        if self.head is None:
            print('Empty linked list')
        else:
            itr = self.head
            while itr:
                if itr.next.next is None:
                    break
                itr = itr.next
            itr.next = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        linked_list = LinkedList()
        for data in data_list:
            linked_list.insert_at_end(data)
        return linked_list

    def insert_at_index(self, data, index: int):
        if index < 0 or index > self.get_length():
            raise InvalidIndexException("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while True:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next
    
    
    def delete_at_index(self, index: int):
        if index < 0 or index > self.get_length():
            raise InvalidIndexException("Invalid index")
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        previous_node = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next 

    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            
            if itr.data == data_after:
                self.insert_at_index(data_to_insert, count+1)
                break
            count += 1
            itr = itr.next
    
    def delete_by_value(self, data):
        count = 0
        itr = self.head
        while True:
            if data == itr.data:
                self.delete_at_index(count)
                break
            count += 1
            itr = itr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(8)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_end(13)
    llist.delete_head()
    llist.insert_at_end(24)
    llist.insert_at_end(123)
    llist.delete_end()
    llist.print()
    new_list = llist.insert_values([43, 12, 6, 93, 0, 4, 5, 6])
    new_list.print()
    new_list.delete_at_index(3)
    new_list.print()
    new_list.delete_at_index(4)
    new_list.print()
    new_list.delete_at_index(2)
    new_list.print()
    new_list.insert_at_index(data="banana", index=5)
    new_list.print()
    new_list.insert_after_value(22, "apple")
    new_list.print()
    new_list.delete_by_value(0)
    new_list.print()