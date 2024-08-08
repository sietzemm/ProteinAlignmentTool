## last edited : 08-08-2024
## Sequence alignment tool for protein analysis

import sys
from tkinter import *
from tkinter import ttk

print(sys.version)

root = Tk()
root.screenName = "ProteinSequenceAligner1"
frame = ttk.Frame(root, padding=10)
frame.grid(padx=50)

# GLOBAL VARIABLES

# set containing all one letter abbreviations for the 20 amino acids,
aminoAcids_lib = {'A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V'}
QuerySequence = StringVar()
ReferenceSequence = StringVar()
maxSequenceSize = 250 ## Maximal sequence length user can provide
globalAlignmentScore = StringVar()
globalAlignmentScore.set('0')
globalErrorMsg = StringVar()
foundMismatches = [] #this list will house tuples containing [location,mismatch]

## GUI 
ttk.Label(frame, text="Protein Sequence Alignment Tool", font=('calibre', 14)).grid(column=0, row=0, columnspan=1)
QuerySeq_label = Label(frame, text = "Query Sequence", font=('calibre', 10, 'bold'))
QuerySeq_label.grid(column=0, row=1, sticky=W)

QuerySeq_input = Entry(frame, textvariable = QuerySequence, font=('calibre', 10, 'bold'),width=75)
QuerySeq_input.grid(column=1, row=1)

ReferenceSeq_label = Label(frame, text = "Reference Sequence", font=('calibre', 10, 'bold'))
ReferenceSeq_label.grid(column=0, row=2, sticky=W)

ReferenceSeq_input = Entry(frame, textvariable = ReferenceSequence, font=('calibre', 10, 'bold'), width=75)
ReferenceSeq_input.grid(column=1, row=2)

alignmentScoreTxt_label = Label(frame, text = 'Match percentage : ', font=('calibre', 10, 'bold'))
alignmentScoreTxt_label.grid(column=0, row=3, sticky=W)

alignmentScoreValue = Label(frame, textvariable=globalAlignmentScore, font=('calibre', 10, 'bold'))
alignmentScoreValue.grid(column=1, row=3, sticky=W)

# Does input checks prior to alignment
def checkInput(queryList, referenceList,):

    #Check if there even is a sequence provided by the user
    if len(queryList) == 0 or len(referenceList) == 0:
        if len(queryList) == 0 and len(referenceList) == 0:
            globalErrorMsg.set("ERROR: Both query and reference sequences are empty!")
        elif len(queryList) == 0:
            globalErrorMsg.set("ERROR: Query sequence is empty!")
        elif len(referenceList) == 0:
            globalErrorMsg.set("ERROR: Reference sequence is empty!")
        return False
    
    #Checks if the provided sequence length does not exceed set sequence length
    if len(queryList) <= maxSequenceSize and len(referenceList) <= maxSequenceSize:
        print('all good')

    else:
        print(f'sequence size is too big, please lower sequence length to less {maxSequenceSize} or fewer amino acids')
        globalErrorMsg.set(f"ERRROR : query length exceeds maximum query length : {maxSequenceSize}")
        return False
    
    #Checks the provided query and reference sequences contain valid one-letter amino acid codes
    for i, x in enumerate(queryList):
        x = x.upper()
        if x not in aminoAcids_lib:
            globalErrorMsg.set('invalid amino acid on location : '+str(i+1)+' with unkown value of : '+str(x))
            print(f'ERROR : The input sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
            return False
        else:
            continue

    for i, x in enumerate(referenceList):
        x = x.upper()
        if x not in aminoAcids_lib:
            try:
                globalErrorMsg.set('invalid amino acid on location : '+str(i+1)+' with unkown value of : '+str(x))
                print(f'ERROR : The reference sequence you provided contains a invalid amino acid on location : {i}', 'with unkown value of :', x)
                return False
            except ValueError:
                pass

    return True

def execAlignment(querySeq, referenceSeq):
    
    print('inside execAlignment')
    localScore = 0
   
   # Convert sequences to uppercase
    querySeq = [x.upper() for x in querySeq]
    referenceSeq = [y.upper() for y in referenceSeq]
    
    # Initialize colored sequences
    coloredQuerySeq = []
    coloredReferenceSeq = []

    #global alignment
    print('executing alignment of sequences')
    for i, (x, y) in enumerate(zip(querySeq, referenceSeq)):

        if x == y:
            localScore += 1
            coloredQuerySeq.append((x, 'green'))
            coloredReferenceSeq.append((y, 'green'))
            print('Local match! [', x, y, '] local score now:', localScore, 'index:', i)
        else:
            foundMismatches.append((i,(x,y)))
            coloredQuerySeq.append((x, 'red'))
            coloredReferenceSeq.append((y, 'red'))
            print('No match!', x, y)
            #change color to red
    
    match_percentage = (localScore / len(querySeq)) * 100
    globalAlignmentScore.set(f'{match_percentage:.2f}')
    print(globalAlignmentScore.get())
    root.update_idletasks()
    
    return (coloredQuerySeq, coloredReferenceSeq)

def errorMsgPopUp():

    top = Toplevel(root)
    top.geometry("450x55")
    top.title("ERROR MESSAGE ")
    Label(top, text=globalErrorMsg.get(), font=('calibre', 10, 'bold'), fg='red').grid(column=0, row=0, padx=10, sticky=W)
    Button(top, text="close", command=top.destroy).grid(column=0,row=2, sticky=W)

def alignmentResultPopUp(alignmentresults):

    top = Toplevel(root)
    top.geometry("750x250")
    top.title("AlIGNMENT RESULT")
    Label(top, text='Alignment result', font=('calibre', 14, 'bold')).grid(column=0, row=0, padx=5, pady=5)

    #display important findings
    # Display mismatches
    Label(top, text="Mismatches: ", font=('calibre', 10, 'bold')).grid(column=0, row=1, sticky=W, padx=5)
    Label(top, text=str(len(foundMismatches)), font=('calibre', 10, 'bold')).grid(column=1, row=1)
    
    # Create Text widgets for displaying sequences
    queryText = Text(top, wrap=NONE, height=1, width=75)
    queryText.grid(column=0, row=2, padx=5, pady=2)
    
    referenceText = Text(top, wrap=NONE, height=1, width=75)
    referenceText.grid(column=0, row=3, padx=5, pady=2)

    # Define tags for colors
    queryText.tag_configure('green', foreground='green')
    queryText.tag_configure('red', foreground='red')
    
    referenceText.tag_configure('green', foreground='green')
    referenceText.tag_configure('red', foreground='red')

    # Insert the sequences with color tags
    for char, color in alignmentresults[0]:
        queryText.insert(END, char, color)
    
    for char, color in alignmentresults[1]:
        referenceText.insert(END, char, color)

    # Label(top, text="gaps : ",font=('calibre', 10, 'bold')).grid(column=2, row=1)
    # Label(top, text="0 : ",font=('calibre', 10, 'bold')).grid(column=3, row=1)
    
    # Label(top, text="dels : ",font=('calibre', 10, 'bold')).grid(column=4, row=1)
    # Label(top, text="0 : ",font=('calibre', 10, 'bold')).grid(column=5, row=1)
    
    # Label(top, text=alignmentresults[0], font=('calibre', 10, 'bold')).grid(column=0, row=2)
    # Label(top, text='||||', font=('calibre', 10, 'bold')).grid(column=0, row=3)
    # Label(top, text=alignmentresults[1], font=('calibre', 10, 'bold')).grid(column=0, row=4)
    
     # Make Text widgets read-only
    queryText.config(state=DISABLED)
    referenceText.config(state=DISABLED)
    
    Button(top, text="Close", command=top.destroy).grid(column=0, row=4, pady=10, sticky=W)
    Button(top, text="Export", command=top.destroy).grid(column=1, row=4, pady=10)
def BTNsubmitQuery():
    
    # on button click, get user input data    
    QuerySequenceSubmit = QuerySequence.get()
    ReferenceSequenceSubmit = ReferenceSequence.get()

    # Make a list of both sequences
    queryList = list(QuerySequenceSubmit)
    referenceList = list(ReferenceSequenceSubmit)
   
    # user input can now be checked for mistakes
    if checkInput(queryList, referenceList) == True:
        
        alignmentResultPopUp(execAlignment(queryList, referenceList))
        alignmentScoreValue = Label(frame, text = globalAlignmentScore.get(), font=('calibre', 10, 'bold'))
        foundMismatches.clear()
        root.update_idletasks()
    else : # there must be a error, show error pop up window
         errorMsgPopUp()

Button(frame, text="Submit Alignment", command= BTNsubmitQuery).grid(column=0, row=4, sticky=W)
footerTextLbl = Label(frame, text='version 1.0, by Sietze Min', font=('calibre', 10,))
footerTextLbl.grid(column=0, row=5, pady=(75,0), sticky=W)

root.mainloop()

# Functionalities to add 
# Needleman-Wunsch alignment algorithm / BLOSUM62
# gap / indel identification
# mismatch
# motif ?
# multiple sequence alignment
# secondary protein structure prediction
# Make mismatches appear red in the output window
# Convert protein to nt sequence / vice versa