<template>
  <div>
    <h1>Home</h1>
    <p>Welcome to the home page!</p>
    <MyComponent />
  </div>
</template>

<script>
import MyComponent from '@/components/MyComponent.vue';

export default {
  name: 'Home',
  components: {
    MyComponent,
  },
};
</script>