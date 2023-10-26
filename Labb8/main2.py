from linkedQFile import LinkedQ

"""
Många av nedanstående metoder är inspirerade från föreläsningen om rekursiv medåkning
"""

class Syntaxfel(Exception):
    pass



def read_molekyl(molekyl):
    read_atom(molekyl)
    if molekyl.peek() == ".":
        molekyl.dequeue()
    else:
        read_num(molekyl)




def read_atom(molekyl):
    read_LETTER(molekyl)
    if not molekyl.peek().isalpha():
        return
    else:
        read_letter(molekyl)


def read_LETTER(molekyl):
    next_char = molekyl.peek()
    if next_char.isalpha() and next_char.isupper():
        molekyl.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet ")


def read_letter(molekyl):
    next_char = molekyl.peek()
    if next_char.isalpha() and next_char.islower():
        molekyl.dequeue()
        return
    raise Syntaxfel("Saknad liten bokstav vid radslutet ")

def read_num(molekyl):
    numbers = molekyl.dequeue()

    if int(numbers) == 0:
        raise Syntaxfel("För litet tal vid radslutet ")
    else:
        while not molekyl.peek() == ".":
            numbers += molekyl.dequeue()

        if int(numbers) > 1:
            return
        raise Syntaxfel("För litet tal vid radslutet ")

def makeQ(mening):
    q = LinkedQ()
    for char in mening:
        q.enqueue(char)
    q.enqueue(".")
    return q

def printfel(q):
    error_string = ""
    while not q.peek() == "." and q.peek():
        error_string += q.dequeue()
    return error_string

def check_molekyl(mening):
    q = makeQ(mening)
    try:
        read_molekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + printfel(q)
    
print(check_molekyl("H2"))