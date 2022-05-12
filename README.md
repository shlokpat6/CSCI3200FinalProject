I implemented a rudimentary version of racket. 

To start, the user can enter either a string or an exp. The string must be all uppercase characters. If they enter an expression, it will be an s_exp, meaning it must be surrouned by parentheses. The expressions that are possible are one or more atoms, which are var(the function), num, and str. The var must consists of all lowercase letters to differentiate it from str. The var can also be some basic arithmetic symbols, with the exception of division. Additionally, defining variables via def considers the variable to be be an str. This means that any defined variable must follow the rules of a string, meaning it must consist of one or more capital letters.

In terms of functions, I implmented cons, cdr, car, add, sub, mul, div, mod, def, and list. The notation for each is identical to that of racket, meaning a user enter a function followed by two arguments, all of which needs to be wrapped by parentheses.

As mentioned earlier, for each of the arithemetic operations, the user can input either the keywords listed above (i.e add, sub, mul, mod, and div) or with the exception of division, they can use the corresponding symbols (i.e +, -, *, %). 

The cons and list functions are capable of constructing cons structures from two or more of either strings or ints. In my version, the cons cells will not be seperated by decimals, but rather spaces. This cons version will also not take a null character.

The car function will return the very first item in a cons structure, whereas the cdr will return everything else.

The def function takes an argument with the same structure as a string (i.e all uppercase) and stores the second argument within it. As it stands, this function both stores and returns the value simultaneously. 

Currently, I have implemented the program feature to take in a user input. This allows the user to input their task directly onto the console rather than having to enter the script and change the program manually. However, the user must still run the code each time they want to enter an input.

Additionally, users may directly enter a string and number without the parentheses. These values will be displayed on the console.

Irregular inputs that do not follow the grammer will be met with an error. 

Implementation comments can be found embedded in the python script. 

Sample test code:
(add 5 (mul 3 (div 1 ( add 3 (sub 9)))))

(* 3 (- 2 (+ 6 8)))

(cons 1 2)

237

(car (cons 4 8))

(cdr (cons 3 5))

(car (cons 2 (cons 3 5)))

(list 3 8 13 27)

(car (list 3 8 13 27))

(cons HELLO WORLD)

(cons IT (cons IS (cons UBSURDLY (cons OUTSIDE TODAY))))

(cdr (cons SERIOUSLY (cons WHY (cons IS (cons IT (cons SO HOT))))))

(list (list 1 2) (list 3 4))

(cdr (list 3 8 13 27))
