
##### Lets start with the most simple and work our way up from there #####

# ListArray #

This is a simple array element that is dynamic, mutable, resizable, and can be accessed randomly. all of this means you can map values and pull them from their direct index with a simple request. 

An array is initialized by `let myList = [];`. Here are some common use case functions for arrays.

```
push(): Adds one or more elements to the end of the array.
pop(): Removes the last element from the array and returns it.
shift(): Removes the first element from the array and returns it.
unshift(): Adds one or more elements to the beginning of the array.
splice(): Changes the contents of an array by removing or replacing existing elements and/or adding new elements.
slice(): Returns a shallow copy of a portion of an array into a new array object.
indexOf(): Returns the first index at which a given element can be found in the array.
includes(): Determines whether an array includes a certain value among its entries.
forEach(), map(), filter(), reduce(): Higher-order functions for iterating and transforming array elements.

```
###### 

# Singly Linked List # 

A singly linked list is a data structure that stores values efficiently in memory. This means that making requests to get information from that list is significantly faster in runtime. The Key characteristics in a Singly Linked List are its:

    - Nodes: Each node stores a value and the property for the next node in a list. If there is no value for the head node, you initialize it as null.
    - Head: This refers to the property of the list that is at the very beginning. Just as in the last bullet point. when initializing, if the value is blank; null.
    - Tail: Tail usually refers to the last node in the list. The tail of the list always has the next node set to null. 
    - One Way Traversal: The nodes only travel with the property '.next', so they can only go one way from the head. These lists aren't immutable, thus allowing you to append new values to them.

Heres how we construct a list from its first node. We define the node, initialize its value as the input value, set the next node to null. When we construct our list, we reinitialize the constructor and create a head and tail, and initial length. 

#####

```javascript

    class Node {
      constructor(value) {
        this.value = value;
        this.next = null;
      }
    }
    
    class SinglyLinkedList {
      constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
      }
    }

    push(value) {
        let newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }

    pop() {
        if (!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        while (current.next) {
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return current;
    }

    shift() {
        if (!this.head) return undefined;
        let oldHead = this.head;
        this.head = oldHead.next;
        this.length--;
        if (this.length === 0) {
            this.tail = null;
        }
        return oldHead;
    }

    unshift(value) {
        let newNode = new Node(value);
            if (!this.head) {
                this.head = newNode;
                this.tail = newNode;
            } else {
                newNode.next = this.head;
                this.head = newNode;
            }
            this.length++;
            return this;
        }

    get(index) {
        if (index < 0 || index >= this.length) return null;
        let counter = 0;
        let current = this.head;
        while (counter !== index) {
            current = current.next;
            counter++;
        }
        return current;
    }

    set(index, value) {
        let foundNode = this.get(index);
        if (foundNode) {
            foundNode.value = value;
            return true;
        }
        return false;
    }

    insert(index, value) {
        if (index < 0 || index > this.length) return false;
        if (index === this.length) return !!this.push(value);
        if (index === 0) return !!this.unshift(value);

        let newNode = new Node(value);
        let prev = this.get(index - 1);
        let temp = prev.next;
        prev.next = newNode;
        newNode.next = temp;
        this.length++;
        return true;
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        if (index === 0) return this.shift();
        if (index === this.length - 1) return this.pop();

        let previousNode = this.get(index - 1);
        let removed = previousNode.next;
        previousNode.next = removed.next;
        this.length--;
        return removed;
    }

    reverse() {
        let node = this.head;
        this.head = this.tail;
        this.tail = node;
        let next;
        let prev = null;
        for (let i = 0; i < this.length; i++) {
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return this;
    }
```
#####

# Doubly Linked List # 

A doubly linked list is a similar data structure to the singly linked list, except it comes with two direct pointers between nodes, making it more efficient than the singly linked list which can only transverse in one direction. The doubly linked list contains three data fields; the data itself, the next node, the previous node. 

#####

```javascript

class Node {
    constructor(data){

        this.data = data;
        this.prev = null;
        this.next = null;
    }
}
```
#####

# Circular Linked List #

A circular linked list works in a similar way the doubly linked list works, but instead of ending at the tail node, the tail node points directly abck to the head node. This way, theres always a reference to the data inside of the list. A circular linked list has many applications, including looping data, making presentations, switching between applications, memory management, etc. 

We use the same exact constructor, except when were referencing the end of the list, we just point directly back to the head. 

#####

```javascript

class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }
}
```
#####

# Stack (arrays) #

A stack is a linear data structure that follows the Last-in-First-out Principle `(LIFO)`. It can be implemented and treated as an array, except your operations happen at the bottom of the stack, hence the Last In First Out property. 

```javascript
class myStack {

    constructor(cap) {
        
        this.arr = new Array(cap);
        this.capacity = cap;
        this.top = -1;
    }

    push(x) {
    if (this.top === this.capacity - 1) {
        console.log("Stack Overflow");
        return;
    }
    this.arr[++this.top] = x;
    }

    pop() {
        if (this.top === -1) {
            console.log("Stack Underflow");
            return -1;
        }
        return this.arr[this.top--];
    }

    peek() {
        if (this.top === -1) {
            console.log("Stack is Empty");
            return -1;
        }
        return this.arr[this.top];
    }

    isEmpty() {
        return this.top === -1;
    }

    isFull() {
        return this.top === this.capacity - 1;
    }

}
```
#####

# Stack (Linked-list) #

Similar to the array stack, this stack is Last-In-First-Out ordered. `(LIFO)`. Differently, this form of linear data structure has no size implementation, and therefore is dynamically flexible until physical memory runs out. A stack with a linked list can be implemented by initializing a Node with a constructor for its data. Then, you can create the stack class with an empty initial constructor, where you can later on implement new Nodes.

#####

```javascript
class Node {
    constructor(x) {
        this.data = x;
        this.next = null;
    }
}

class myStack {
    constructor() {
        this.top = null;
        this.count = 0;
    }

    push(x) {
        let temp = new Node(x);
        temp.next = this.top;
        this.top = temp;
        this.count++;
    }

    pop() {
        if (this.top === null) {
            console.log("Stack Underflow");
            return -1;
        }
        let temp = this.top;
        this.top = this.top.next;
        let val = temp.data;
        this.count--;
        return val;
    }

    peek() {
        if (this.top === null) {
            console.log("Stack is Empty");
            return -1;
        }
        return this.top.data;
    }

    isEmpty() {
        return this.top === null;
    }

    size() {
        return this.count;
    }
}
```
#####

# Queue (Array) #

A queue is a data structure that follows the First-In-First-Out principle in computer science `(FIFO)`. We're initializing a class with a constructor that has a capacity, as all arrays need a capacity. 

```javascript
class myQueue {
    constructor(capacity) {
        this.capacity = capacity;
        this.arr = new Array(capacity);
        this.size = 0;
    }

    isEmpty() {
        return this.size === 0;
    }

    isFull() {
        return this.size === this.capacity;
    }

    enqueue(x) {
        if (this.isFull()) {
            console.log("Queue is full!");
            return;
        }
        this.arr[this.size] = x;
        this.size++;
    }

    dequeue() {
        if (this.isEmpty()) {
            console.log("Queue is empty!");
            return;
        }
        for (let i = 1; i < this.size; i++) {
            this.arr[i - 1] = this.arr[i];
        }
        this.size--;
    }

    getFront() {
        if (this.isEmpty()) {
            console.log("Queue is empty!");
            return -1;
        }
        return this.arr[0];
    }
    
    getRear() {
        if (this.isEmpty()) {
            console.log("Queue is empty!");
            return -1;
        }
        return this.arr[this.size - 1];
    }
}
```

#####

# Queue (Linked-List) #

A queue as a Linked-List functions similarly to a stack as a linked list, except they follow very different properties. These queues are dynamic, meaning they can be infinitely changed until memory runs out. They are mutable, and follow the First-In-First-Out Principle `(FIFO)`.

```javascript

class Node() {
    constructor(newData) {
        this.data = newData;
        this.next = null;
    }
}

class Queue() {
    constructor() {
        this.front = this.rear = null;
        currSize = 0;
    }

    isEmpty() {
        return this.front === null;
    }

    enqueue(newData) {
        const newNode = new Node(newData);
        if (this.isEmpty()) {
            this.front = this.rear = newNode;
        } else {
            this.rear.next = newNode;
            this.rear = newNode;
        }
        this.currSize++;
    }

    dequeue() {
        if (this.isEmpty()) {
            console.log("Queue Underflow");
            return -1;
        } else {
            const removedData = this.front.data;
            this.front = this.front.next;
            if (this.front === null) {
                this.rear === null;
            }
            this.currSize--;
            return removedData;
        }
    }

    getFront() {
        if (this.isEmpty()) {
            console.log("Empty.")
            return -1;
        }
        return this.front.data;
    }

    size() {
        return this.currSize;
    }

}

```

#####

# Deque (Array) #

A deque is a data structure that allows you to make insertions and deletions from both the front and the back of the queue array object. The data structure starts with two pointers to the front and the rear, where we can make shift, unshift, push, and pop operations. This data structure is mutable, resizable, and runtime efficient (most operations are O(1) runtime except insert and delete O(N)).

```javascript

class Deque() {
    constructor() {
        this.dq = [];
    }
    isEmpty() {
        return this.dq.length === 0;
    }

    insertFront(x) {
        this.dq.unshift(x);
    }

    insertRear(x) {
        this.dq.push(x);
    }

    deleteFront() {
        if (!this.isEmpty()) {
            this.dq.shift();
        }
    }

    deleteRear() {
        if (!this.isEmpty()) {
            this.dq.pop();
        }
    }

    getFront() {
        return this.isEmpty() ? -1 : this.dq[0];
    }

    getRear() {
        return this.isEmpty() ? -1 : this.dq[this.dq.length - 1];
    }

    display() { 
        console.log(this.dq.join(' '));
    }
}


```

#####

# Deque (Linked-List) #

A deque as a linked list is a more efficient version of a deque in an array, as insertions and deletions are runtime O(1) instead of O(n), where only erasing the entire data strucutre is O(n) because it loops through every value once. This data structure is mutable, scalable, and utilizes nodes to store values. 

```javascript

class Node() {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class Deque() {
    constructor() {
        this.front = this.rear = null;
        this.size = 0;
    }

    isEmpty() {
        return this.front === null;
    }

    getSize() {
        return this.size;
    }

    insertFront(data) {
        newNode = new Node(data);
        if (this.isEmpty()) {
            this.front = this.rear = newNode;
        } else {
            newNode.next = this.front;
            this.front.prev = newNode;
            this.front = newNode;
        }
        this.size++;
    }

    insertRear() {
        newNode = new Node(data);
        if (this.isEmpty()) {
            this.rear = this.front = newNode;
        } else {
            newNode.prev = this.rear;
            this.rear.next = newNode;
            this.rear = newNode;
        }
        this.size--;
    }

    deleteFront() {
        if (this.isEmpty()) {
            console.log("Deque Underflow")
            return -1;
        } else {
            this.front = this.front.next;
            if (this.front) this.front.prev = null;
            else this.rear = null;            
            this.size--;
        }
    }
}

```

##### Kadane's Algorithm #####

Kadane's algorithm returns the maximum sum of a contiguous subarray. This means an `array nested within an array`. This algorithm is taking a subset of integer
values within the array, testing them against each other to find the subarray with the maximum sum instide of it.

In this example, were passing in a parameter nums thats the parent array. We define two arrays. The Max found so far, and the current maximum from add operations.
We're going to start at the beginning of the array, looping through every element in the array with a for loop. It's going to take i element from the array, add it to the CurrentMax, and append it as the value for MaxThusFar if its greater than the current MaxThusFar. The function then returns the highest value found within the array.

An example use case of this algorithm is to find the maximum sum of a contiguous subarray within an array.

######

```javascript
var maxSubArray = function(nums) {
    let MaxThusFar = nums[0];
    let CurrentMax = nums[0];
    for (let i = 1; i < nums.length; i++) {
        CurrentMax = Math.max(nums[i], CurrentMax + nums[i]);
        MaxThusFar = Math.max(MaxThusFar, CurrentMax);
    }

    return MaxThusFar;
};
```
######

