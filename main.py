import os
from PyPDF2 import PdfFileMerger
import tkinter
from tkinter import filedialog

# Prevents an empty tkinter window from appearing
tkinter.Tk().withdraw() 
#Getting the path of selected files in an array
source_dir = filedialog.askopenfilenames(filetypes=[('PDF files', '*.pdf'),
                                                       ('JPG files', '*.jpg'),
                                                       ('PNG files', '*.png'),
                                                       ('all files', '.*')],
                                            initialdir=os.getcwd(),
                                            title="Select files", multiple=True) 
#Making merger object
merger =PdfFileMerger()

source_dir = list(source_dir)
#fixes tkinter issue: Bring first element to the last
source_dir.append(source_dir.pop(0))  
for item in source_dir:
    if item.endswith('pdf'):
        #appending all pdfs selections only
        merger.append(item) 
#writing the pdf of desired name specified by the user
merger.write(filedialog.asksaveasfilename())
merger.close()
