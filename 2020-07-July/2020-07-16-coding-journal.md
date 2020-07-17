Very good [article](https://itnext.io/efficiently-understanding-and-using-nuxt-vuex-7905eb8858d6) on Nuxt and Vuex. A little better than official documentation of vuex on nuxt official site, IMO. Read it in full.

According to author, if we have more than 3 API calls or state management items to handle the modular approach is required. 

Unless we plan on configuring Vuedx with some fancy plugins or changing its configuration, `index.js` should never exist in the `store` folder. Instead each 'widget' needs its own file

##State 

State is a simple function that returns the object stored inside it. 

`store/cars.js`

```
export const state = () => ({
  list: [],
  car: {}
})
```

In our component html we can access it using `$state.cars.list`, and in our javascript via `this.$state.cars.list`. This is fine if it is read only. If we could change state directly, then we skip the parts that will let the rest of our app know it has changed. 

It is very important to keep our state as flat as possible. Deeply nested objects in a state lose reactivity. For example, if our state contains something like `store.state.cars.car.color`, mutations on color would need to be forced to reload. It is better to make a new store module just for a single `car` then. This is because if Vuex had to walk down a deep chain of object keys there is a huge performance hit, as well as a possibility of a never-ending loop. 

##Getters

Think of getters as a computed properties of a store. They should read the current state of the module and return someting. It should give some meaning to what it is expected to present. Meaning full names are very important!

```
totalCars: state => {
  return state.cars.length
},
blueCars: state => {
  return state.cars.filter(car => car.color === "blue")
}
```

Getters are always read-only values in our views, however the combination of these with computed properties can provide us a custom setter. 

##Mutation

This is how to commit values in state. We don't call it directly because a mutation is a reactive event and we would want our app to know when something is changed. 

```
export const mutation = {
  set (state, cars) {
    state.list = cars
  },
  add (state, value) {
    merge (state.list, value)
  },
  remove (state, {car}) {
    state.list.splice(state.list.indexOf(car), 1)
  },
  setCar(state, car) { state.car = car }
}
```

With this we have an access to call `$store.commit('cars/set', [{id: 1, model: "Tacoma", brand: "Toyota"}])`, etc. This is useful in components with the `fetch`, `asyncData` and `nuxtServerInit` functions when we want to prefill the store with default values, or to use it as a `set` handler in a computed property.

##Action 

These are useful for any asynchronous activity the application needs. Especially useful for calling a backend server, or when non-blocking mutation are needed. 

```
export const action = {
  async get({commit}) {
    await this.$axios.get('cars')
      .then((res) => {
        if (res.status === 200) {
          commit('set', res.data)
        }
      })
  },
  async show({commit}, params) {
    await this.$axios.get(`cars/${params.car_id}`)
      .then((res) => {
        if (res.status === 200) {
          commit('setCar', res.data)
        }
      })
  },
  async set({commit}, car) {
    await commit('set', car)
  }
}
```

Here we defined three actions, `get`, `show` and `set`. Get would fetch our entire car collection and on success set the store with the list the server gives back. Show is the same, but we can pass in query parameters. This is useful for setting up searches or any other scenario we can imagine where params are needed. Last is an addition onto our previous mutation, an action calling the mutation 'set' from above. This way we can set up a successful future for using promises or async/await calls.

