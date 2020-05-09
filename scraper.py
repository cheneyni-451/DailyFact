from bs4 import BeautifulSoup
import requests

gec_codes = ["AF","AX","AL","AG","AQ","AN","AO","AV","AY"
            "AC","AR","AM","AA","AT","AS","AU","AJ","BF",
            "BA","FQ","BG","BB","BS","BO","BE","BH","BN",
            "BD","BT","BL","BK","BC","BV","BR","IO","VI",
            "BX","BU","UV","BM","BY","CV","CB","CM","CA",
            "CJ","CT","CD","CI","CH","KT","IP","CK","CO",
            "CN","CG","CF","CW","CR","CS","IV","HR","CU",
            "UC","CY","EZ","DA","DX","DJ","DO","DR","EC",
            "EG","ES","EK","ER","EN","WZ","ET","EU","FK",
            "FO","FJ","FI","FR","FG","FP","FS","GB","GA",
            "GZ","GG","GM","GH","GI","GO","GR","GL","GJ",
            "GP","GQ","GT","GK","GV","PU","GY","HA","HM",
            "VT","HO","HK","HQ","HU","IC","IN","ID","IR",
            "IZ","EI","IM","IS","IT","JM","JN","JA","DQ",
            "JE","JQ","JO","JU","KZ","KE","KQ","KR","KN",
            "KS","KV","KU","KG","LA","LG","LE","LT","LI",
            "LY","LS","LH","LU","MC","MA","MI","MY","MV",
            "ML","MT","RM","MB","MR","MP","MF","MX","FM",
            "MQ","MD","MN","MG","MJ","MH","MO","MZ","WA",
            "NR","BQ","NP","NL","NT","NC","NZ","NU","NG",
            "NI","NE","NF","MK","CQ","NO","MU","PK","PS",
            "LQ","PM","PP","PF","PA","PE","RP","PC","PL",
            "PO","RQ","QA","RE","RO","RS","RW","TB","SH",
            "SC","ST","RN","SB","VC","WS","SM","TP","SA",
            "SG","RI","SE","SL","SN","NN","LO","SI","BP",
            "SO","SF","SX","OD","SP","PG","CE","SU","NS",
            "SV","SW","SZ","SY","TW","TI","TZ","TH","TT",
            "TO","TL","TN","TD","TE","TS","TU","TX","TK",
            "TV","UG","UP","AE","UK","US","UY","UZ","NH",
            "VE","VM","VQ","WQ","WF","WE","WI","YM","ZA",
            "ZI"]

URL = "https://www.cia.gov/library/publications/the-world-factbook/geos/af.html"
htmldoc = requests.get(URL)

soup = BeautifulSoup(htmldoc.content, 'html.parser')

all_expands = soup.find(attrs={"class": "expandcollapse"})
section_titles = ["geography", "people-and-society", "government", "economy", "transnational-issues"]

last_country = 0
last_section = 0


