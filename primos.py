def multiplo(n, i):
    if (n % i) == 0:
        return True
    else:
        return False



def primo(n):
    if n < 2:
        return False
    status = True
    for i in range(2,n):
        if multiplo(n, i):
            status = False
    return status

for i in range(100):
    if primo(i):
        print(i)
        
