<template>
  <div class="book-list">
    <template v-if="books && books.length">
      <div
        v-for="book in books"
        :key="book.ISBN"
        @click="handleBookCardClick(book.ISBN)"
        :class="{ 'clickable': currentBookSet.currBookSet }"
      >
        
        <div>
          <img :src="book['Image-URL-L']" alt="book cover" >
          <h2>{{ book['Book-Title'] }}</h2>
          <p>{{ book['Book-Author'] }}</p>
          <p>{{ book['Year-Of-Publication'] }}</p>
          <p>{{ book.Publisher }}</p>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'BookCard',
  props: {
    books: {
      type: Array,
      required: true,
    },
    currentBookSet: {
      type: Object,
      required: true,
    },
  },
  methods: {
    handleBookCardClick(isbn) {
      if (this.currentBookSet.currBookSet) {
        this.$emit('book-clicked', isbn);
      }
    },
  },
};
</script>

<style scoped>
.book-list {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background: #f4f4f4;
}

.book-list > div {
  flex: 1 0 30%;
  margin: 0 10px;
  background: #fff;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s ease;
  overflow: hidden;
  border-radius: 10px;
}

.book-list > div:hover {
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  cursor: pointer;
}

.book-list > div > div {
  padding: 20px;
}

.book-list > div > div img {
  max-height: 500px;
  width: auto;
  display: block;
  margin: auto;
  object-fit: contain;
}

.book-list > div > div h2 {
  font-size: 20px;
  margin: 10px 0;
}

.book-list > div > div p {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
}

.clickable {
  cursor: pointer;
}
</style>
