from select import select
import sqlite3

conn = sqlite3.connect('Med_Table.db')
db = conn.cursor()

db.execute('''Create table Compositions (ID TEXT, Composition_name TEXT, Generic_comp_eq TEXT, PRIMARY KEY (ID));''')
db.execute('''Create table Medicines(med_id TEXT, Medicine_name TEXT, Manufacturer TEXT, Comp_ID TEXT, FOREIGN KEY (Comp_ID) REFERENCES Compositions(ID));''')
