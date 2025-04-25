str = 'CPE-CPE009A-2025: 0.8475'
colon = str.find(":")
afterColon = str[colon + 1:].strip()
convFloat = float(afterColon)

print(convFloat)
