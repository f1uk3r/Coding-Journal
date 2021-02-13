- [Python String replace() method](https://www.w3schools.com/python/ref_string_replace.asp)

```txt = "I like bananas"

x = txt.replace("bananas", "apples")```

- [Save image - Python](https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know)

```import urllib.request

urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")```

- [Center Align Elements](https://www.w3schools.com/css/css_align.asp)

```.center {
  width: 50%;
  margin: auto;
}

- [Right-align block elements in HTML](https://stackoverflow.com/questions/17614801/right-align-block-elements-in-html#comment25640753_17614801)

`div > img { float: right; clear: right; }`

- [Screen width property](https://www.w3schools.com/jsref/prop_screen_width.asp)

- [Window Size in Vue] (https://stackoverflow.com/questions/47219272/how-can-i-use-window-size-in-vue-how-do-i-detect-the-soft-keyboard)

- [Center Image/Element with Bulma](https://stackoverflow.com/questions/48277473/center-image-in-bulma)

```is-horizontal-center {
  justify-content: center;
}```

- [Extract URL from an HTML 'a' tag](https://stackoverflow.com/questions/499345/regular-expression-to-extract-url-from-an-html-link)

```import re
match = re.search(r'href=[\'"]?([^\'" >]+)', s)
if match:
    print(match.group(1))```

- [FontAwesome instagram icon - colorized](https://stackoverflow.com/questions/38507734/fontawesome-instagram-icon-colorized)

```.fa.fa-instagram {
  color: transparent;
  background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background: -webkit-radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background-clip: text;
  -webkit-background-clip: text;
}```