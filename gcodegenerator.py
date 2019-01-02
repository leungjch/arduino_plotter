from PIL import Image
from numpy import*

temp=Image.open('mac.png')
size = 32,32
temp.thumbnail(size, Image.ANTIALIAS)
temp = temp.convert('1')
temp.save('new.jpg', "PNG")

A = array(temp)             # Creates an array, white pixels==True and black pixels==False
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j]=0
        else:
            new_A[i][j]=1

savetxt("gcode.txt", new_A, delimiter=',',newline=',2,', fmt="%i")
