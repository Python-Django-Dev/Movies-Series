import json

# Open the file in binary mode to inspect and clean invalid bytes
with open('db.json', 'rb') as file:
    content = file.read()

# Check if the file starts with a BOM (UTF-16 BOM is 0xFFFE)
if content.startswith(b'\xfe\xff') or content.startswith(b'\xff\xfe'):
    print("File starts with a UTF-16 BOM. Attempting to decode as UTF-16.")
    content = content[2:]  # Remove the BOM if it's UTF-16

# Try decoding the file content with UTF-16 to handle potential UTF-16 encoding
try:
    decoded_content = content.decode('utf-16')  # Try decoding as UTF-16
    print("File successfully decoded with UTF-16!")
except UnicodeDecodeError as e:
    print(f"Error decoding content with UTF-16: {e}")
    exit(1)

# Try loading the JSON data from the decoded content
try:
    data = json.loads(decoded_content)
    print("Data loaded successfully!")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    print("The content is still not valid JSON.")

# Save the cleaned data back to a new file in UTF-8
with open('db_cleaned.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("Cleaned data saved to 'db_cleaned.json'")
