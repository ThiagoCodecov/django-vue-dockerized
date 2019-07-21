<template>
  <div class="container">
    <h1>Cookiecutter Django Vue </h1>
    <p align="center">
      <img src="https://i.imgur.com/SA8cjs8.png">
    </p>
    <p>
      {{ response }}
    </p>
    <button v-on:click="sync">Sync</button>
    <button v-on:click="loadCommits">Show Commits</button>
    <div id="example-1">
      <div v-for="item in commits">
        <h4 v-bind:class="[colorFromStatus(item.statuses)]">{{ item.sha }}</h4>
        <h5>Parents</h5>
        <ul id="example-2">
          <li v-for="p in item.parents">
          {{ p }}
          </li>
        </ul>
        <h5>Statuses</h5>
        <ul id="example-3">
          <li v-for="st in item.statuses">
          {{ st.message }} - {{ st.status_context }} - {{ st.current_status }}
          </li>
        </ul>
      </li>
    </div>
  </div>
</div>
</template>

<script lang="ts">

// calling the backend directly from a vue component is a bad example, 
// this is here just to demonstrate the backend loading data
import axios from 'axios';

export default {
  name: 'FirstComponent',
  data: function() {
         return  {
           response: [],
           commits: []
         }
    },
    created: function(){
        
    },
    methods: {
      loadCommits: function() {
        axios.get('http://localhost:8000/api/commits',).then(response => this.commits = response.data);
      },
      sync: function() {
        axios.post('http://localhost:8000/api/repos', {slug: 'ThiagoCodecov/example-python'}).then(response => this.response = response.data);
      },
      colorFromStatus: function(statuses) {
        if (statuses.length == 0) {
          return 'grey'
        }
        for (var i = 0; i < statuses.length; i++) {
            if (statuses[i].current_status != 'success') {
              return 'red'
            }
        }
        return 'green';
      }
    }
}
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
  .red {
    background-color: red
  }
  .grey {
    background-color: gray
  }
  .green {
    background-color: green;
  }
</style>
