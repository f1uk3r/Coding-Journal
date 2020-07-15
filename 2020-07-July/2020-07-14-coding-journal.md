Learnings from Pomodoro timer

[Creating countdown Timer](https://www.w3schools.com/howto/howto_js_countdown.asp)

[Javascript Timing events](https://www.w3schools.com/js/js_timing.asp)

```
 <button onclick="setInterval(myFunction, 3000)">Try it</button>

<script>
function myFunction() {
  alert('Hello');
}
</script> 
```

setInterval() will kind of start running a loop every x milliseconds.

[Sounds using JavaScript](https://learningsolutionsmag.com/articles/coding-sound-with-javascript-beginner-s-guide)

***

[Very good tutorial on Basic branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

##Create a branch and start working

```
git branch some-branch-name
git checkout some-branch-name
```

or 

`git checkout -b some-branch-name`

Now the head of the git is directed toward this new branch. All the commits now made will be in this branch. If a situation arrives where you have to move back to original master branch to make some fixes without interference of the new branch we made, we just checkout the master. One thing that have to be noted that there shouldn't be any uncommited changes in the `some-branch-name` because git won't allow to checkout to other branches. 

`git checkout master`

Now make a new branch where we will put our fixes in.

`git checkout -b hotfix`

Make some commits and the hotfix is ready to be deployed. Now we merge this `hotfix` branch with the master and then delete this branch. To merge the branch we will first have to checkout to the `master` branch and then have to merge the branches.

```
git checkout master
git merge hotfix
```

Now delete the `hotfix` branch

`git branch -d hotfix`

Now we can go back to `some-branch-name` and finish our feature that we are building. The same procedure have to be followed to mix this branch with master as we did for `hotfix`.

```
git checkout master
git merge some-branch-name
git branch -d some-branch-name
```

***

Tried to search for `nuxt django login` didn't get any solid result so tried `vue django login`. Which should be quite similar in functioning. I tried to find the article that I based my login in Vue application, but couldn't find it. 

This is the [article](https://hackernoon.com/jwt-authentication-in-vue-js-and-django-rest-framework-part-2-788f0ad53ad5) I was talking about just above