import os
import time

from dotenv import load_dotenv
from pyairtable import Table

load_dotenv()

# Load the values from .env
api_key = os.environ["ATF_API_KEY"]
base_id = os.environ["BASE_ID"]
table_id = os.environ["TABLE_ID"]
SECONDS = 60
MINUTES = 10

table = Table(api_key, base_id, table_id)

records = table.all(
    view="Send emails",
)

for record in records:
    table.update(record_id=record["id"], fields={"Enviar email": True})
    print(f"Email sent to: {record['fields']['Nombre']}")
    time.sleep(MINUTES * SECONDS)
