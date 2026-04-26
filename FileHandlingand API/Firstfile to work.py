import json
from pathlib import Path

file_path = Path("C:\\Users\\Aman amoriya\\Rishabh python\\FileHandlingand API\\Music.json")

data = json.loads(file_path.read_text())
print(data)


    
