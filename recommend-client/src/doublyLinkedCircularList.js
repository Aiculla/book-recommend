class Node {
  constructor(books, currBookSet, selectedBook) {
    this.books = books;
    this.currBookSet = currBookSet;
    this.selectedBook = selectedBook;
    this.next = null;
    this.prev = null;
  }
}
  
export class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  insert(books, currBookSet, selectedBook) {
    const newNode = new Node(books, currBookSet, selectedBook);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
      newNode.next = newNode;
      newNode.prev = newNode;
    } else {
      newNode.next = this.head;
      newNode.prev = this.tail;
      this.head.prev = newNode;
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  display() {
    if (this.head === null) {
      console.log("The list is empty.");
      return;
    }

    let current = this.head;
    do {
      console.log("Books:", current.books);
      console.log("CurrBookSet:", current.currBookSet);
      console.log("SelectedBook:", current.selectedBook);
      console.log();

      current = current.next;
    } while (current !== this.head);
  }
}

