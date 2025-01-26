<template>
  <div id="app">
    <nav>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
nav {
  margin-bottom: 20px;
}
nav a {
  margin-right: 10px;
}
</style>