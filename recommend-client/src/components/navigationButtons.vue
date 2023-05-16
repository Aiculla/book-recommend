<template>
    <div>
      <button @click="goBackward">Backward</button>
      <button @click="goForward">Forward</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "NavigationButtons",
    data() {
      return {
        currentIndex: 0, // Assuming you have a use-case like a carousel or multi-step form, etc.
      };
    },
    methods: {
      goBackward() {
        this.$emit('indexChanged', -1);
      },
      goForward() {
        this.$emit('indexChanged', 1);
        
      },
    },
  };
  </script>
  