"""
1. What is the result of the code, and explain?

&gt;&gt;&gt; X = &#39;iNeuron&#39;
&gt;&gt;&gt; def func():
print(X)

&gt;&gt;&gt; func()

ANSWER..

The code defines a variable X as 'iNeuron' outside of the function func(). The function func() prints the value of X,
which is 'iNeuron' because it is accessing the global variable. When func() is called, it prints 'iNeuron'.



-----------------------------------------------------------------------------------------------

2. What is the result of the code, and explain?

&gt;&gt;&gt; X = &#39;iNeuron&#39;
&gt;&gt;&gt; def func():
X = &#39;NI!&#39;

&gt;&gt;&gt; func()
&gt;&gt;&gt; print(X)

ANSWER..

The code defines a variable X as 'iNeuron' outside of the function func(). The function func() defines a
local variable X as 'NI!', which does not affect the global variable. When func() is called, it does not
print anything. When print(X) is called outside of the function, it prints 'iNeuron' because the global
variable was not changed by the function.



-----------------------------------------------------------------------------------------------

3. What does this code print, and why?

&gt;&gt;&gt; X = &#39;iNeuron&#39;
&gt;&gt;&gt; def func():
X = &#39;NI&#39;
print(X)

&gt;&gt;&gt; func()
&gt;&gt;&gt; print(X)

ANSWER..

The code defines a variable X as 'iNeuron' outside of the function func(). The function func() defines
a local variable X as 'NI' and prints it. When func() is called, it prints 'NI'. When print(X) is called
outside of the function, it prints 'iNeuron' because the global variable was not changed by the function.

-----------------------------------------------------------------------------------------------

4. What output does this code produce? Why?

&gt;&gt;&gt; X = &#39;iNeuron&#39;
&gt;&gt;&gt; def func():
global X
X = &#39;NI&#39;

&gt;&gt;&gt; func()
&gt;&gt;&gt; print(X)

ANSWER..

The code defines a variable X as 'iNeuron' outside of the function func(). The function func() uses the "global"
keyword to modify the global variable X to 'NI'. When func() is called, it modifies the global variable X to
'NI'. When print(X) is called outside of the function, it prints 'NI' because the global variable was changed by the function.



-----------------------------------------------------------------------------------------------

5. What about this code—what’s the output, and why?

&gt;&gt;&gt; X = &#39;iNeuron&#39;
&gt;&gt;&gt; def func():
X = &#39;NI&#39;
def nested():
print(X)
nested()

&gt;&gt;&gt; func()
&gt;&gt;&gt; X

ANSWER..

The code defines a variable X as 'iNeuron' outside of the function func(). The function func() defines
a local variable X as 'NI' and then defines a nested function nested() that prints the value of X.
When func() is called, it calls nested(), which prints 'NI'. The value of X outside of the function is still 'iNeuron'.



-----------------------------------------------------------------------------------------------

6. How about this code: what is its output in Python 3, and explain?

&gt;&gt;&gt; def func():
X = &#39;NI&#39;
def nested():
nonlocal X
X = &#39;Spam&#39;
nested()
print(X)

&gt;&gt;&gt; func()

ANSWER..

The code defines a function func() that defines a local variable X as 'NI' and then defines a nested function
nested() that uses the "nonlocal" keyword to modify the variable X to 'Spam'. When func() is called, it calls
nested(), which modifies the value of X to 'Spam'. When func() is finished, it prints the value of X, which is 'Spam'.


-----------------------------------------------------------------------------------------------

"""
