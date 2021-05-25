# Week 2

As packages were a part of this week's curriculum, I packaged my input sanitising into functions into reusables.py where possible, so that I can reuse them at a later time.

### Task 1 - Objectives

- get user input of a float number
- check if the number is lower than .50 then round the figure to lower end
- check if the number is greater than .51 then round the figure to higher end
- example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

### Walkthrough

I imported the ```math``` package to have the rounding methods ```floor``` and ```ceil``` to round the number up and down as desired.

I then called the function input_float, which takes a user input that can be a float and returns that float.

```python
import math
from reusables import input_float

num_float = input_float()


```
input_float prompts a user for an input, and ensures it is suitable as a float. It will return either the phrase "exit" if the user types this as part of their response, or the desired float:

```
def input_float(): #makes sure that the input is a float
    #Will either return the input as a float or the phrase "exit"
    while True:
        var = input(f"Please enter a float. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                return float(var)
            except:
                print("input not recognised")
                continue
   ```


Other than that, I simply subtracted the rounded down number from the float that was input. This leaves a float between 0 and 1, and determining whether this is greater than 0.5 or not lets me determine whether to round up or down.

```python
#subtracting the rounded down number leaves only the decimal part.
# then applying control flow. Could also have been solved by using int(num_float), which works quite similarly to math.floor.
if num_float - math.floor(num_float) > 0.50:
    print(math.ceil(num_float))
else:
    print(math.floor(num_float))
```