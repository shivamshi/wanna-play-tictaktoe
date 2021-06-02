#always start with X

def display(l):                      #function to print matrix
    for i in l:
        print('[',end='')
        for j in i:
            print(j,end='')
        print(']\n')
        
def check(a):                        #function to check who wins
    for i in range(0,3):
        if l[i][0]==l[i][1]==l[i][2]==a or l[0][i]==l[1][i]==l[2][i]==a: 
            return True
    if l[0][0]==l[1][1]==l[2][2]==a or l[0][2]==l[1][1]==l[2][0]==a:
        return True
    else: return False
    
l=[['_','_','_'],['_','_','_'],['_','_','_']]

display(l)

for i in range(1,10):
    n=int(input('enter a position : '))
    if i%2==1: l[(n-1)//3][n%3 -1]='x'
    if i%2==0: l[(n-1)//3][n%3 -1]='o'
    display(l)
    if check('x'):
        print('x win')
        i=10
        break
    elif check('o'):
        print('o win')
        i=10
        break
if i<10: print('draw')
