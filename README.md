# TIPS & Key Notes

## Great, you completed two exercises. Here are some simple programming tips to make the best of the course:

## Be as persistent as you can before looking at hints or the solution. Persistence is gold in programming.

##  Sometimes taking a break is the best thing you can do to solve a problem.

## When getting an error, don't panic, but look closely at the error message. Knowing how to fix errors is as important as knowing to write programs.


## slicing syntax is upper-bound exclusive

## Besides the left-to-right positive indexing system that starts from zero, sequence data types such as lists also have a second indexing system that starts from -1 and decreases by one from right to left. 

## Syntax of list slicing is [start:end:step] . When you don't pass a step, Python assumes the step is 1. [:]  itself means get everything from start to end. So, [::2]  means get everything from start to end at a step of two.

## A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.

## As you see, accessing dictionary values follows the same syntax as accessing list items. The difference is that lists have indexes, while dictionaries have keys which you create by yourself.

## range()  is a Python built-in function that generates a range of integers. However, range()  creates a Python range object. To get a real list object you need to use the list() function to convert the range object into a list object.

## We used a set  function to convert the list to a set which would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates. Then using list  we converted the set back to a list. The drawback here is that the original order of the items is lost. If you need to preserve the order you may want to use the solution in Answer 2 below.

## Ordered dictionaries are another data type in Python that unlike sets and normal dictionaries they preserve the order of the items. Here OrderedDict.fromkeys(a)  would produce an OrderedDict  like [('1', None), (1, None), (2, None)] . Then we would convert that OrderedDict  to a list.

## d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values  items.

## pprint  module which is used to print out well formatted views of datatypes in Python.

## string  is a built-in module and string.ascii_lowercase  returns a string object containing all 26 letters of English alphabet. Then we simply iterate through that string and print out the string items.

## A for  loop is used to repeat an action (i.e. print ) until the iterating sequence (i.e. range ) is consumed. In our case it would print all items of the range one by one.

## Always put non default parameters first followed by default ones.

## A function is called using bracket notation () .

## indent=4  will create 4 white spaces to indent the different levels of the dictionary items and sort_keys=True  tells Python to preserve the order of the dictionary thrown in the file.

## In the code Python is actually referring to the script name which is requests  and it doesn't find a get attribute for that name. Script names load in the current namespace. They are actually stored in the __name__  variable. You could try to print that variable out and you would see that it prints your script name. Therefore you should not name your scripts under library names. 