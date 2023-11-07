from Labb10.linkedQFile import LinkedQ

class Syntax_error(Exception):
    pass

def uppercase(q, molekyl):
    if q.peek().isupper():
        q.dequeue()
        lowercase(q)
        return
    raise Syntax_error(f"Saknad stor bokstav vid radslutet {molekyl}") 

def lowercase(q):
    if q.isEmpty() is False and q.peek().islower():
        q.dequeue()
    number(q)

def number(q):
    number = []
    while q.isEmpty() is False:
        number.append(int(q.peek()))
        q.dequeue()
    
    if len(number) == 0: 
        return
    elif number[0] == 0: 
        if len(number) > 1:
            raise Syntax_error(f"För litet tal vid radslutet {''.join(str(num) for num in number[1:])}")
        else:
            raise Syntax_error("För litet tal vid radslutet")
    elif number[0] == 1 and len(number) == 1:
        raise Syntax_error("För litet tal vid radslutet")
        
def molecule_syntax(molecule_input):
    q = LinkedQ()
    for i in molecule_input:
        q.enqueue(i)

    try:
        uppercase(q, molecule_input)
    except Syntax_error as error:
        return str(error)
    return "Formeln är syntaktiskt korrekt"

# def main():
#     while True:
#         molecule_input = input("")
#         if molecule_input == "#":
#             break
#         print(molecule_syntax(molecule_input))

# main()