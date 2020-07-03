Python script to generate these `md` files for these journals. All directories and files will be managed automatically

There isn't whole lot to talk about this script, fairly simple, just had to make some searches for making directory and files. Also to traverse through directory path

```
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
```

had to check if the directory exists with required month and year, if not used `os.makedirs()` to make the directory

`os.chdir(f'./{directory_name}')`

to move up a directory since all the files for a month are to be generated in one particular folder

```
with open(f'{year_today}-{month_today}-{day_today}-coding-journal.md', 'w') as fp:
  pass
```

used `open()` to just create the required file. In future I might write some structure to the file that is being repeated in my journals.

Note: I could have `cd`ed in the required directory in the `open` function as well. [See ex 2](https://www.geeksforgeeks.org/create-an-empty-file-using-python/)

***

following [this article](https://medium.com/@pascalluther/deploy-a-nuxt-spa-app-to-amazons-aws-amplify-74994d4326c1) now

rendering mode SPA is to be applied

6:45. Amplify failed at build.
It probably errored out because I gave it the wrong build folder.

7:23 still building files. Its been about 20 minutes, shouldn't be this slow.

bareback app with buefy did diployed perfectly. Now I have added the project so it have started to build again. Hope JS works in this project. If it does, I might deploy the original repo to have my old commits in the file.