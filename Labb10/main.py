"""
The version with digit list

"""

from linkedQFile import LinkedQ

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

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
    rutan = Ruta() #skapa ruta som är ett object
    if q.peek() == ")" or q.peek() in numbers:
        raise SyntaxFel("Felaktig gruppstart vid radslutet")
    if left_parenthesis:
        q.dequeue()
        while not q.isEmpty() and not q.peek() == ")":
            readGroup(q, q.peek() == "(")
        if q.peek() == ")":
            q.dequeue()
            if not q.isEmpty() and not number(q).isdigit():
                raise SyntaxFel("Saknad siffra vid radslutet")
            
            """
            Om det är en parentesgrupp ska readgroups anrop till readmol returnera en delmolekyl som sätts under rutan.down.
            """
            
            return
        raise SyntaxFel("Saknad högerparentes vid radslutet")
    else:
        atom, num = readAtom(q) #num är en tuple så man måste lägga i num[1] för att få siffran


def readAtom(q):
    atom = letter(q)
    num = number(q)
    return atom, num


def letter(q):
    if not q.isEmpty() and q.peek().isupper():
        atom = q.dequeue()
        if not q.isEmpty() and q.peek().islower():
            atom += q.dequeue()
        if atom in atoms:
            return atom #return the atom?
        raise SyntaxFel("Okänd atom vid radslutet")
    raise SyntaxFel("Saknad stor bokstav vid radslutet")


def number(q):
    num = "" #las till för att kunna retunera
    if q.peek() == "0":
        num += q.dequeue()
        raise SyntaxFel("För litet tal vid radslutet")
    if q.peek() in numbers:
        num += q.dequeue() #försök på att stoppa ihop siffrorna igen
        if num == "1" and q.peek() not in numbers:
            raise SyntaxFel("För litet tal vid radslutet")
        while q.peek() in numbers:
            num += q.dequeue()
    return num


atomstr = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr " \
        "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd " \
        "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf " \
        "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm " \
        "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
atoms = atomstr.split()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    while True:
        molecule_input = input("")
        if molecule_input == "#":
            break
        print(readFormel(molecule_input))
        


#main()