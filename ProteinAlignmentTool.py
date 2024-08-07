## last edited : 07-08-2024
## Sequence alignment tool for protein analysis

import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.screenName = "ProteinSequenceAligner1"
frame = ttk.Frame(root, padding=10)
frame.grid()

# GLOBAL VARIABLES

# set containing all one letter abbreviations for the 20 amino acids,
aminoAcids_lib = {'A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V'}
testSequence1 = "aRNDz"
testSequence2 = "RNDCz"
QuerySequence = StringVar()
ReferenceSequence = StringVar()

ttk.Label(frame, text="Protein Sequence Alignment Tool").grid(column=0, row=0, columnspan=1)
QuerySeq_label = Label(frame, text = "Query Sequence", font=('calibre', 10, 'bold'))
QuerySeq_input = Entry(frame, textvariable = QuerySequence, font=('calibre', 10, 'bold'))

QuerySeq_label.grid(column=0, row=1, sticky=W)
QuerySeq_input.grid(column=1, row=1)

ReferenceSeq_label = Label(frame, text = "Reference Sequence", font=('calibre', 10, 'bold'))
ReferenceSeq_input = Entry(frame, textvariable = ReferenceSequence, font=('calibre', 10, 'bold'))

ReferenceSeq_label.grid(column=0, row=2, sticky=W)
ReferenceSeq_input.grid(column=1, row=2)

## Placeholder function for displaying of error messages
def open_popup():
    top = Toplevel(root)
    top.geometry("250x250")
    top.title("ERROR MESSAGE")
    Label(top, text="pop up text", font=('calibre', 10, 'bold')).grid(column=0, row=0)

print(sys.version)

def checkInput(QuerySequence, ReferenceSequence):
    
    queryList = list(QuerySequence)
    referenceList = list(ReferenceSequence)
    maxSequenceSize = 10 ## Maximal sequence length

    if len(queryList) <= maxSequenceSize and len(referenceList) <= maxSequenceSize:
        print('all good')
        ##continue with script, like normal

    else:
        print('sequence size is too big, please lower sequence length to less 10 or fewer amino acids')
        ## put sequence in a list

    # check if the characters of the input sequences are a valid one letter protein codes
    
    for i, x in enumerate(queryList):
        x = x.upper()
        if x not in aminoAcids_lib:
            print(f'ERROR : The input sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
        else:
            continue

    for i, x in enumerate(referenceList):
        x = x.upper()
        if x not in aminoAcids_lib:
            try:
                print(f'ERROR : The reference sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
            except ValueError:
                pass

def BTNsubmitQuery():
    top = Toplevel(root)
    top.geometry("250x250")
    top.title("INPUT PROVIDED")
    
    QuerySequenceSubmit = QuerySequence.get()
    ReferenceSequenceSubmit = ReferenceSequence.get()
    
   # print('submitted query Sequence : ' + str(QuerySequenceSubmit))
    #print('provided reference sequence : ' + ReferenceSequence)

    Label(top, text=QuerySequenceSubmit, font=('calibre', 10, 'bold')).grid(column=0, row=0)
    Label(top, text=ReferenceSequenceSubmit, font=('calibre', 10, 'bold')).grid(column=0, row=2)

    checkInput(QuerySequenceSubmit, ReferenceSequenceSubmit)


Button(frame, text="Submit Alignment", command= BTNsubmitQuery).grid(column=0, row=3, columnspan=1)

root.mainloop()

# Alanine = A
# Arginine = R
# Asparagine = N
# Aspartic acid = D
# Cysteine = c
# Glutamic acid = E
# Glutamine = Q
# Glycine = G
# Histidine = H
# Isoleucine = I
# Leucine = L
# Lysine = K
# Methionin = M
# Phenylalanine = F
# Proline = P
# Serine = S
# Threonine = T
# Tryptophan = W
# Tyrosine = Y
# Valine = V