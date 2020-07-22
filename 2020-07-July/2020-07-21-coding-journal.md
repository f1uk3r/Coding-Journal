Some useful tools working with json and regex

[json formatter](https://jsonformatter.org/)

[regex online checker](https://regex101.com/)

***

Substituting with regex in python. [Resource](https://www.w3schools.com/python/python_regex.asp)

In python if we have too match anything we use `((?s).*)` and then use matched.group(1) to extract what we want

***

To querySelector an select-option tag in vanilla javascript

```
var select = document.getElementById('color')
var currentOpt = select.option[select.selectedIndex]
```

***

JSON Server turn a json file to a API server making it ready to be consumed by javascript

`npm install -g json-server`

then run the server with this command

`json-server --watch db.json`

where db.json is our json file

