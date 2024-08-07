## last edited : 07-08-2024
## Sequence alignment tool for protein analysis

import sys
from tkinter import *
from tkinter import ttk

print(sys.version)

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
maxSequenceSize = 10 ## Maximal sequence length user can provide
globalAlignmentScore = StringVar()
globalAlignmentScore.set('0')
globalErrorMsg = StringVar()

## GUI 
ttk.Label(frame, text="Protein Sequence Alignment Tool", font=('calibre', 14)).grid(column=0, row=0, columnspan=1)
QuerySeq_label = Label(frame, text = "Query Sequence", font=('calibre', 10, 'bold'))
QuerySeq_label.grid(column=0, row=1, sticky=W)

QuerySeq_input = Entry(frame, textvariable = QuerySequence, font=('calibre', 10, 'bold'))
QuerySeq_input.grid(column=1, row=1)

ReferenceSeq_label = Label(frame, text = "Reference Sequence", font=('calibre', 10, 'bold'))
ReferenceSeq_label.grid(column=0, row=2, sticky=W)

ReferenceSeq_input = Entry(frame, textvariable = ReferenceSequence, font=('calibre', 10, 'bold'))
ReferenceSeq_input.grid(column=1, row=2)

alignmentScoreTxt_label = Label(frame, text = 'Match percentage : ', font=('calibre', 10, 'bold'))
alignmentScoreTxt_label.grid(column=0, row=3, sticky=W)

alignmentScoreValue = Label(frame, textvariable=globalAlignmentScore, font=('calibre', 10, 'bold'))
alignmentScoreValue.grid(column=1, row=3, sticky=W)

# Does input checks prior to alignment
def checkInput(queryList, referenceList,):

    #Check if there even is a sequence provided by the user
    if len(queryList) == 0 or len(referenceList) == 0: 
        globalErrorMsg.set("ERRROR : Query and/or refference sequence are empty!")
        return False
    
    #Checks if the provided sequence length does not exceed set sequence length
    if len(queryList) <= maxSequenceSize and len(referenceList) <= maxSequenceSize:
        print('all good')

    else:
        print('sequence size is too big, please lower sequence length to less 10 or fewer amino acids')
        return False
    
    #Checks the provided query and reference sequences contain valid one-letter amino acid codes
    for i, x in enumerate(queryList):
        x = x.upper()
        if x not in aminoAcids_lib:
            print(f'ERROR : The input sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
            return False
        else:
            continue

    for i, x in enumerate(referenceList):
        x = x.upper()
        if x not in aminoAcids_lib:
            try:
                print(f'ERROR : The reference sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
                return False
            except ValueError:
                pass

    return True

def execAlignment(querySeq, referenceSeq):
    print('inside execAlignment')
    localScore = 0
   
    #global alignment
    print('executing alignment of sequences')
    for i, (x, y) in enumerate(zip(querySeq, referenceSeq)):
        if x == y:
            localScore += 1
            print('Local match! [', x, y, '] local score now:', localScore, 'index:', i)
        else:
            print('No match!', x, y)
    
    match_percentage = (localScore / len(querySeq)) * 100
    globalAlignmentScore.set(f'{match_percentage:.2f}')
    print(globalAlignmentScore.get())
    root.update_idletasks()

def BTNsubmitQuery():
    errorMSG = StringVar()
    top = Toplevel(root)
    top.geometry("750x250")
    top.title("INPUT PROVIDED")
    
    QuerySequenceSubmit = QuerySequence.get()
    ReferenceSequenceSubmit = ReferenceSequence.get()

    queryList = list(QuerySequenceSubmit)
    referenceList = list(ReferenceSequenceSubmit)
   
    if checkInput(queryList, referenceList) == True:
        execAlignment(queryList, referenceList)
        Label(top, text=QuerySequenceSubmit, font=('calibre', 10, 'bold')).grid(column=0, row=0)
        Label(top, text='||||', font=('calibre', 10, 'bold')).grid(column=0, row=1)
        Label(top, text=ReferenceSequenceSubmit, font=('calibre', 10, 'bold')).grid(column=0, row=3)
        alignmentScoreValue = Label(frame, text = globalAlignmentScore.get(), font=('calibre', 10, 'bold'))
      
    else : 
         Label(top, text=globalErrorMsg.get(), font=('calibre', 10, 'bold'), fg='red').grid(column=0, row=0, columnspan=2, padx=10, sticky=W)



Button(frame, text="Submit Alignment", command= BTNsubmitQuery).grid(column=0, row=4, sticky=W)

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

# Functionalities to add 
# Needleman-Wunsch alignment algorithm / BLOSUM62
# gap / indel identification
# mismatch
# multiple sequence alignment
# secondary protein structure prediction
# Make mismatches appear red in the output window