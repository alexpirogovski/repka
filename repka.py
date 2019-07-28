#!/usr/bin/env python

izba = ['Ded', 'grandma', 'girl', 'bitch', 'cat', 'mouse']
repka = ['repka']


def pull_repka(repka):
    shout = len(repka) - 1
    repka.append(izba[shout])
    print ', '.join([repka[repka.index(x) + 1] + ' za ' + x for x in reversed(repka)
                     if repka.index(x) != len(repka) - 1 and len(repka) != 0])
    if len(repka) == len(izba):
        print 'Repka is pulled'
    else:
        print 'Not enough power to pull the repka'
        print '{} shouts to {}'.format(izba[shout], izba[shout + 1])
        pull_repka(repka)


def main():
    print '=============== SKAZKA PRO REPKU ==============='
    print 'Posadil {} repku\nVyroskla repka bolshaya-prebolshaya\nStal {} tyanut repku:'.format(izba[0], izba[0])
    pull_repka(repka)
    print '===================== KONEC ===================='

if __name__ == "__main__":
    main()
