# Details
 This repo contains pseudocode and the solution to the challenge in multiple languages.

# Pseudocode
 This was written to detail my intitial thought process after reading the challenge. Also it was written assuming a hard typed language, but it doesn't actually properly cast values when they should be (for output, etc). But it is pseudcode!. 

# Python solution
 This solution named "Supply.py" will ask for input of supply quantity, and output who we can sell to, for how much, and how much overall we will make. Additionally if supply is entered that is over the demand, then the program will inform you.

 Additionally input doesn't need to be sorted (like in the example input) because of the use of built-ins like max() and index().

 Resources:
    Classes: UT CS303E and CS313E
    https://docs.python.org/3/library/functions.html
    https://docs.python.org/3/tutorial/datastructures.html


# The Challenge
 In our Materials Marketplace we have many different companies all looking for the same material. However, each company is looking for a specific quantity of the material at a price they set themselves. A company approaches our team with a large amount of that material, but not enough to complete every request for it. Given the total amount of the material they have, the company asks us to find out what companies they should sell to in order to maximize their profits. This scenario happens frequently so we need to be able to compute the answer relatively quickly and with minimal processing power.

# Sample Input
 https://s3.amazonaws.com/cocolevio-public/InterviewQuestionExample.PNG
 
 Also available from input.csv