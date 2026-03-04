from urllib.parse import quote

attack = "' OR 1=1 --"
safe = quote(attack)
print(f"Original : {attack}")
print(f"Encoded  : {safe}")


