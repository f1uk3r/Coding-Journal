[async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

`await` keyword is permitted within async function. The `async` and `await` keywords enable asynchronous, promise-based behavior to be written in a cleaner style, avoiding the need to explicitly configure promise chains. 

```
async function nameOfTheFunction (param) {
  statement
} 

```

The return value of an async function will always be a `Promise` which will be resolved with the value returned by the async function or rejected with an exception thrown from or uncaught within the async function. If the return value of an async function is not explicitly a promise, it wil be implicitly wrapped in a promise.

Async function can contain zero or more `await` expressions. Code above the first `await` keyword will run synchronously and `await` expression suspend progress through an async function, yielding control and subsequently resuming progress only when an awaited promise-based asynchronous operation is either fulfilled or rejected. 