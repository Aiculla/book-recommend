<template>
  <div class="loading-screen">
    <p class="loading-text">Loading <span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></p>
    
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



.loading-text {
font-size: 24px;
color: #000;
margin-bottom: 20px;

}

.dot {
animation: blink 1s linear infinite;
}

@keyframes bounce {
0%, 100% { transform: scale(0.0); }
50% { transform: scale(1.0); }
}

@keyframes blink {
0% { opacity: .2; }
20% { opacity: 1; }
100% { opacity: .2; }
}
</style>
