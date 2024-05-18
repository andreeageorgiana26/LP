import re
from pdfminer.high_level import extract_text
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

text = extract_text("balena.pdf") #extrage textul din pdf

paragrafe= text.split('\n\n') #impartirea textului

pattern_este = re.compile(r'\beste\b', re.IGNORECASE) #gasirea cuvantului este
pattern_pe = re.compile(r'\bpe\b', re.IGNORECASE)

paragrafe_este = [] #selecteaza paragrafele care contin cuvantul "este" de cel

paragrafe_pe_2 = []# putin doua ori si determina numarul de aparitii

for paragraf in paragrafe:
    numar_este= len(pattern_este.findall(paragraf))
    if numar_este>= 2:
        numar_pe=len(pattern_pe.findall(paragraf))
        paragrafe_este.append((paragraf, numar_pe))
        if numar_pe==2:
            paragrafe_pe_2.append(paragraf)



def save_to_pdf(paragrafe, filename): # functie pt salvarea unui nou fisier pdf cu textul cerut
    c=canvas.Canvas(filename,pagesize=letter)
    width, height = letter
    text_object= c.beginText(40, height - 40)
    text_object.setFont("Helvetica", 12)

    for paragraf in paragrafe:
        text_object.textLines(paragraf)
        text_object.moveCursor(0, 20)
    c.drawText(text_object)
    c.showPage()
    c.save()

save_to_pdf(paragrafe_pe_2,"Paragrafe_unde_cuvantul_pe_apare_de_doua_ori.pdf")
#Salvarea paragraf. ce contin cuvantul "pe" de exact doua ori in noul fisier pdf
for paragraf, numar_pe in paragrafe_este:
    print(paragraf)
    print(f"\nNumarul aparitiilor cuvantului 'pe' : {numar_pe}")
    print("\n---\n")
    print("Paragrafele cerute au fost salvate in 'Paragrafe_unde_cuvantul_pe_apare_de_doua_ori.pdf")
#afisarea paragrafelor ce contin "este" de cel putin doua ori si numarul aparitiilor cuv. "pe"


    #Sursele de inspiratie:
    #https://www.datasciencelearner.com/data-preprocessing/top-5-python-pdf-library-know-data-scientist/
    #https://dzone.com/articles/exporting-data-from-pdfs-with-python
    #https://www.youtube.com/watch?v=RULkvM7AdzY
    #https://www.youtube.com/watch?v=dL7vDCtynaM
    #https://reintech.io/blog/how-to-create-pdfs-with-python