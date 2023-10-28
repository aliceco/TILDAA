from linkedQFile import LinkedQ

paranteser = []

atomstr = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr " \
        "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd " \
        "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf " \
        "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm " \
        "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"

atoms_lst = atomstr.split()

class Syntax_error(Exception):
    pass

def readformel(molecule_input):
    q = LinkedQ()
    for i in molecule_input:
        q.enqueue(i)

    try:
        readmol(q)
    except Syntax_error as error:
        return str(error)
    return "Formeln är syntaktiskt korrekt"

def check_parantes(q):
    pass
        

def readmol(q):
    """
    If mol is group or group+mol
    check if there are parathatheses?
    """
    readgroup(q)
    
    if q.isEmpty():
        return
    elif q.peek() == ")":
        if len(paranteser)  < 1:
            raise Syntax_error()
    else: 
        readmol(q)

def readgroup(q):
    """
    <group> ::= <atom> |<atom><num> | (<mol>) <num>
    """

    if q.isEmpty():
        print("här tog det slut")

    elif q.peek().isalpha():
        readatom(q)
        if q.peek() is None:
            return
        
        if q.peek().isdigit():
            number(q)
        
        return
    elif q.peek() == "(":
        paranteser.append(q.dequeue())
        readmol(q)
    
    return 

def readatom(q):
    atom = ""
    if q.peek().isupper(): #ersätter uppercase()
        atom = q.dequeue()
    else:
        raise Syntax_error("Saknad stor bokstav vid radslutet ")

    if q.peek() != None:
        if q.peek().islower():
            atom += q.dequeue()

    if atom in atoms_lst:
        return
    else:
        raise Syntax_error("Okänd atom vid radslutet ")

def uppercase(q, molekyl): #används inte just nu
    if q.peek().isupper():
        temp = q.dequeue()
        lowercase(q, temp)
        return
    raise Syntax_error(f"Saknad stor bokstav vid radslutet {molekyl}") 

def lowercase(q, temp): #används typ inte nu heller
    if q.isEmpty() is False and q.peek().islower():
        q.dequeue()
    number(q)
        

def number(q): #behöver göras om
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

def main():

    while True:
        molecule_input = input("")
        if molecule_input == "#":
            break
        print(readformel(molecule_input))

main()
