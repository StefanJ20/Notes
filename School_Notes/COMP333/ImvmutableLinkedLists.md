Mutable Linked List (MList): Can be changed overtime and through operations.

Mlist l = new MList(); // l : [] 

l.prepend(1); // l : [1] 
l.prepend(2); // l : [2,1]

Immutable Linked List (IList): Cannot be changed, but rather duplicates your list and adds your data to a new list.

IList l1 = NewIList(); // l1 : []

Ilist l2 = l1.prepend(1);
// l1: []
// l2: [1]

        Ilist:
       /     \
      /       \
    Nil.       cons: int head, IList tail

    nil = empty list
    cons objects equate to single element, non-empty list