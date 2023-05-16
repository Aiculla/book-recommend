<template>
  <div class="book-list">
    <template v-if="books && books.length">
      <div
        v-for="book in books"
        :key="book.ISBN"
        class="book-card"
        @click="handleBookCardClick(book.ISBN)"
        :class="{ 'clickable': currentBookSet.currBookSet }"
      >
        <img :src="book['Image-URL-L']" alt="book cover" class="book-cover">
        <div class="book-details">
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
  flex-wrap: wrap;
  gap: 1rem;
}

.book-card {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 1rem;
  max-width: 300px;
}

.book-cover {
  width: 100%;
  height: auto;
}

.book-details {
  margin-top: 1rem;
}
</style>



