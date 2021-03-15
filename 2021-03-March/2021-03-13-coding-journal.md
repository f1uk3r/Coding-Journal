## Get yesterday's date using Javascript. [Link](https://flaviocopes.com/how-to-get-yesterday-date-javascript/)

'''
const today = new Date()
const yesterday = new Date(today)

yesterday.setDate(yesterday.getDate() - 1)

today.toDateString()
yesterday.toDateString()
'''

## Removing plugins with vue-cli3. [SO Link](https://stackoverflow.com/questions/50155541/remove-plugins-with-vue-cli3)

Go to `package.json` and remove the entry for the plugin/package, delete the directory of your `node_module` and then run

`npm install`

