"Doc adapter"

import docx2txt

def docx_to_pages(file):
	"extract text from Word file"
	pages = []
	pages = docx2txt.process(file)
	return pages