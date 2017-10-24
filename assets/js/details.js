Vue.component('star-rating', {
  template: `<div class="rating-input rating">
      <span v-for="(_, index) in possible" class="star mr-1">
        <i v-if="index < rating" v-on:click="onRate(index + 1)" class="fa fa-star"></i>
        <i v-if="index >= rating" v-on:click="onRate(index + 1)" class="fa fa-star-o"></i>
      </span>
  </div>`,

  data: function() {
    return {
      possible: 5,      
      rating: 0,
    }
  },

  computed:{
    active: function() {
      return this.rating;
    },
    inactive: function() {
      return this.possible - this.rating;
    }
  },

  methods: {
    onRate: function(index) {
      this.rating = index;
      this.$emit('ratingchange', this.rating);
    } 
  }
})

var detailsApp = new Vue({
  el: '#panel4',
  data: {
    user_id: null,
    rating: 0,
    comments: '',
    anonymous: false,

    loading: false
  },

  computed: {
    allowSubmit: function() {
      return this.comments.trim().length > 0 || this.rating != 0
    }
  },

  methods: {
    onSubmit: function(event) {
      var self = this;
      event.preventDefault();

      console.log({
        user_id: self.user_id,
        rating: self.rating,
        comments: self.comments,
        anonymous: self.anonymous
      });
    },
    
    onRatingChange: function(rating) {
      this.rating = rating;
    }
  },

  mounted: function() {
    this.user_id = userObject.id
  }
})

