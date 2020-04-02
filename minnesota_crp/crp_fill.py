import os
import pdfrw


INVOICE_TEMPLATE_PATH = 'crp_template.pdf'
INVOICE_OUTPUT_PATH = 'crp_completed.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


data_dict = {
   'Renterfirstnameandinitial': 'Jane',
   'Renterlastname': 'Doe',
   'ECN': '11111111111',
   'unitaddress': '1111 address street',
   'unit': 'unit 1',
   'rentercity': 'Cityville',
   'renterstate': 'IL',
   'renterzip': '00000',
   'rentercounty': 'Cook',
   'RentedfromMMDDYYYY': '11/11/11',
   'toMMDDYYYY': '12/12/12',
   'TotalMonthsRented': '9',
   'NumberofAdultsLivinginUnit': '22',
   # Place an 'X' for one of the following 6 options.
   'AdultFosterCare': '',
   'AssistedLiving': 'X',
   'IntermediateCareFacility': '',
   'NursingHome': '',
   'MobileHome': '',
   'MobileHomeLot': '',
   'propertyidorparcel': 'NA',
   'numberofunits': '1',
   #Was any rent paid by medical assistance (Medicaid)? Y/N.
   'medicaidyes': 'X',
   'medicaidno': '',
   'A': '$1,000',
   'B': '',
   '1': '10000',
   '2': '',
   '3': '10000',
   'PropertyOwnername': 'Property Holdings',
   'propertyownerDaytimePhone': '777-777-7777',
   'PropertyOwnerAddress': '1 west Property Holdings Dr.',
   'City': 'Chicago',
    'State': 'IL',
    'ZIPcode': '77777',
    'Signaturedate': '3/13/12',
    'MangingAgentNameIfApplicablepleaseprint': 'NA',
    'DaytimePhone': '555-555-5555'

}

if __name__ == '__main__':
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)