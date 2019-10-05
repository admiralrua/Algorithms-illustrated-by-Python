def middle_Node(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        return slow


def has_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
        return False


def first_Node_of_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
         
    slow = head
    while fast and slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def last_Node_of_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
         
    slow = head
    while fast and slow.next != fast.next:
        slow = slow.next
        fast = fast.next
      
    # fast.ext = None     # use this to remove the cycle >_<
    return fast
