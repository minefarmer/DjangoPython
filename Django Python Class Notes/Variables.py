"""
variables are 'tags'.
variable = value.
all ready made commands are called functions. (int(), str(), type(), etc).



"""

>>> type(message)
<class 'str'>
>>> age = 81
>>> type(age)
<class 'int'>
>>> print(age)
81
>>> name = 'carl'
>>> family_name = 'matson'
>>> 1_f = 'carl   #  NO Underscores
  File "<stdin>", line 1
    1_f = 'carl
     ^
SyntaxError: invalid token
>>> a-r = 'rich'
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> name = '206'
>>> color = 'red'
>>> max_speed = 120
>>> print(name)
206
>>> print(max_speed)
120
>>> print(color)
red
>>> name = 'rich'
>>> print(name)
rich
>>> a = 3
>>> a = 6
>>> a
6
>>> 'Hello' + 'world'
'Helloworld'
>>> 'Hello ' + 'world'
'Hello world'
>>> 'Hello ' + 'world' + '!'
'Hello world!'
>>> a = 'hello '
>>> b = 'world'
>>> c = '!'
>>> a + b + c
'hello world!'
>>> d = a + b + c
>>> print(d)
hello world!
>>> a
'hello '
>>> b
'world'
>>> c
'!'
>>> d
'hello world!'
>>> exit()
(base) carl@carlw:~/Github/DjangoPython$

(base) carl@carlw:~/Github/DjangoPython$ python
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> 
>>> 3 + 2
5
>>> 4 + 5 + 5
14
>>> a = 1
>>> b = 60
>>> c = 40
>>> a + b + c
101
>>> d = 'hello '
>>> a + d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> d = '20'
>>> a = '10'
>>> a + d
'1020'
>>> 'hello ' + 'world'
'hello world'
>>> 2 + 2.0
4.0
>>> 2 + 2
4
>>> 2.0 + 2.0
4.0
>>> 2.0 + 2
4.0
>>> '20'
'20'
>>> int('20')
20
>>> 
>>> a = '20'
>>> b = 30
>>> s + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> int(a) + b
50
>>> 'sala'
'sala'
>>> int('sala')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'sala'
>>> 
>>> str(ali)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ali' is not defined
>>> a = 20
>>> type(a)
<class 'int'>
>>> str(a)
'20'
>>> 'hello' + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'hello' + str(a)
'hello20'
>>> 'hello ' + str(a)
'hello 20'
>>> a = 2.0
>>> str(a)
'2.0'
>>> 2 + 2.0
4.0
>>> 2 + int(2.0)
4
>>> float(2)
2.0
>>> 2.5
2.5
>>> int(2.5)
2
>>> 2.1
2.1
>>> int(2.1)
2
>>> int(2.8)
2
>>> 