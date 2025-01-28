import { createStore } from 'vuex';

export default createStore({
  state: {
    message: '',
  },
  mutations: {
    setMessage(state, message) {
      state.message = message;
    },
  },
  actions: {
    fetchMessage({ commit }) {
      fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => {
          commit('setMessage', data.message);
        });
    },
  },
});