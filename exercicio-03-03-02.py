'''
Um objeto de função é um valor que pode ser atribuído a uma variável ou passado
como argumento.
Por exemplo, do_twice é uma função que toma um objeto de função como argumento e
o chama duas vezes:
'''

# 1
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
# do_twice(print_spam)

# 2
def do_twice(f, value):
    f(value)
    f(value)
def print_spam(value):
    print(value)
# do_twice(print_spam, 'spam')

# 3
def print_twice(bruce):
    print(bruce)
    print(bruce)

# 4
def do_twice(f, value):
    f(value)
    f(value)
def print_twice(bruce):
    print(bruce)
    print(bruce)
# do_twice(print_twice, 'spam')

# 5
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
do_four(print_twice, 'spam')
