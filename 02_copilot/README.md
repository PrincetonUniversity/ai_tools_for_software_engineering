# Microsoft Copilot

On May 20, 2024, OIT announced:

> Microsoft Copilot (formerly known as Bing Chat), a generative artificial intelligence (AI) tool that can be used to generate or analyze text and images, is now available for use at Princeton University. Copilot is currently the only generative AI tool made available by the Office of Information Technology (OIT).
>
> Data security, privacy and accuracy in Copilot 
>
> In order to help secure Princeton data and reduce risk to the University, it is recommended that you avoid writing prompts that include restricted or confidential information, including proprietary research data. 
>
> Additionally, AI responses can be biased, inaccurate, or may contain copyrighted information. Always review, validate, and iterate on responses provided before sharing them more broadly. 
>
> How to use Copilot with your Princeton netID 
>
> To use Copilot, sign in with a work or school account using a princeton.edu netID and password. Doing so will provide greater data protection, in which data is not saved or used to train the model. The same level of protection is not available when using Copilot without your Princeton.edu account or another generative AI tool.

Learn more about OIT's announcement: [Microsoft Copilot at Princeton University](https://oit.princeton.edu/microsoft-copilot-princeton-university)

## Disambiguation

- Microsoft Copilot: A generative A.I. chatbot for coding tasks
- Copilot for 365: A.I. for Outlook, Word, Excel and other office applications
- GitHub Copilot: An A.I. coding assistant. It can be fine-tuned on your repositories.

## Using Copilot

To use Copilot, users must sign in to [Copilot](https://copilot.microsoft.com/?BCB=0&showconv=1) with their princeton.edu account using their netID and password.

1. On the [Copilot website](https://copilot.microsoft.com/?BCB=0&showconv=1), in the top-right corner, select Sign in, then Sign in with a work or school account. Follow the prompts for netID login and Duo two-factor authentication.

2. When you are signed in with your Princeton account, you will see a green Protected label in the top-right corner, indicating greater data protection.

3. Visit the [Copilot FAQ](https://www.microsoft.com/en-us/bing?form=MG0AUO&OCID=MG0AUO#faq).

[Use Copilot to build a website](https://www.microsoft.com/en-us/bing/do-more-with-ai/build-a-website?form=MA13KP)  
[Create and test APIs with Copilot](https://www.microsoft.com/en-us/bing/do-more-with-ai/create-and-test-apis?form=MA13KP)  
[Copilot: AI prompt writing 101](https://www.microsoft.com/en-us/bing/do-more-with-ai/ai-prompt-writing?form=MA13KP)  

#### Generative AI and data accuracy

Regardless of the tool or mode, AI responses can be biased, inaccurate, inappropriate, or may contain unauthorized copyrighted information.  Always review, validate, and iterate on responses provided by any Generative AI tool before relying on them or sharing them broadly.

## Hands-On Exercise 1: Simple Code Generation

Imagine that you have a data file in CSV format like this:

```
timestamp,temperature,length
1210,3.9,6.5
1220,3.8,6.4
1230,3.7,6.4
1240,3.8,6.9
```

Use Copilot to generate a Python script that reads in a CSV file and calculates the average of the second column.


## Hands-On Exercise 2: Debugging

Copilot can be used to identify bugs. Consider the code below:

```Python
"""This script should print a list of non-furniture objects in
   alphabetical order.""" 

def remove_furniture(items):
    furniture = {'couch', 'table', 'desk', 'chair'}
    items_furniture_removed = [item for item in items if item not in furniture]
    return items_furniture_removed

# input list of items
items = ['book', 'pencil', 'desk', 'door']

# remove furniture objects from items
items = remove_furniture(items)

# print remaining items in alphabetical order
for item in items.sort():
    print(item)
```

The author of the code was expecting the following output:

```
$ python no_furniture.py
book
door
pencil
```

Instead, the output is:

```
$ python no_furniture.py 
Traceback (most recent call last):
  File "no_furniture.py", line 16, in <module>
    for item in items.sort():
TypeError: 'NoneType' object is not iterable
```

Ask Copilot if it can spot the bug in the code. When entering the prompt, select Shift+Enter to make a line break.

## Hands-On Exercise 3: Unit Testing

Ask Copilot to create a Python function that performs some simple task. Also have it generate unit tests for the code. Here is an example:

```
Write a Python function called remove_large that takes a list of integers and returns the list with all values greater than a threshold value removed. Generate unit tests for the function.
```

## Hands-On Exercise 4: Code Translation

1. Use Copilot to convert the MATLAB code below to Python using [CuPy](https://cupy.dev/):

```matlab
gpu = gpuDevice();
fprintf('Using a %s GPU.\n', gpu.Name);
disp(gpuDevice);

X = gpuArray([1 0 2; -1 5 0; 0 3 -9]);
whos X;
[U,S,V] = svd(X)
fprintf('trace(S): %f\n', trace(S))
quit;
```

2. Use Copilot to covert the following TensorFlow script to PyTorch:

```python
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print('\nTest accuracy:', test_acc)
```

## Hands-On Exercise 5: Increasing Performance

Ask Copilot to rewrite the code below to run faster. You may try specifying a specific approach such as NumPy, Numba or multiprocessing.

```python
import random

N = 10000

x = []
for i in range(N):
    x.append(random.random())

print(sum(x))
```

## Hands-On Exercise 6: Documentation

Ask Copilot to generate a docstring for the following function. Consider also asking it add [type hints](https://www.geeksforgeeks.org/type-hints-in-python/).

```python
def remove_furniture(items):
    furniture = {'couch', 'table', 'desk', 'chair'}
    items_furniture_removed = [item for item in items if item not in furniture]
    return items_furniture_removed
```

Certain IDEs like Spyder also have the ability to generate docstrings.


## Parallelizing Code

We saw above how simple Python code for CPUs could be ran on a GPU. Another line of work to be aware of is [automatically parallelizing codes using MPI](https://github.com/Scientific-Computing-Lab-NRCN/MPI-rical).
