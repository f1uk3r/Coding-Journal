- codecanyon.net for paid codes

### Instead of passing parameters in computed properties use methods

The difference between a computed property and a method is that computed properties are cached and change only when their dependencies change. A method will evaluate every time it's called.

If you need parameters, there are usually no benefits of using a computed property function over a method in such a case. Though it allows you to have a parametrized getter function bound to the Vue instance, you lose caching so not really any gain there, in fact, you may break reactivity (AFAIU). 

https://stackoverflow.com/questions/40522634/can-i-pass-parameters-in-computed-properties-in-vue-js

- Check [this example](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_slideshow) for CSS of dots in carousel

- Use [level in bulma](https://bulma.io/documentation/layout/level/) to align (left/right/center) in same line 

- [vue-meta](https://www.npmjs.com/package/vue-meta) to apply meta tags in Vue2. Doesn't work in Vue3

- Box shadow: rightpx bottompx color;

### Toast vs SnackBar

Toast is an UI component that is used to show message or notification that does not reqire any user action. It is independent to the activity in ich it is being shown and disappears automatically after the set duration.

Snackbar is a UI component used to show popup message to user that requires some user action. It can disappear automatically after set time or can be dismissed by user.

https://www.geeksforgeeks.org/differnce-between-android-toast-and-snackbar/

