
def vokon_zählen(wort):
    wort_lower = wort.lower()
    vokal = "aeiou"
    buchstaben = [i for i in wort_lower if i.isalpha()]
    vokale = [k for k in buchstaben if k in vokal]
    print(f'Es gibt in "{wort}" {len(vokale)} Vokale und {len(buchstaben) - len(vokale)} Konsonanten.')

vokon_zählen("Berlin")
vokon_zählen("HI,&%/ BerliN!!")