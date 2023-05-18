<template>
  <div>
    <template v-if="isloading">
      <LoadingScreen />
    </template>
    <template v-else>
      <FlashMessage :success="success" :message="flashMessage" />
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
import FlashMessage from './components/FlashMessage.vue';
import {DoublyLinkedList} from './doublyLinkedCircularList'
import { coldStart, nextThree,initial} from './api';

// Call init and then do coldStart, 
export default {
  components: {
    BookCard,
    LoadingScreen,
    NavigationButtons,
    FlashMessage
  },
  data() {
    return {
      linkedList: new DoublyLinkedList(),
      clickedBookISBN: '',
      currentBookSet: '',
      isloading: true,
      flashMessage: '',
      success: false,
      timer: null
    };
  },
  methods: {
    setFlashMessage(message, success) {
      clearTimeout(this.timer); // Clear the existing timer if any

      this.flashMessage = message;
      this.success = success;

      // Set a new timer to clear the message after 5 seconds
      this.timer = setTimeout(() => {
        this.flashMessage = '';
      }, 5000);
    },
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
        let msg = 'Book successfully loaded'
        let succ = true
        if(!response.Success) {
          msg = 'Error when loading books'
          succ = false
        }
        this.setFlashMessage(msg, succ);
        return
      })).catch(() => {
    // Set flash message
    this.setFlashMessage('Error while loading books',false);
  })
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
         let msg = 'Data successfully loaded'
        let succ = true
          if(!response.Success) {
          msg = 'Error when loading data'
          succ = false
        }
        this.setFlashMessage(msg, succ);
      


    }).catch(() => {
      // Set flash message
      this.setFlashMessage('Error while loading data',false);
    })
  }).catch(() => {
    // Set flash message
    this.setFlashMessage('Error while initializing',false);
  })
},
  },
  beforeUnmount() {
    clearTimeout(this.timer); // Clear the timer when the component is unmounted
  },
  mounted() {
    this.loadData()
  }
};
</script>
