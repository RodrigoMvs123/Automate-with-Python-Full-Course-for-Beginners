import camelot

tables = camelot.read_pdf(‘foo.pdf’, pages=‘1’)
print(tables)

tables.export(‘foo.cvs’, f=‘cvs’, compress=True)
tables[0].to_csv(‘foo.csv’)
print(tables[0].df)
