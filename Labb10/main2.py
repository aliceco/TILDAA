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
    readGroup(q, q.peek() == "(")
    if not q.isEmpty():
        readMol(q)


def readGroup(q, left_parenthesis):
    if (not q.isEmpty() and q.peek().isdigit()) or q.peek() == ")":
        raise SyntaxFel("Felaktig gruppstart vid radslutet")
    if left_parenthesis:
        q.dequeue()
        while not q.isEmpty() and not q.peek() == ")":
            readGroup(q, q.peek() == "(")
        if q.peek() == ")":
            q.dequeue()
            if not number(q):
                raise SyntaxFel("Saknad siffra vid radslutet")
            return
        raise SyntaxFel("Saknad högerparentes vid radslutet")
    else:
        readAtom(q)


def readAtom(q):
    letter(q)
    number(q)


def letter(q):
    if not q.isEmpty() and q.peek().isupper():
        temp = q.dequeue()
        if not q.isEmpty() and q.peek().islower():
            temp += q.dequeue()
        if temp in atoms:
            return
        raise SyntaxFel("Okänd atom vid radslutet")
    raise SyntaxFel("Saknad stor bokstav vid radslutet")


def number(q):
    number_exists = False
    if q.peek() == "0":
        q.dequeue()
        raise SyntaxFel("För litet tal vid radslutet")
    if not q.isEmpty() and q.peek().isdigit():
        if q.dequeue() == "1" and not q.isEmpty() and not q.peek().isdigit():
            raise SyntaxFel("För litet tal vid radslutet")
        number_exists = True
        while not q.isEmpty() and q.peek().isdigit():
            q.dequeue()
    return number_exists


atomstr = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr " \
        "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd " \
        "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf " \
        "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm " \
        "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
atoms = atomstr.split()


"""def main():
    while True:
        molecule_input = input("")
        if molecule_input == "#":
            break
        print(readFormel(molecule_input))
        

main()
"""