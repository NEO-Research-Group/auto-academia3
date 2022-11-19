import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import sys
from test_articulo import TestArticulo

def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    record = editor(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    record = add_plaintext_fields(record)
    #record = homogenize_latex_encoding(record)

    return record


if __name__ == "__main__":
    with open(sys.argv[1]) as bibtex_file:
        parser = BibTexParser()
        parser.add_missing_from_crossref = True
        parser.add_plaintext
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)


        #browser = TestArticulo()
        #browser.setup_method(None)


        for entry in bib_database.entries:
            if (entry['ENTRYTYPE'] == 'article'):
                print(f'Título: {entry["plain_title"]}')
                print('Autores:')
                pos = 0
                for count, author in enumerate(entry['author']):
                    print(f'\t{author}')
                    if (author.startswith('Chicano')):
                        pos = count+1
                print(f'Posición: {pos}')
                print(f'Revista: {entry["journal"]}')
                print(f'Volumen: {entry["volume"]}')
                print(f'Año: {entry["year"]}')
                #browser.test_articulo(entry, pos)
                #print(entry)


        #browser.teardown_method(None)

