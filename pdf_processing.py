import pdfrw


class ProcessPdf:
    def __init__(self, input_file):
        self.input_file = input_file

    def print_annotaion_keys(self):
        template = pdfrw.PdfReader(self.input_file)

        for page in template.pages:
            annotations = page['/Annots']
            if annotations is None:
                continue

            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        key = annotation['/T'][1:-1]

                        print(key)

    def add_data_to_pdf(self, data, output_file):
        template = pdfrw.PdfReader(self.input_file)

        for page in template.pages:
            annotations = page['/Annots']
            if annotations is None:
                continue

            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        key = annotation['/T'][1:-1]

                        if key in data:
                            annotation.update(pdfrw.PdfDict(V=_encode_pdf_string(data[key])))
                        annotation.update(pdfrw.PdfDict(Ff=1))

        template.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        pdfrw.PdfWriter().write(output_file, template)


def _encode_pdf_string(value):
    if value:
        return pdfrw.objects.pdfstring.PdfString.encode(str(value))
    else:
        return pdfrw.objects.pdfstring.PdfString.encode('')
