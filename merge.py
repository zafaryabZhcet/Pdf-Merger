import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs_in_directory(directory_path, output_filename):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    pdf_files.sort()

    for pdf in pdf_files:
        with open(os.path.join(directory_path, pdf), 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

def merge_pdfs():
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return
    output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_filename:
        return
    merge_pdfs_in_directory(folder_selected, output_filename)
    messagebox.showinfo("Success", "PDFs merged successfully!")

root = tk.Tk()
root.title("PDF Merger")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="PDF Merger Tool", font=('Arial', 16))
label.pack(pady=20)

merge_btn = tk.Button(frame, text="Merge PDFs", command=merge_pdfs, width=15, height=2)
merge_btn.pack(pady=20)

root.mainloop()
