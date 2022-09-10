import os
from PyPDF2 import PdfFileMerger

pdfs = ['01.pdf', '02.pdf','03.pdf','04.pdf','05.pdf','06.pdf','1.pdf', '2.pdf','3.pdf','4.pdf','5.pdf','6.pdf','7.pdf','8.pdf', '9.pdf','10.pdf', '11.pdf', '12.pdf','13.pdf','14.pdf','15.pdf','16.pdf','17.pdf','18.pdf', '19.pdf','20.pdf', '21.pdf', '22.pdf','23.pdf','24.pdf','25.pdf','26.pdf','27.pdf','28.pdf', '29.pdf', '30.pdf', '31.pdf', '32.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()