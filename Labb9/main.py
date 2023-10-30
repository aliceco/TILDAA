
from linkedQFile import LinkedQ


class SyntaxFel(Exception):
    pass


def readFormel(molecule):
    q = LinkedQ()
    for i in molecule:
        q.enqueue(i)
    try:
        readMol(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxFel as fel:
        err_str = ""
        while not q.isEmpty():
            err_str += q.dequeue()
        return f"{fel} {err_str}"


def readMol(q):
    readGroup(q)
    if q.isEmpty() and len(left_parentheses) > len(right_parentheses):
        raise SyntaxFel("Saknad högerparentes vid radslutet")
    if not q.isEmpty():
        readMol(q)


def readGroup(q):
    if not q.isEmpty() and q.peek() in numbers:
        raise SyntaxFel("Felaktig gruppstart vid radslutet")
    if not q.isEmpty() and q.peek() == "(":
        q.dequeue()
        left_parentheses.append("1")
        if q.peek() == ")":
            raise SyntaxFel("Felaktig gruppstart vid radslutet")
        readMol(q)
    if not q.isEmpty() and q.peek() == ")":
        right_parentheses.append("1")
        if len(right_parentheses) > len(left_parentheses):
            raise SyntaxFel("Felaktig gruppstart vid radslutet")
        q.dequeue()
        if not number(q):  # Syntaxfel om inte en siffra kommer efter högerparentes
            raise SyntaxFel("Saknad siffra vid radslutet")
        readMol(q)
    if not q.isEmpty():
        readAtom(q)


def readAtom(q):
    uppercase(q)
    number(q)


def uppercase(q):
    if not q.isEmpty() and q.peek().isupper():
        temp = q.dequeue()
        if not q.isEmpty() and q.peek().islower():
            temp += q.peek()
            q.dequeue()
        if temp in atoms:
            return
        raise SyntaxFel("Okänd atom vid radslutet")
    raise SyntaxFel("Saknad stor bokstav vid radslutet")


def number(q):
    number_exists = False
    num1 = q.peek()
    if num1 == "0":
        q.dequeue()
        raise SyntaxFel("För litet tal vid radslutet")
    if num1 in numbers:
        q.dequeue()
        if num1 == "1" and q.peek() not in numbers:
            raise SyntaxFel("För litet tal vid radslutet")
        number_exists = True
        while q.peek() in numbers:
            q.dequeue()
    return number_exists


atomstr = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr " \
        "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd " \
        "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf " \
        "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm " \
        "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
atoms = atomstr.split()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
left_parentheses = []
right_parentheses = []


# def main():
#     while True:
#         molecule_input = input("")
#         if molecule_input == "#":
#             break
#         print(readFormel(molecule_input))
#         left_parentheses.clear()  # Rensar parenteslistorna efter varje instoppad molekyl
#         right_parentheses.clear()


# main()
