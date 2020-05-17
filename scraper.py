from bs4 import BeautifulSoup
import requests

# All GEC country codes for the CIA website urls
gec_codes = [
    "AF", "AX", "AL", "AG", "AQ", "AN", "AO", "AV", "AY",
    "AC", "AR", "AM", "AA", "AT", "AS", "AU", "AJ", "BF",
    "BA", "FQ", "BG", "BB", "BS", "BO", "BE", "BH", "BN",
    "BD", "BT", "BL", "BK", "BC", "BV", "BR", "IO", "VI",
    "BX", "BU", "UV", "BM", "BY", "CV", "CB", "CM", "CA",
    "CJ", "CT", "CD", "CI", "CH", "KT", "IP", "CK", "CO",
    "CN", "CG", "CF", "CW", "CR", "CS", "IV", "HR", "CU",
    "UC", "CY", "EZ", "DA", "DX", "DJ", "DO", "DR", "EC",
    "EG", "ES", "EK", "ER", "EN", "WZ", "ET", "EU", "FK",
    "FO", "FJ", "FI", "FR", "FG", "FP", "FS", "GB", "GA",
    "GZ", "GG", "GM", "GH", "GI", "GO", "GR", "GL", "GJ",
    "GP", "GQ", "GT", "GK", "GV", "PU", "GY", "HA", "HM",
    "VT", "HO", "HK", "HQ", "HU", "IC", "IN", "ID", "IR",
    "IZ", "EI", "IM", "IS", "IT", "JM", "JN", "JA", "DQ",
    "JE", "JQ", "JO", "JU", "KZ", "KE", "KQ", "KR", "KN",
    "KS", "KV", "KU", "KG", "LA", "LG", "LE", "LT", "LI",
    "LY", "LS", "LH", "LU", "MC", "MA", "MI", "MY", "MV",
    "ML", "MT", "RM", "MB", "MR", "MP", "MF", "MX", "FM",
    "MQ", "MD", "MN", "MG", "MJ", "MH", "MO", "MZ", "WA",
    "NR", "BQ", "NP", "NL", "NT", "NC", "NZ", "NU", "NG",
    "NI", "NE", "NF", "MK", "CQ", "NO", "MU", "PK", "PS",
    "LQ", "PM", "PP", "PF", "PA", "PE", "RP", "PC", "PL",
    "PO", "RQ", "QA", "RE", "RO", "RS", "RW", "TB", "SH",
    "SC", "ST", "RN", "SB", "VC", "WS", "SM", "TP", "SA",
    "SG", "RI", "SE", "SL", "SN", "NN", "LO", "SI", "BP",
    "SO", "SF", "SX", "OD", "SP", "PG", "CE", "SU", "NS",
    "SV", "SW", "SZ", "SY", "TW", "TI", "TZ", "TH", "TT",
    "TO", "TL", "TN", "TD", "TE", "TS", "TU", "TX", "TK",
    "TV", "UG", "UP", "AE", "UK", "US", "UY", "UZ", "NH",
    "VE", "VM", "VQ", "WQ", "WF", "WE", "WI", "YM", "ZA",
    "ZI"
]

# List of the fact categories for each country
section_titles = ["geography", "people-and-society", "government", "economy", "transnational-issues"]

last_country = -1
last_section = -1

cur_country = last_country + 1
cur_section = last_section + 1

# Setup for bs4
URL = "https://www.cia.gov/library/publications/the-world-factbook/geos/" +\
        gec_codes[cur_country].lower() + ".html"
htmldoc = requests.get(URL)
soup = BeautifulSoup(htmldoc.content, 'html.parser')

# Find the container of the facts
all_expands = soup.find(attrs={"class": "expandcollapse"})
category = all_expands.find(id=section_titles[cur_section] + "-category-section")


# Functions to scrape and parse respective section
def get_geo(section):
    fields = [
        "location", "geographic-coordinates", "area",
        "land-boundaries", "climate", "terrain", "natural-hazards"
    ]
    # Everything except land-boundaries, the fact is the first child of the field
    # land-boundaries fact is second child

    facts = ""

    for field in fields:
        f = section.find(id="field-" + field)
        if f:  # check if the field exists because not all countries have the same data categories
            if field == "land-boundaries":
                facts += f.contents[3].get_text(" ", strip=True) + "\n"
            else:
                facts += f.contents[1].get_text(" ", strip=True) + "\n"

    return facts


def get_soc(section):
    fields = [
        "population", "languages", "age-structure", "median-age",
        "net-migration-rate", "life-expectancy-at-birth", "literacy"
    ]

    facts = ""

    for field in fields:
        f = section.find(id="field-" + field)
        if f:
            if field == "age-structure":
                for i in range(1, len(f.contents) - 2, 2):
                    facts += f.contents[i].get_text(" ", strip=True) + "\n"
            elif field == "literacy":
                facts += f.contents[3].get_text(" ", strip=True) + "\n"
            else:
                facts += f.contents[1].get_text(" ", strip=True) + "\n"

    return facts


def get_gov(section):
    pass


def get_eco(section):
    pass


def get_iss(section):
    pass


# Determine which fact category to show
if cur_section == 0:
    print(get_geo(category))
elif cur_section == 1:
    print(get_soc(category))
elif cur_section == 2:
    print(get_gov(category))
elif cur_section == 3:
    print(get_eco(category))
else:
    print(get_iss(category))

