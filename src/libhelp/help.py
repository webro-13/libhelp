print('this is a python helper library made to help you figure out the syntax of other python libraries. just type the name of the library you want to know about in the parentheses, and it will tell you the syntax of the functions in that library. to find out what libraries I know, type known libs in the parentheses.')

def hlib(lib):
    if lib.lower() == 'known libs':
        print('pycheet')
    elif lib.lower() == 'pycheet':
        print('pycheet is a python library that has a few functions; and allows you to "cheet" on your code. to use the functions in this library, type "from pycheet import hello"')
        print('to use the functions in this library, type "from pycheet import hello"')
        print('then type "hello.th()" to print "Hello, World!"')
        print('type "hello.h()" to print "Hello"')
        print('type "hello.hn(name)" to print "Hello " + name')
        print('type "hello.sh()" to print "Hi"')
        print('and for the password function, type "from pycheet import password"')
        print('then type "password.pass(password)" store a password')
        print('then you can use password.get_pass() to get the password')
    else:
        print('I do not know that library/function. try typing known libs to find out what libraries I know.')