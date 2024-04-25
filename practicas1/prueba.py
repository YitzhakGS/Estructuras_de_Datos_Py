x = input()

def validar(x):
    if x.isdigit():
        return True
    else:
        return False
    
print(validar(x))