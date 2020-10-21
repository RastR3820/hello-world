# A simple python program to test the Repl.it IDE
import obj
import test.echo

x = 5
y = 7

print("Why Hello There!\n")
print("x + y = ", x+y)

obj1 = obj.Test(7,"thing")
obj1.doThing()

obj2 = obj.Test(3,"whatever")
obj2.doThing()

obj3 = test.echo.Marco("this was a triumph")
obj3.polo()
