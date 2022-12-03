import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import sys
from test_articulo import Articulo, Congreso, Tfe

def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    for key in list(record.keys()):
        if isinstance(record[key], str):
            record[key] = record[key].replace('\n',' ')

    record = type(record)
    record = author(record)
    record = convert_to_unicode(record)
    record = add_plaintext_fields(record)
    record = editor(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    #record = homogenize_latex_encoding(record)

    return record

def articulos(argv):
    with open(argv[0]) as bibtex_file:
        parser = BibTexParser()
        parser.add_missing_from_crossref = True
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)


        browser = Articulo()
        browser.setup_method(None)


        for entry in bib_database.entries:
            if (entry['ENTRYTYPE'] == 'article'):
                print(f'Título: {entry["plain_title"]}')
                print('Autores:')
                pos = 0
                for count, author in enumerate(entry['author']):
                    print(f'\t{author}')
                    if author.startswith(argv[1]):
                        pos = count+1
                print(f'Posición: {pos}')
                print(f'Revista: {entry["plain_journal"]}')
                print(f'Volumen: {entry["volume"]}')
                print(f'Año: {entry["year"]}')
                browser.aniade_articulo(entry, pos)
                #print(entry)


        browser.teardown_method(None)

def congresos(argv):
    with open(argv[0]) as bibtex_file:
        parser = BibTexParser()
        parser.add_missing_from_crossref = True
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)


        browser = Congreso()
        browser.setup_method(None)


        for entry in bib_database.entries:
            if (entry['ENTRYTYPE'] == 'inproceedings'):
                print(f'Título: {entry["plain_title"]}')
                print('Autores:')
                pos = 0
                for count, author in enumerate(entry['author']):
                    print(f'\t{author}')
                    if author.startswith(argv[1]):
                        pos = count+1
                print(f'Posición: {pos}')
                print(f'Congreso: {entry["plain_booktitle"]}')
                print(f'Año: {entry["year"]}')
                browser.aniade_congreso(entry, pos)
                #print(entry)


        browser.teardown_method(None)


def tfes(argv):
    import csv
    with open(argv[0],'r',encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        browser = Tfe()
        browser.setup_method(None)
        for entry in reader:
            print(f'TFE: {entry["Title"]}')
            browser.aniade_tfe(entry)
        browser.teardown_method(None)

if __name__ == "__main__":
    if (sys.argv[1] == 'revistas'):
        articulos(sys.argv[2:])
    elif (sys.argv[1] == 'congresos'):
        congresos(sys.argv[2:])
    elif (sys.argv[1] == 'tfes'):
        tfes(sys.argv[2:])
