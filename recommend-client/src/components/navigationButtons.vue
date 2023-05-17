<template>
    <div class="button-container">
      <button class="nav-button" @click="goBackward">Backward</button>
      <button class="nav-button" @click="goForward">Forward</button>
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
  
  <style scoped>
.button-container {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.nav-button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.nav-button:hover {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50;
}
</style>







