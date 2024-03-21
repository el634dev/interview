const reverseList = function(head) {
    // Base case
    if (head == null || head.next == null) return head;
    // Create a new node to call the function recursively and we get the reverse linked list
    let res = reverseList(head.next);
    // Set head node as head.next.next
    head.next.next = head;
    //set head's next to be null
    head.next = null;
    // Return the reverse linked list
    return res;
};