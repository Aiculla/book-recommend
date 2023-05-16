<template>
  <div>
    <template v-if="currentBookSet && currentBookSet.books">
      <div class="book-list">
      <BookCard
        :books="currentBookSet.books.Message"
        :currentBookSet="currentBookSet"
        @book-clicked="handleBookClick"
        class="book-card"
      />
    </div>
    </template>
  </div>
</template>


<script>
import BookCard from './components/BookCard.vue';
import {DoublyLinkedList} from './doublyLinkedCircularList'
import { coldStart, nextThree} from './api';

// Call init and then do coldStart, 
export default {
  components: {
    BookCard,
  },
  data() {
    return {
      linkedList: new DoublyLinkedList(),
      clickedBookISBN: '',
      currentBookSet: '',
    };
  },
  methods: {
    handleBookClick(isbn) {
      // Send a request to nextThree, add it to the linked list, and set currentBookSet to the next node, change values for currentBookSet and selectedBook
      nextThree({isbn: isbn}).then((response => {
        console.log(response)
        this.currentBookSet.currBookSet = false
        this.currentBookSet.selectedBook = isbn
        this.linkedList.insert(response,true,0)
        this.currentBookSet = this.currentBookSet.next
        console.log(this.currentBookSet)
      }))
    },
    loadData()  {
  //     initial().then((result) => {
  //     console.log(result)
  //     coldStart().then((response) => {
  //       console.log(response)
  //       this.linkedList.insert(response,true,0)
  //       this.currentBookSet = this.linkedList.head
  //     })
  // })
  coldStart().then((response) => {
        console.log(response)
        this.linkedList.insert(response,true,0)
        this.currentBookSet = this.linkedList.head
      })
    }
  },
  mounted() {
    this.loadData()
  }
};





// What I'm looking at 
// Isloading reactive varaible for showing the loading screen and the other components
// Component for the forward and backward buttons
//Forward and Backward buttons changes the node being sent to the card component
// Selected card gets highlighted and is no longer able to 

</script>
