message = 'Call me 415-555-1011 tomorrow, or at 405-555-9999 or my office Line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message)

print(mo.group())