let id = 0;
let prevNodeTail = 0;
// Insertion
// Add(value)
//   Pre: value is the value to add to the list
//   Post: value has been placed at the tail of the list
//   n ← node(value)
//   if head = ø
//     head ← n
//     tail ← n
//   else
//     tail.next ← n
//     tail ← n
//   end if
// end Add
function generateId() {
    return id++
}


function Node(head) {
    this.id = 0;
    this.head = head;
    this.tail = 0;
}


function LinkedListInsertion(node, prevNode, insertValue) {
    if (node.tail >= 1) {
        node.head = insertValue;
        node.id = prevNodeTail;
        prevNodeTail = prevNodeTail + 1;
        node.tail = prevNodeTail;
    } else {
        node.id = generateId();
        node.head = insertValue;
        node.tail = generateId();
        prevNodeTail = node.tail;
    }
    return node;
}

const nodeFirst = new Node();
const nodeSecond = new Node();
const nodeThird = new Node();
const nodeFourth = new Node();

let first = LinkedListInsertion(nodeFirst, null, 12);
let second = LinkedListInsertion(nodeSecond, nodeFirst, 15);
let third = LinkedListInsertion(nodeThird, nodeSecond, 19);
let fourth = LinkedListInsertion(nodeFourth, nodeThird, 25);
console.log('first object', first);
console.log('second object', second);
console.log('third object', third);
console.log('fourth object', fourth);

