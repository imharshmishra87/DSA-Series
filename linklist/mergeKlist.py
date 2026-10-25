import heapq


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, head_node in enumerate(lists):
            if head_node is not None:
                heapq.heappush(heap, (head_node.val, i, head_node))

        new_node = ListNode(0)
        curr = new_node

        while heap:
            val, i, smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next

            if smallest_node.next is not None:
                heapq.heappush(heap, (smallest_node.next.val, i, smallest_node.next))
        return new_node.next


"""The algorithm mainly involves using a min-heap (priority queue) to efficiently merge k sorted linked lists. Here's a breakdown of the algorithm:"""
"""First we will import the heapq module, which provides an implementation of the min-heap data structure. 
We will define a ListNode class to represent each node in the linked lists. 
The ListNode class has two attributes: val (the value of the node) and next (a reference to the next node in the list). 
We will define a Solution class that contains the mergeKLists method. 
This method takes a list of linked lists as input and returns a single merged linked list. 
We will initialize an empty min-heap (heap) to store the nodes from the linked lists. 
We will iterate through each linked list in the input lists. 
For each non-empty linked list, we will push a tuple containing the value of the head node, its index in the input list, and the head node itself into the min-heap. 
We will create a new dummy node (new_node) to serve as the head of the merged linked list. 
We will also create a pointer (curr) that will be used to build the merged list. 
While there are still nodes in the min-heap, we will pop the smallest node from the heap (smallest_node) and add it to the merged list by updating curr.next to point to smallest_node. 
We will then move curr to point to smallest_node. If smallest_node has a next node, we will push that next node into the min-heap along with its value and index. Finally, we will return new_node.next, which points to the head of the merged linked list."""


"""Time complexity: O(N log k), where N is the total number of nodes across all linked lists and k is the number of linked lists.
Space complexity: O(k), where k is the number of linked lists. The min-heap can contain at most k nodes at any given time."""
