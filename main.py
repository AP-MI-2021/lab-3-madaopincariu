def citire_lista():
    l=[]
    givenstring=input("Dati lista cu numerele separate prin vrigula:")
    numbersasstring=givenstring.split(",")
    for x in numbersasstring:
        l.append(int(x))
    return l

def nr_pare(l):
    '''
    Determina daca un numar este par
    :return: True daca x e par sau False daca x e impar
    :param l: o lista de numere
    '''
    for x in l:
        if x%2==0:
            return True
        else:
            return False

def test_nr_pare():
    assert nr_pare([12, 22, 34]) == True
    assert nr_pare([12, 24, 21]) == False

def get_longest_all_even(l):
    '''
    Determina ce ami lunga secventa de numere pare
    :param l: lista de elemente
    :return: subsecventa de numere pare
    '''
    rezultat = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if nr_pare(l[i:j + 1]) and len(l[i:j + 1]) > len(rezultat):
                rezultat = l[i:j + 1]

def test_get_longest_all_even():
    assert get_longest_all_even([2, 3, 4, 6])==[4, 6]
    assert get_longest_all_even([1,4,9,9])==[4]



def nr_prim(n):
    """
    Determina daca un numar este numar prim
        :param n: o valoare intreaga
        :return: True, daca n este prim, respectiv False in caz contrar
        """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_nr_prim():
    assert nr_prim(2) is True
    assert nr_prim(4) is False

def concat_num_din_lista(l):
    '''
    Concateneaza numerele din lista
    :param l: o lista de numere
    :return: True daca nr este prim sau False daca nr nu este prim
    '''
    if len(l)==0:
        return False
    nr=str(l[0])
    for i in range(1,len(l)):
        nr=nr+str(l[i])
    if nr_prim(int(nr)):
        return True
    return False

def test_concat_num_din_lista():
    assert concat_num_din_lista([1,2,3,4])==1234
    assert concat_num_din_lista([56,79,10])==567910

def get_longest_concat_is_prime(l):
    '''
    Determina cea mai lunga secventa din lista care prin concatenare rezulta un numar prin
    :param l: lista de numere
    :return: lista de numere
    '''
    rezultat=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if concat_num_din_lista(l[i:j+1]) and len(l[i:j+1])>len(rezultat):
                rezultat=l[i:j+1]
    return rezultat

def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([2, 1, 4, 6]) ==[2]

def is_palindrome(n):
    '''
    Determină dacă un număr dat este palindrom.
    :param n: un numar
    :return: True daca este palindrom sau False in caz contrar
    '''
    x=n
    inv=0
    while x!=0:
        c=x%10
        inv=inv*10+c
        x=x//10
    if inv==n:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(97) is False

def get_longest_all_palindromes(l):
    '''
    Determina ce mai lunga subsecventa a listei care contine doar numere de tip palindrom
    :param l: lista de numere
    :return: lista de numere
    '''
    rezultat = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if is_palindrome(l[i:j + 1]) and len(l[i:j + 1]) > len(rezultat):
                rezultat = l[i:j + 1]
    return rezultat

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121, 11, 343, 12]) == [121, 11, 343]
    assert get_longest_all_palindromes([45, 56, 3875, 1221])== [1221]

def main():
    l=[]
    test_nr_prim()
    test_get_longest_all_even()
    test_nr_pare()
    test_get_longest_concat_is_prime()
    test_concat_num_din_lista()
    test_is_palindrome()
    test_get_longest_all_palindromes()
    while True:
        print('1.Citire lista')
        print('2.Afiseaza cea mai lunga secventa de numere pare')
        print('3.Afiseaza cea mai lunga secventa care prin concatenare reprezinta un numar prim ')
        print('4.Afseaza cea mai lunga secventa in care toate numerele sunt palindroame')
        print('x.Iesire din program')
        opt = input('Alege optiunea: ')
        if opt=='1':
            l=citire_lista()
        elif opt == '2':
            l = input('Dati lista de numere:')
            print(get_longest_all_even(l))
        elif opt == '3':
            l =input('Dati lista de numere:')
            print(get_longest_concat_is_prime(l))
        elif opt=='4':
            l = input('Dati lista de numere:')
            print(get_longest_all_palindromes(l))
        elif opt == 'x':
            break
        else:
            print("optiune invalida")

main()