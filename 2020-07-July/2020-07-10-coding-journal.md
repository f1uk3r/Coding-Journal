Multiple plugins in Vue. [Resource](https://stackoverflow.com/questions/57256629/use-multiple-plugins-with-parameters-in-vuejs)

```
Vue.use(BootstrapVue);

Vue.use(VueAnalytics, {
    id: 'UA-12345678-9'
});
```

***

Import axios globally in Vue. [Resource](https://stackoverflow.com/questions/50370939/import-axios-method-globally-in-vuejs)

>in `main.js`

```
import axios from 'axios'
Vue.use({
    install (Vue) {
    Vue.prototype.$api = axios.create({
      baseURL: 'http://localhost:8000/api/'
    })
  }
})
```

Note: Didn't worked

***

[Vuex official documentation](https://vuex.vuejs.org/guide/state.html)

[Vuex alligator.io article](https://alligator.io/vuejs/intro-to-vuex/)

[Vuex css-tricks article](https://css-tricks.com/intro-to-vue-4-vuex/)





***


Javascript: to parse string, use String()

***

