from datetime import date, datetime
import sqlite3





# Adapter: Date → String
def date_to_db(d: date) -> str:
    return d.isoformat()

# Konverter: String (aus DB) → Date
def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

# Registrierung der Konvertierung bei sqlite
sqlite3.register_adapter(date, date_to_db)
sqlite3.register_converter("DATE", db_to_date)