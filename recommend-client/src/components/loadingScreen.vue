<template>
    <div class="loading-screen">
      <p class="loading-text">Loading...</p>
      <div class="spinner">
        <div class="double-bounce1"></div>
        <div class="double-bounce2"></div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoadingScreen',
  }
  </script>
  
  <style scoped lang="scss">
  .loading-screen {
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    flex-direction: column;
  }
  
  .spinner {
    width: 40px;
    height: 40px;
    position: relative;
    margin: 10px auto;
  }
  
  .double-bounce1, .double-bounce2 {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #000;
    opacity: 0.6;
    position: absolute;
    top: 0;
    left: 0;
    
    animation: bounce 2.0s infinite ease-in-out;
  }
  
  .double-bounce2 {
    animation-delay: -1.0s;
  }
  
  .loading-text {
    font-size: 20px;
    color: #000;
    margin-bottom: 20px;
  }
  
  @keyframes bounce {
    0%, 100% { transform: scale(0.0); }
    50% { transform: scale(1.0); }
  }
  </style>
  