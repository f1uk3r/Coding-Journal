# requesting API with an Authorisation token

[Resource](https://stackoverflow.com/questions/44245588/how-to-send-authorization-header-with-axios)

```
getEntries () {
  this.$axios.$get(
    'dashboard/', {
      headers: {
        Authorization: `Bearer ${this.$store.state.admin.jwt}`,
        'Content-Type': 'application/json'
      }
    })
    .then((response) => {
      this.entries = response.data.results
    })
}
```

***

redirect after login. [Resource](https://cmty.app/nuxt/auth-module/issues/c208)

***

Whenever running pylatex do download these two apt-get dependencies

```
pip install pdflatex
pip install pylatex
sudo apt-get install latexmk
sudo apt-get install -y texlive-latex-extra
```

then use doc.generate_pdf(compiler='pdflatex')

***

