import PyPDF2
def pdf_to_text(pdf_path, output_text):
    #open the pdf file in read binary mode
    with open(pdf_path, 'rb') as pdf_file:
        #created a pdf reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        #Initializing an empty string to store the extracted text from the pdf
        text = ""
        len_pdf = len(pdf_reader.pages)

        for page_num in range(len_pdf):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
 
    #write the extracted text in txt file 
    with open(output_text, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


if __name__ == "__main__":
    pdf_path = 'xyz.pdf'
    output_text = 'xyz.txt'
    pdf_to_text(pdf_path, output_text)
    print("Pdf converted to text successfully.")