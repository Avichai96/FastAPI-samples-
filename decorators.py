''' Create decorators example '''

# Function decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

# Class decorators
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print('Display function run')

decorator_class
def display_info(name, age):
    print(f'display_info run with argumemts {name} {age}')


display()
display_info(name='Avichai', age=25)