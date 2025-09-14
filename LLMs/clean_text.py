import re
import textblob


# with open("pdf_text.txt", "r") as f:
#     print("Initiating: \n")
#     text = re.sub(r'--- Page \d+ ---', ' ', f.read())
#     clean_text = re.sub(r'\b(b|w|\?|HW|\d{1,3})+\b', ' ', text)
#     clean_text = re.sub(r'[^A-Za-z0-9\s.,;:!?()-]', '', clean_text)
#     print("Removed non alphabetic chars\n")
#     clean_text = re.sub(r'\s+', ' ', clean_text)
#     clean_text = re.sub(r'\n+', ' ', clean_text)
#     print("Added spaces\n")

#     # blob = textblob.TextBlob(clean_text)
#     # clean_text = blob.correct().string
#     # print("Text blob corrected \n Cleaned Text: \n")

#     print(clean_text[:2000])

#     with open("clean_text.txt", "w") as f:
#         f.write(clean_text)

with open("pdf_text.txt", "r") as f:
    text = f.read()

# Remove page markers
text = re.sub(r'--- Page \d+ ---', ' ', text)

# Collapse repeated letters (3+ times)
text = re.sub(r'(.)\1{2,}', r'\1', text)

# Remove residual OCR noise (1-2 letter words, stray numbers)
text = re.sub(r'\b([a-zA-Z0-9]{1,2})\b', ' ', text)
text = re.sub(r'\d+', ' ', text)

# Clean punctuation but keep musical symbols
text = re.sub(r'[^A-Za-z0-9\s.,;:!?()#/-]', '', text)

# Normalize whitespace
text = re.sub(r'\s+', ' ', text)

# Manual replacements for common OCR errors
replacements = {
    'alpha- bet': 'alphabet',
    'ledg9er': 'ledger',
    'Octave Registers ?': 'Octave Registers:',
    'Awlways': 'Always',
}
for k, v in replacements.items():
    text = text.replace(k, v)



with open("clean_text2.txt", "w") as f:
    f.write(text)
