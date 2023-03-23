def get_note(c):
    while c != False or c != True:
        try:
            a = ()
            while a != False or a != True:
                a = input('Введите ноту: \n')
                b = int(input('Введите нормер нотации октавы: \n'))
                if a.upper() == "C":
                    Hz = 261.63 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "D":
                    Hz = 293.66 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "E":
                    Hz = 329.63 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "F":
                    Hz = 349.23 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "G":
                    Hz = 392.00 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "A":
                    Hz = 440.00 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                elif a.upper() == "B":
                    Hz = 493.88 / (2 ** (4 - b))
                    print(' Частота %s = %.2f Hz' % (a.upper(), Hz))
                else:
                    print(" Note isn't exists")
        except ValueError:
            print('Better enter number')
