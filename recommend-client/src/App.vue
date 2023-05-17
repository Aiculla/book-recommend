<template>
  <div>
    <template v-if="isloading">
      <LoadingScreen />
    </template>
    <template v-else>
      <BookCard
        :books="currentBookSet.books.Message"
        :currentBookSet="currentBookSet"
        @book-clicked="handleBookClick"
        class="book-card"
      />
      <NavigationButtons @indexChanged ="changeLinkedListIndex"/>
    </template>
  </div>
</template>

<script>
import BookCard from './components/BookCard.vue';
import LoadingScreen from "./components/loadingScreen.vue"
import NavigationButtons from "./components/navigationButtons.vue"
import {DoublyLinkedList} from './doublyLinkedCircularList'
import { coldStart, nextThree,initial} from './api';

// Call init and then do coldStart, 
export default {
  components: {
    BookCard,
    LoadingScreen,
    NavigationButtons,
  },
  data() {
    return {
      linkedList: new DoublyLinkedList(),
      clickedBookISBN: '',
      currentBookSet: '',
      isloading: true,
      setNumber: 1,
    };
  },
  methods: {
    handleBookClick(isbn) {
      // Send a request to nextThree, add it to the linked list, and set currentBookSet to the next node, change values for currentBookSet and selectedBook
      nextThree({isbn: isbn}).then((response => {
        console.log(response)
        // Adding to the linked list 
        this.currentBookSet.currBookSet = false
        this.currentBookSet.selectedBook = isbn
        this.linkedList.insert(response,true,0)
        this.currentBookSet = this.currentBookSet.next
        this.setNumber = this.setNumber + 1
        return
      }))
    },
    changeLinkedListIndex(newIndex) {
      if(newIndex > 0)  {
        this.currentBookSet = this.currentBookSet.prev
      }
      else  {
        this.currentBookSet = this.currentBookSet.next
      }
    },
    loadData()  {
       initial().then((result) => {
       console.log(result)
       coldStart().then((response) => {
         console.log(response)
         this.linkedList.insert(response,true,0)
         this.currentBookSet = this.linkedList.head
         this.isloading = false
         
       })
   })
    },
  },
  mounted() {
    this.loadData()
  }
};





// What I'm looking at 

// Selected card gets highlighted
// Change the styling for buttons, loading screen, book cards, 
// Message Flashing 

</script>
