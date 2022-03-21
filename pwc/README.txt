Funtional requirements

I used Python as it is my strongest language followed by Javascript and Java.

The whole problem can be put into a class Store, which contains all the functions requuired to perform
all the necessary tasks.
The design pattern I intent to use is Factory design pattern, intent to in the sense when we want to 
code things up for a large corporation or a warehouse, this design pattern is what we use.


Non-Funtional Programming

1. Speed
The speed should be optimal as even if we have a 1000+ elements in the cart, since we are using a dictionary 
the search for apples/soup or any other offer should be in constant time O(a+b...+z), where a, b...z 
are all offers, while calculating subtotal would be in linear time O(n), where n is the number of 
elements in the cart.

2. Respourse sharing
The space complexity would also be O(n) i.e linear, for a dictionary in Python.

3. Threading
The program is thread safe as there is only one thread. 


To run the program :

Go to the folder "Grocery", and run
python3 grocery.py

to run tests, go to folder "tests", and run
pyhton3 test_grocery.py