import PyPDF2
from pathlib import Path

class PDF_Converter:
  def combine(filename):
    pdf_dir = Path("./raw")
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for i in range(pdf_reader.getNumPages()):
          pdf_writer.addPage(pdf_reader.getPage(i))
    with open(f"./done/{filename}.pdf", "wb") as f:
        pdf_writer.write(f)
    return "done"
  def split():
    pdf_dir = Path("./raw")
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    for pdf_file in pdf_files:
      pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
      num_pages = pdf_reader.getNumPages()
      digits = len(str(num_pages))  
      fpad = '{0:0' + str(digits) + 'd}'  
      for i in range(num_pages):
          page = pdf_reader.getPage(i) 
          pdf_writer = PyPDF2.PdfFileWriter() 
          pdf_writer.addPage(page) 
          filename = str(pdf_file).replace(".pdf","").split("/")[0]
          with open(f"./done/{i}-{filename}.pdf", "wb") as f:
              pdf_writer.write(f)  
    return "done"
