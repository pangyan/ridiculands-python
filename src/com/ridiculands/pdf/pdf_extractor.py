import pdfplumber


def build_group_in_charge(description, item_value, delimiter):
    if item_value and not item_value.isspace():
        if description and not description.isspace():
            return description + '：' + item_value + delimiter
        else:
            return item_value + delimiter
    else:
        return ''


def build_groups(hymns, snacks, service):
    if (hymns and not hymns.isspace()) or (snacks and not snacks.isspace()) or (service and not service.isspace()):
        return '（' + hymns + snacks + service + '）'
    else:
        return ''


def build_event_entry(date, description, group):
    if date and not date.isspace():
        return date.rjust(6) + '　' + description + '　' + group
    else:
        return ''


def build(event_header, event_entry):
    result = build_event_entry(
                event_entry[5],
                event_entry[6],
                build_groups(
                    build_group_in_charge(event_header[7], event_entry[7], '；'),
                    build_group_in_charge(event_header[8], event_entry[8], '；'),
                    build_group_in_charge(event_header[9], event_entry[9], '')
                )
            )
    return result


if __name__ == "__main__":
    print("dnlmch")

pdf = pdfplumber.open("/Users/pywong/Documents/Hosanna_roster_2020-v5-test.pdf")

# for page in pdf.pages:
first_page = pdf.pages[0]
# print(first_page.extract_text())
table = first_page.extract_table()
print(table[1][7])
print(table[1][8])
print(table[1][9])

for i in range(2, len(table)):
    print(build(table[1], table[i]))
    # print(table[i][5:])


