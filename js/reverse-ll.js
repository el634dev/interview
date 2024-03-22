// Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.

// -----------------
// EXAMPLES
// -----------------

// Example 1:
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]

// ----------------
// Example 2:
// Input: head = [1,2]
// Output: [2,1]

// ----------------
// Example 3:
// Input: head = []
// Output: []

// ----------------
// Constraints:
// The number of nodes in the list is the range [0, 5000].
// -5000 <= Node.val <= 5000

// ----------------
// Follow up: A linked list can be reversed either iteratively or recursively. 
// Could you implement both?

// -----------------
// SOLUTIONS
// -----------------

// Recursive Solution
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
