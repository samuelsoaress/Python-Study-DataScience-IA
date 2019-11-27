answer = 42
name = "PythonBo"

def add_numbers(a, b):
    print(a + b)


def add_numbers(a: int, b: int):
    return a  + b


def var_args(nome, *args): # *args == aceita muitos argumentos 
    print(nome)
    print(args)


var_args("Mark", '1211', 'student_id:90', 2323, 21)


def var_kwargs(nome, **kwargs): # aceita n paramentros com chaves
    print(nome)
    print(kwargs["description"], kwargs["feedback"])


var_kwargs("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)