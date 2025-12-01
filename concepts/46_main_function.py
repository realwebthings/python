# *************************************
# *   __name__ and "__main__"         *
# *************************************

# __name__ is a built-in variable which evaluates to the name of the current module.
# However, if a module is being run as the main program, __name__ is set to the string "__main__".
# This is used to check whether the current script is being run on its own or being imported somewhere else.

import message

print(__name__)


# Python interpreter sets "special variables", one of which __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

def main():
    print("Hello")
    print("World!")

if __name__ == "__main__":
    main()
