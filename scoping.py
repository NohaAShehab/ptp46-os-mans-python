
"""
    *************** 1- define global variable
"""
username = 'iti'

print(username)


username = 'updated'


""" ******** define the local variable ?? 
    any variable defined inside a function ?
"""


def say_hello():
    user =  "Ahmed"   # this a local variable is accessed only inside a function.
    print(f"user = {user}")

# say_hello()
# print(user)  # NameError: name 'user' is not defined. Did you mean: 'super'?

"""

    3- access global variable  from inside function 
"""
""" 3.1 read the global variable """

def print_username ():
    print(f"from inside function username = {username}")

print_username()


""" 3.2 update the global variable """

def modify_username ():
    username = input("Enter your username: ") # create new local variable ?
    print(f"username = {username}")

# modify_username()
# print(username)


def modify_username ():
    global username
    username = input("Enter your username: ") # please don't create new local variable, use the global one
    print(f"username = {username}")

# modify_username()
# print(f"After calling username = {username}")




""" ************ Functions inside a function ***************** """
""" 4- access local variable from inner functions """
def outer_function():
    track = "Open source Application"  # local variables
    print(f"track = {track}")
    def inner_function():
        print(f"---- from inner track = {track}")

    inner_function()


# outer_function()


""" modify local variable from inside the inner function ??"""
def outer_function2():
    track = "Open source Application"  # local variables

    def inner_function():
        track = input("Enter your track: ")  # new local variable
        print(f"---- from inner track = {track}")

    inner_function()
    print(f"track = {track}")

# outer_function2()
""" """

def outer_function3():
    track = "Open source Application"  # local variables

    def inner_function():
        nonlocal track  # please don't create new one use the parent's one
        track = input("Enter your track: ")  # use the local one of your parent
        print(f"---- from inner track = {track}")

    inner_function()
    print(f"track = {track}")

#
# outer_function3()

#####################################
def A():
    track = "Open source Application"
    def B():
        def C():
            def D():
                def E():
                    def F():
                        nonlocal track
                        track = input("Enter your track: ")
                        print(track)
                    F()
                E()
            D()
        C()
    B()
    print(f"after calling F () -> track = {track}")

# A()

# def test_scoping3():
#     def B():
#         def C():
#             def D():
#                 def E():
#                     def F():
#                         nonlocal track
#                         track = input("Enter your track: ")
#                         print(track)
#                     F()
#                 E()
#             D()
#         C()
#     B()
#     print(f"after calling F () -> track = {track}")
#
# test_scoping3()


#########################
def test_scoping2():
    def B():
        def C():
            def D():
                def E():
                    def F():
                        global track
                        track = input("Enter your track: ")
                        print(track)
                    F()
                E()
            D()
        C()
    B()
    print(f"after calling F () -> track = {track}")

test_scoping2()



















