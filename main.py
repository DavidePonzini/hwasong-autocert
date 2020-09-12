import autocert

if __name__ == '__main__':
    # Override if needed
    # autocert.OUTPUT_PATH = 'D:/Desktop'

    autocert.fill_cert_maggiorenne('Davide Ponzini', 'citta`', 'prov', 12, 9, 2020, 'citta`', 'prov', 'indirizzo',
                          'tel', 'mail@mail.com')
