import re

string_text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, string_text)
for extracted_email in extracted_emails:
    print(extracted_email[0])
