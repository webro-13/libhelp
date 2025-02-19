def hlib():
    if input() == 'libhelp':
        print('this is a python helper library made to help you figure out the syntax of other python libraries. just type the name of the library you want to know about and it will tell you the syntax of the functions in that library. to find out what libraries I know, type "known libs.')
    elif input() == 'known libs':
        print('pycheet')
    elif input() == 'pycheet':
        print('pycheet is a python library that has a few functions that print out different greetings.')
        print('to use the functions in this library, type "from pycheet import hello"')
        print('then type "hello.th()" to print "Hello, World!"')
        print('type "hello.h()" to print "Hello"')
        print('type "hello.hn(name)" to print "Hello " + name')
        print('type "hello.sh()" to print "Hi"')