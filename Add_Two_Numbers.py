# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list2num(input_list):
    total = 0
    for num in range(100):
        total += input_list.val * 10 ** num
        input_list = input_list.next
        if input_list == None:
            return total

def listnode_next(current_node):
    next_listnode = ListNode()
    current_node.next = next_listnode
    return current_node.next

def num2list(input_num):
    output_listnode = ListNode()
    head = output_listnode
    for num in range(100):
        output_listnode.val = (input_num % 10)
        input_num = input_num // 10
        if input_num < 1:
            return head
        output_listnode = listnode_next(output_listnode)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return num2list(list2num(l1) + list2num(l2))
