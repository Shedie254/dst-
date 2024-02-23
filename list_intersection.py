class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_intersection_node_optimized(headA, headB):
    """
    Finds the first node where two singly linked lists intersect, considering
    the additional information that the intersection happens after the end of
    the shorter list's original part.

    Args:
        headA: The head of the first linked list.
        headB: The head of the second linked list.

    Returns:
        The node where the linked lists intersect, or None if they don't.
    """

    # Handle edge cases: both lists are empty or either head is None
    if headA is None or headB is None:
        return None

    # Calculate lengths of both lists' original parts
    lenA, lenB = 0, 0
    currA, currB = headA, headB
    while currA and currA.next is not currB:
        lenA += 1
        currA = currA.next
    while currB and currB.next is not currA:
        lenB += 1
        currB = currB.next

    # Advance the longer list's pointer to meet the shorter list at c1
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            currB = currB.next

    # Traverse both lists simultaneously, checking for intersection
    while currA and currB:
        if currA is currB:
            return currA  # Intersection found
        currA = currA.next
        currB = currB.next

    # Check if either pointer reached the end of its original part
    if currA is None or currB is None:
        return None  # No intersection found

    # Since both pointers are now in the shared part, they'll meet eventually
    while True:
        if currA is currB:
            return currA  # Intersection found
        currA = currA.next
        currB = currB.next

def create_list(data):
    """
    Creates a singly linked list from a given list of data.

    Args:
        data: A list of data values to represent the linked list nodes.

    Returns:
        The head node of the created linked list.
    """

    head = None
    prev = None
    for item in data:
        node = Node(item)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head

def main():
    # Create lists according to the provided structure
    listA_data = ["a1", "a2", "c1", "c2", "c3"]
    listB_data = ["b1", "b2", "b3", "c1", "c2", "c3"]

    headA = create_list(listA_data)
    headB = create_list(listB_data)

    # Find and print the intersection node
    intersection_node = get_intersection_node_optimized(headA, headB)
    if intersection_node:
        print("Intersection node:", intersection_node.data)
    else:
        print("No intersection found")

if __name__ == "__main__":
    main()
