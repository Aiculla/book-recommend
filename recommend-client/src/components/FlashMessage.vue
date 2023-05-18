<template>
    <div :class="messageClass" v-if="message">
      {{ message }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      success: {
        type: Boolean,
        required: true,
      },
      message: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        timer: null,
      };
    },
    computed: {
      messageClass() {
        return {
          'message-success': this.success,
          'message-error': !this.success,
        };
      },
    },
    methods: {
      hideMessage() {
        this.$emit('update:message', '');
      },
    },
    mounted() {
      this.timer = setTimeout(this.hideMessage, 5000);
    },
    beforeUnmount() {
      clearTimeout(this.timer);
    },
  };
  </script>
  
  <style scoped>
  .message-success, .message-error {
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
    font-size: 1.2em;
    font-weight: bold;
    text-align: center;
    transition: all 0.5s ease;
  }
  
  .message-success {
    background-color: #dff0d8;
    color: #3c763d;
    border: 1px solid #d6e9c6;
  }
  
  .message-error {
    background-color: #f2dede;
    color: #a94442;
    border: 1px solid #ebccd1;
  }
  
  .message-success::before {
    content: '✔';
    margin-right: 5px;
  }
  
  .message-error::before {
    content: '✖';
    margin-right: 5px;
  }
  </style>