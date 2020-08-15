Python: Best way to handle list.index() that might not exist. [Stack overflow](https://stackoverflow.com/questions/2132718/best-way-to-handle-list-indexmight-not-exist-in-python)

Use try-except block

***

Both headers and footers in pylatex are created using header.create() method. [Official Doc](https://jeltef.github.io/PyLaTeX/current/examples/header.html)

***

Python use `functools.partial` to pass an argument to the `filter` function

```python
from functools import partial
for i in range(len(chapters_selected)):
  all_relevant_questions_from_chapter = list(filter(partial(question_filter, chapter=chapters_selected[i]), data_list))
```

where filter function is as follows

```python
def question_filter(question_dict, chapter):
  if(subject_selected == question_dict["subject"] and standard_selected == int(question_dict["standard"]) and question_dict["options"] != [] and not re.match("http", question_dict["question"]) and question_dict["chapter"] == chapter):
    if (re.match("http", question_dict["question"])):
      return False
    for i in range(len(question_dict["options"])):
      if (re.match("http", question_dict["options"][i])):
        return False
    return True
  else:
    return False
```