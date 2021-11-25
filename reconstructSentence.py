#reconstructSentence.py
#created by Jenna Hebert 
#program takes two command line arguments
#the two command line arguments should be input file names 
# these files are read into the code, and then reversed and alternate words are read
#the output is contained in file "output.txt"
#If the contents of input files are:
#input1.txt: Molloy. by Second Embedded Building Techniques Tools Exploring the site the This
#input2.txt: Derek Edition Linux with for and BeagleBone: book for companion is
#Then, the output file output.txt will contain:
#This is the companion site for the book Exploring BeagleBone: Tools and Techniques for Building with Embedded Linux Second Edition by Derek Molloy
import sys
if len(sys.argv) != 3:
    print('Program takes two command line arguments. Please call the program with two text file names')
    quit()
input1=sys.argv[1]
file1=open(input1, 'r');
text1=file1.read()
#print(text1)
input2=sys.argv[2]
file2=open(input2, 'r');
text2=file2.read()
#print(text2)

text1=text1.split()
print('list1 is: '+str(text1))
length1=len(text1)
print('length of list1 is: '+str(length1))

text2=text2.split()
print('list2 is: '+str(text2))
length2=len(text2)
print('length of list2 is: '+str(length2))

out=[]
i=length1*-1
j=length2*-1
m=j
n=i
k=0
#if it is an odd number, it will print the next last element from the first list
#else, it will do the same for the second list
#if the input strings are mismatched, a blank space will be printed 
for k in range(0,length1+length2):
    if (k % 2 != 0): #odd number
        if (m in range(-1,j-1,-1)):
		out.insert(0,text2[m])
		m+=1
	else:
		out.insert(0,' ')
    else:
        if (n in range(-1,i-1,-1)):
            #print(text1[n])
            out.insert(0,text1[n])
            n+=1
        else:
            out.insert(0,' ')
    k+=1
#print(out)
fileout = open("output.txt", "w")
k=0
for k in range(0,length1+length2):
    fileout.write(out[k])
    fileout.write(' ')
