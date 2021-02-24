# -*- coding: utf-8 -*-
"""(8 kyu) Grasshopper - Personalized Message

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bqT89xFS8vLluYnRI2wC7qEVg4FamfTB

Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:


**case** name equals owner, **return**	'Hello boss'

**case** otherwise	**return** 'Hello guest'
"""

def greet(name, owner):
    # Add code here
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'