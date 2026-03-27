import pandas as pd
import pytest
from pathlib import Path

# helpers shared across tests
def make_logid_df(fields, type_val='Traffic', category='forward'):
    """Build a minimal LOGID DataFrame for testing.
    fields: list of dicts with keys: name, type, length, desc
    """
    rows = []
    for f in fields:
        rows.append({
            'Log Field Name': f['name'],
            'Data Type': f.get('type', 'string'),
            'Length': f.get('length', '32'),
            'Description': f.get('desc', ''),
            'Type': type_val,
            'Category': category,
            'LOGID': '10',
            'Message_ID': '10',
            'Message_Description': 'TEST',
            'Message_Meaning': 'Test log',
            'Severity': 'Notice',
            'Version': '7.2.0',
        })
    return pd.DataFrame(rows)
