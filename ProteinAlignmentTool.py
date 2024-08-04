## last edited : 04-08-2024
## Sequence alignment tool for protein analysis

import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.screenName = "ProteinSequenceAligner1"
frm = ttk.Frame(root, padding=10)
frm.grid()

QuerySequence = StringVar()
ReferenceSequence = StringVar()

ttk.Label(frm, text="Protein Sequence Alignment Tool").grid(column=0, row=0, columnspan=2)
QuerySeq_label = Label(frm, text = "Query Sequence", font=('calibre', 10, 'bold'))
QuerySeq_input = Entry(frm, textvariable = QuerySequence, font=('calibre', 10, 'bold'))

QuerySeq_label.grid(column=0, row=1, sticky=W)
QuerySeq_input.grid(column=1, row=1)

ReferenceSeq_label = Label(frm, text = "Reference Sequence", font=('calibre', 10, 'bold'))
ReferenceSeq_input = Entry(frm, textvariable = ReferenceSequence, font=('calibre', 10, 'bold'))

ReferenceSeq_label.grid(column=0, row=2, sticky=W)
ReferenceSeq_input.grid(column=1, row=2)

Button(frm, text="Submit Alignment", command=root.destroy).grid(column=0, row=3, columnspan=1)

QuerySequence = StringVar()



print(sys.version)
print('hello world')

testSequence1 = "ARND"
testSequence2 = "RNDC"

def sequenceAlignment(seq_01, seq_02):
 
    maxSequenceSize = 10 

    if len(seq_01) <= maxSequenceSize and len(seq_02) <= maxSequenceSize:
        print('all good so far')
        ##continue with script, like normal

        sequenceList_1 = list(seq_01)
        sequenceList_2 = list(seq_02)

        print(sequenceList_1[0])
        print(sequenceList_2[1])

    else:
        print('sequence size is too big, please lower sequence length to less 10 or fewer amino acids')
        ## put sequence in a list


sequenceAlignment(testSequence1, testSequence2)
    #limit sequence input length to 10
    # store each sequence in a data holder like a list

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