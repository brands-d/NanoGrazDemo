from re import compile, findall

text = "A cat, a car, and a carr were in the cartr."

pattern = compile(r"car*")
matches = findall(pattern, text)
if matches:
    print(matches)  # Output: ['ca', 'car', 'carr', 'car']
