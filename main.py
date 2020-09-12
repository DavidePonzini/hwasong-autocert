import pdf_processing
from datetime import date


INPUT_PATH = './Autocertificazione COVID19.pdf'
OUTPUT_PATH = 'D:/Desktop/'


def fill_cert_minorenne(nome, natoa, prov_nascita, data_nascita_d, data_nascita_m, data_nascita_y,
                        residenza, prov_residenza, indirizzo_residenza, tel, mail,
                        minore_nome, minore_natoa, minore_prov_nascita,
                        minore_data_nascita_d, minore_data_nascita_m, minore_data_nascita_y,
                        minore_residenza, minore_prov_residenza,
                        covid_tampone1='', covid_tampone2='', covid_fine='',
                        giorno=date.today().day, mese=date.today().month, anno=date.today().year):
    data = {
        'sottoscrittoa': nome,
        'natoa': natoa,
        'prov': prov_nascita,
        'l': '{:02}/{:02}/{:04}'.format(data_nascita_d, data_nascita_m, data_nascita_y),
        'n': residenza,
        'prov_2': prov_residenza,
        'viapiazza': indirizzo_residenza,
        'utenza telefonica': tel,
        'l_2': mail,
        'In caso di minore genitoretutore del minore': minore_nome,
        'natoa_2': minore_natoa,
        'prov_3': minore_prov_nascita,
        'l_3': '{:02}/{:02}/{:04}'.format(minore_data_nascita_d, minore_data_nascita_m, minore_data_nascita_y),
        'n_2': minore_residenza,
        'prov_4': minore_prov_residenza,
        'in data': covid_tampone1,
        'n data': covid_tampone2,
        'terminato in data': covid_fine,
        'Data': giorno,
        'undefined': mese,
        'undefined_2': anno,
        'undefined_3': nome
    }

    _fill_cert(data, nome, giorno, mese, anno)


def fill_cert_maggiorenne(nome, natoa, prov_nascita, data_nascita_d, data_nascita_m, data_nascita_y,
                          residenza, prov_residenza, indirizzo_residenza, tel, mail,
                          covid_tampone1='', covid_tampone2='', covid_fine='',
                          giorno=date.today().day, mese=date.today().month, anno=date.today().year):
    data = {
        'sottoscrittoa': nome,
        'natoa': natoa,
        'prov': prov_nascita,
        'l': '{:02}/{:02}/{:04}'.format(data_nascita_d, data_nascita_m, data_nascita_y),
        'n': residenza,
        'prov_2': prov_residenza,
        'viapiazza': indirizzo_residenza,
        'utenza telefonica': tel,
        'l_2': mail,
        'In caso di minore genitoretutore del minore': '',
        'natoa_2': '',
        'prov_3': '',
        'l_3': '',
        'n_2': '',
        'prov_4': '',
        'in data': covid_tampone1,
        'n data': covid_tampone2,
        'terminato in data': covid_fine,
        'Data': giorno,
        'undefined': mese,
        'undefined_2': anno,
        'undefined_3': nome
    }

    _fill_cert(data, nome, giorno, mese, anno)


def _fill_cert(data, nome, giorno, mese, anno):
    pdf = pdf_processing.ProcessPdf(INPUT_PATH)

    # pdf.print_annotaion_keys()
    pdf.add_data_to_pdf(data, '{}/{}_{:04}{:02}{:02}.pdf'.format(OUTPUT_PATH, nome, anno, mese, giorno))


if __name__ == '__main__':
    fill_cert_maggiorenne('Davide Ponzini', 'Sanremo', 'IM', 18, 4, 1995, 'Sanremo', 'IM', 'Str. Caravelli 60',
                          '338 717 4566', 'davide.ponzini95@gmail.com')
