<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    register() {
      // 處理註冊邏輯
      console.log('Email:', this.email)
      console.log('Password:', this.password)
    }
  }
}
</script>