import json
f = open('fluc.json',)
data = json.load(f)

# jahr = 20210000 # "w_2021"
#     Monat = "Juli"
#     if Monat == "Jänner":
#         Monat1 = 100
#     Monat = "February"
#     if Monat == "Februar":
#         Monat2 = 200



d = data.replace('\\n', "")
d = d.replace('\\t', "")
d = d.replace('\\t\t\t', "")
d = d.replace('& nbsp', "")
d = d.replace('&nbsp', "")
d = d.replace("'", "")
d = d.replace('[', "")
d = d.replace(']', "")
d = d.replace('\n', "")
d = d.replace(',', "")
d = d.replace('Montag', "")
d = d.replace('Dienstag', "")
d = d.replace('Mittwoch', "")
d = d.replace('Donnerstag', "")
d = d.replace('Freitag', "")
d = d.replace('Samstag', "")
d = d.replace('Sonntag', "")
print(d)