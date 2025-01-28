<template>
    <div>
      <h2>My Component</h2>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MyComponent',
    data() {
      return {
        message: 'Hello from MyComponent!',
      };
    },
    created() {
      // 這裡可以進行 API 請求或其他初始化操作
      fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => {
          this.message = data.message;
        });
    },
  };
  </script>
  
  <style scoped>
  h2 {
    color: blue;
  }
  </style>