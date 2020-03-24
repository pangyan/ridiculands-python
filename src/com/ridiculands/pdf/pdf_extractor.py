import pdfplumber

if __name__ == "__main__":
    print("dnlmch")

pdf = pdfplumber.open("/Users/pywong/Documents/Hosanna_roster_2020-v5-test.pdf")

# for page in pdf.pages:
first_page = pdf.pages[0]
# print(first_page.extract_text())
table = first_page.extract_table()
for row in table:
    print(row[5:])
