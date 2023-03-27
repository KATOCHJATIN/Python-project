import fontstyle
s=fontstyle.apply('🎀 ⋆. MATHS ⋆.  🎀'.center(450),'bold/italic/red/BLACK_BG')
print(s)
s=fontstyle.apply('''..................
topics:
....................'''.upper(),'bold/harlow solid Italic/blue/BLACK_BG')
print(s)
s=fontstyle.apply('    1.matrix'.upper(),'bold/harlow solid Italic/yellow/BLACK_BG')
print(s)
s=fontstyle.apply('    2.determinant'.upper(),'bold/harlow solid Italic/green/BLACK_BG')
print(s)
s=fontstyle.apply('select one topic'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
print(s)
s=fontstyle.apply('topic no : '.upper(),'bold/HARLOW SOLID italic/purple/BLACK_BG')
a=int(input(s))
while a==1 or a==2:
    if a==1:
        s=fontstyle.apply('there are two sub topic : '.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
        print(s)
        s=fontstyle.apply('1.addition'.upper(),'bold/HARLOW SOLID italic/yellow/BLACK_BG')
        print(s)
        s=fontstyle.apply('2.multiplication'.upper(),'bold/HARLOW SOLID italic/yellow/BLACK_BG')
        print(s)
        s=fontstyle.apply('sub topic = '.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
        t=int(input(s))
        if t==1:
              s=fontstyle.apply('addition'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
              print(s)
              ai=int(input('i r:'))
              aj=int(input('j c:'))
              bi=int(input('i r:'))
              bj=int(input('j c:'))
              if ai==aj:
                  s
                  a=[[ int(j) for i in range(bj) for j in input('Matrix a=' )]for x in range(ai)]
                  b=[[int(j) for i in range(bj) for j in input('Matrix b= ')]for x in range(bi)]
                  x=0
                  r=[[x for i in range(aj)]for j in range(ai)]
                  for i in range(len(a)):
                      for j in range(len(a[0])):
                          r[i][j]=a[i][j]+b[i][j]
                  s=fontstyle.apply('ans'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
                  print(r)
              else:
                  print('oder are not same')
        if t==2:
            s=fontstyle.apply('multiplication'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
            print(s)
            k=int(input('row a '.upper()))
            j=int(input('c of a '.upper()))
            m=int(input('row b '.upper()))
            n=int(input('c of b '.upper()))
            if j==m:
                a=[[int(j) for i in range(j) for j in input('a : ').split()] for x in range(k)]
                b=[[int(j) for i in range(n) for j in input('b :').split()] for x in range(m)]
                x=0
                r=[[x for i in range(n)] for j in range(k)]
                for i in range(len(a)):
                      for j in range(len(b[0])):
                            for k in range(len(b)):
                                      r[i][j] += a[i][k] * b[k][j]
                s=fontstyle.apply('ans'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
                print(s,r)  
            else:
              print('the order does nt math the condition'.upper())
            if a==2:
                pass
                
    a=int(input('topic = '.upper()))
import fontstyle
s=fontstyle.apply('🎀 ⋆. MATHS ⋆.  🎀'.center(450),'bold/italic/red/BLACK_BG')
print(s)
s=fontstyle.apply('''..................
topics:
....................'''.upper(),'bold/harlow solid Italic/blue/BLACK_BG')
print(s)
s=fontstyle.apply('    1.matrix'.upper(),'bold/harlow solid Italic/yellow/BLACK_BG')
print(s)
s=fontstyle.apply('    2.determinant'.upper(),'bold/harlow solid Italic/green/BLACK_BG')
print(s)
s=fontstyle.apply('select one topic'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
print(s)
s=fontstyle.apply('topic no : '.upper(),'bold/HARLOW SOLID italic/purple/BLACK_BG')
a=int(input(s))
while a==1 or a==2:
    if a==1:
        s=fontstyle.apply('there are two sub topic : '.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
        print(s)
        s=fontstyle.apply('1.addition'.upper(),'bold/HARLOW SOLID italic/yellow/BLACK_BG')
        print(s)
        s=fontstyle.apply('2.multiplication'.upper(),'bold/HARLOW SOLID italic/yellow/BLACK_BG')
        print(s)
        s=fontstyle.apply('sub topic = '.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
        t=int(input(s))
        if t==1:
              s=fontstyle.apply('addition'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
              print(s)
              ai=int(input('i r:'))
              aj=int(input('j c:'))
              bi=int(input('i r:'))
              bj=int(input('j c:'))
              if ai==aj:
                  s
                  a=[[ int(j) for i in range(bj) for j in input('Matrix a=' )]for x in range(ai)]
                  b=[[int(j) for i in range(bj) for j in input('Matrix b= ')]for x in range(bi)]
                  x=0
                  r=[[x for i in range(aj)]for j in range(ai)]
                  for i in range(len(a)):
                      for j in range(len(a[0])):
                          r[i][j]=a[i][j]+b[i][j]
                  s=fontstyle.apply('ans'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
                  print(r)
              else:
                  print('oder are not same')
        if t==2:
            s=fontstyle.apply('multiplication'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
            print(s)
            k=int(input('row a '.upper()))
            j=int(input('c of a '.upper()))
            m=int(input('row b '.upper()))
            n=int(input('c of b '.upper()))
            if j==m:
                a=[[int(j) for i in range(j) for j in input('a : ').split()] for x in range(k)]
                b=[[int(j) for i in range(n) for j in input('b :').split()] for x in range(m)]
                x=0
                r=[[x for i in range(n)] for j in range(k)]
                for i in range(len(a)):
                      for j in range(len(b[0])):
                            for k in range(len(b)):
                                      r[i][j] += a[i][k] * b[k][j]
                s=fontstyle.apply('ans'.upper(),'bold/HARLOW SOLID italic/cyan/BLACK_BG')
                print(s,r)  
            else:
              print('the order does nt math the condition'.upper())
            if a==2:
                pass
                
    a=int(input('topic = '.upper()))
    k=int(input('row a '.upper()))
    
    j=int(input('c of a '.upper()))
    m=int(input('row b '.upper()))
    n=int(input('c of b '.upper()))
    if j==m:
        a=[[int(j) for i in range(j) for j in input('a : ').split()] for x in range(k)]
        b=[[int(j) for i in range(n) for j in input('b :').split()] for x in range(m)]
        x=0
        r=[[x for i in range(n)] for j in range(k)]
        # iterating by row of A
        for i in range(len(a)):
    
        # iterating by column by B
            for j in range(len(b[0])):
    
            # iterating by rows of B
                for k in range(len(b)):
                    r[i][j] = a[i][k] * b[k][j]
            print(r)
                
    else:
        print('the order does nt math the condition'.upper())
