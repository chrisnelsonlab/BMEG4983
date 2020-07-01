# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:18:55 2020

@author: nelsonc

This script reads in a fasta file and finds returns all protospacers for a 
given PAM and protospacer length. Inputs are a fasta file, PAM, and 
protospacer length

There are three functions. 1.Creadfasta, 2. reversecomplement, 3. ispam
There are built in function that can take the place
of fasta read and reverse complement
"""

def Creadfasta(filename):
    #This function reads in a fasta file and outputs a header and a sequence
    #Also removes linebreaks
    fh = open(filename)
    header=fh.readline()
    header = header.replace('>','')
    
   
    seq = ''
    for line in fh:
        seq = seq+line
    seq = seq.replace('\n','')
    return header, seq

def ispam(seq,PAM):
    #This function decides if a given seq is a PAM. This should work for any
    #length of PAM. This takes into account generic nucleotide letters
    for x,char in enumerate(PAM):
        if char =='N':
            continue
        elif char =="A" and seq[x]=="A":
            continue
        elif char =="T" and seq[x]=="T":
            continue
        elif char =="C" and seq[x]=="C":
            continue
        elif char =="G" and seq[x]=="G":
            continue
        elif char =="R" and (seq[x]=="G" or seq[x]=="A"):
            continue
        elif char =="Y" and (seq[x]=="C" or seq[x]=="T"):
            continue
        elif char =="S" and (seq[x]=="G" or seq[x]=="C"):
            continue
        elif char =="W" and (seq[x]=="A" or seq[x]=="T"):
            continue           
        elif char =="K" and (seq[x]=="G" or seq[x]=="T"):
            continue
        elif char =="M" and (seq[x]=="A" or seq[x]=="C"):
            continue
        elif char =="B" and (seq[x]=="C" or seq[x]=="G" or seq[x]=="T"):
            continue
        elif char =="D" and (seq[x]=="A" or seq[x]=="G" or seq[x]=="T"):
            continue
        elif char =="H" and (seq[x]=="A" or seq[x]=="C" or seq[x]=="T"):
            continue
        elif char =="V" and (seq[x]=="A" or seq[x]=="C" or seq[x]=="G"):
            continue
        else:
            return False
    return True
    
def reversecomplement(seq):
    #This function returns a reverse complement of a sequence. Not designed
    #to be computationally efficient
    seq = seq.upper()
    seq = seq[::-1]
    seq = seq.replace("A", "t")
    seq = seq.replace("C", "g")
    seq = seq.replace("T", "a")
    seq = seq.replace("G", "c")
    seq = seq.upper()
    return seq
    

#Begin main
    
#Choose protospacer size. This could also be an input
protospacer_size = 20

#Choose PAM (3' PAMs only like SpCas9), This could also be an input
PAM = 'NGG'    

header,seq = Creadfasta('C:/Users/nelsonc/Desktop/PROGRAMMING/PYTHON/data/vegf.fa')
g = open('C:/Users/nelsonc/Desktop/PROGRAMMING/PYTHON/data/gRNA_output.txt', 'w') #OUTPUT with write permissions

#HEADER:
g.write("Protospacer\tPAM\tSense\tLocation\n")

#Check sense
for i in range(protospacer_size,len(seq)-len(PAM)):
    if(ispam(seq[i:i+len(PAM)],PAM)):
        print(i)
        print(seq[i:i+len(PAM)])
        print(seq[i-protospacer_size:i])
        g.write(seq[i-protospacer_size:i]+"\t"+seq[i:i+len(PAM)]+"\tSense\t"+str(i-protospacer_size+1)+"\n")

#Check reverse complement
RCseq = reversecomplement(seq)
fasize = len(seq)
for i in range(protospacer_size,len(RCseq)-len(PAM)):
    if(ispam(RCseq[i:i+len(PAM)],PAM)):
        print(i)
        print(RCseq[i:i+len(PAM)])
        print(RCseq[i-protospacer_size:i])
        g.write(RCseq[i-protospacer_size:i]+"\t"+RCseq[i:i+len(PAM)]+"\tAntiSense\t"+str(fasize-i+protospacer_size)+"\n")
g.close()




#Other ideas for improving the gRNA design?

#Removing poly_N (polyT)
#Removing extreme GC content (<20 >80)
#Refining the location?
#Off-targets?

