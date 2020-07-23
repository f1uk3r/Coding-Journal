Random item from JavaScript array. [Stack Overflow](https://stackoverflow.com/questions/5915096/get-random-item-from-javascript-array)

`var item = items[Math.floor(Math.random() * items.length)]`

***

JavaScript filter. [Resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

***


### Asked on discord

So I am using `fetch` a json which is served with `json-server` like this

```
async function fetchData () {
  fetch('http://localhost:3000/data')
    .then((data) => {
      console.log(data.json())
    })
}
```

In the console it is giving me a promise with `<state>: "pending"`. What am i doing wrong. How do I correctly get the data so that I can use my json.

### Answer

`data.json()` also returns a `Promise`, so you'd do:

```
async function fetchData () {
  fetch('https://localhost:3000/data')
    .then(data => data.json())
    .then(json => {
      // here you can do stuff w/ json : )
    });
}
```

 or

```
async function fetchData () {
  const response = await fetch('https://localhost:3000/data');
  const json = await response.json();

  return json;
}

const data = await fetchData(); // => { key1: value1, key2: ... }
```

***

`.innerHTML` -> write any html you want to put here

***

I'll work on latex part of the question later. Right now I'll move on to jspdf.

Do check out this [resource](https://ckeditor.com/docs/ckeditor4/latest/features/mathjax.html) when start working on math-tex again
***

