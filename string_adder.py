<<<<<<< HEAD
def add():
    return 0
=======
def add(*args):
    if not args:
        return 0
    if len(args) == 1:
        return int(args[0])
>>>>>>> 3142291 (Implement string adder function and update tests for null and single value inputs)
