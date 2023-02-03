def primo(num):
    print('-'*50)
    print('Verificador de números primo')
    
    if num / 2 != 0:
        print('Este número é primo.')
    elif num / 3 != 0:
        print('Este número é primo.')
    elif num / 5 != 0:
        print('Este número é primo.')
    elif num / 7 != 0:
        print('Este número é primo.')
    else: 
        print('Este número não é primo.')
    return '-'*50

num = int(input('Digite um número: '))
print(primo(num))
    