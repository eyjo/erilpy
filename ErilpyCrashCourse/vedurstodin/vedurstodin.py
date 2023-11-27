import requests
from lxml import etree

# Sækjum veðrið :-)


# API yfirliti Veðrustofunar
#   https://vedur.is/um-vi/vefurinn/xml/

# Leiðbendingar fyrir veður API
#   https://vedur.is/media/vedurstofan/XMLthjonusta.pdf

# Slóðin að vefþjónustu Veðurstofunar
url = "https://xmlweather.vedur.is"

payload = {
    "op_w": "xml",
    "type": "obs",
    "lang": "is",
    "view": "xml",
    "ids": "1;422;2738;1473",  # Reykjavík, Akureyri og Bolungarvík
    # "params": "T;D;F;W",  # hiti, vindátt, vindhraði, veðurlýsing ... valfrjálst
}
# vedurstofan notar semikommu aðgreiningu sem stríðir gegn stöðlum og er því umbreytt af requests
#  en þetta virkar samt

# Framkvæmum kallið:
response = requests.get(
    url=url, 
    params=payload)

# Svarið ætti að gefa kóðan ef allt gekk vel 200 eða 404 ef ekkert fanst
response
response.status_code
response.ok
# Listi yfir status skilaboð
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# upplýsingar um samskiptin/metadata
response.headers

# Það sem okkur barst
print(response.text)


# Umbreytum XML kóðanum í tré sem við getum lesið einingar (elements) úr:
tree = etree.fromstring(response.content)

# Til að sjá XML tréð skýrar
print(etree.tostring(tree, encoding="utf-8", pretty_print=True).decode())


# Til að fletta upp skammstöfunum (svona geymir maður yfirleitt í sér skjali)

maelistaerd = {
    'F': 'Vindhraði (m/s)',
    'FX': 'Mesti vindhraði (m/s)',
    'FG': 'Mesta vindhviða (m/s)',
    'D': 'Vindstefna',
    'T': 'Hiti (°C)',
    'W': 'Veðurlýsing',
    'V': 'Skyggni (km)',
    'N': 'Skýjahula (%)',
    'P': 'Loftþrýstingur (hPa)',
    'RH': 'Rakastig (%)',
    'SNC': 'Lýsing á snjó',
    'SND': 'Snjódýpt (cm)',
    'SED': 'Sjólag',
    'RTE': 'Vegahiti (°C)',
    'TD': 'Daggarmark (°C)',
    'R': 'Uppsöfnuð úrkoma (mm / klst) úr sjálfvirkum mælum.',
}

vindstefna = {
    'Logn': 'Logn',
    'N': 'Norðan',
    'NNA': 'Norð-norð-austan',
    'ANA': 'Aust-norð-austan',
    'A': 'Austan',
    'ASA': 'Aust-suð-austan',
    'SA': 'Suð-austan',
    'SSA': 'Suð-suð-austan',
    'S': 'Sunnan',
    'SSV': 'Suð-suð-vestan',
    'SV': 'Suð-vestan',
    'VSV': 'Vest-suð-vestan',
    'V': 'Vestan',
    'VNV': 'Vest-norð-vestan',
    'NV': 'Norð-vestan',
    'NNV': 'Norð-norð-vestan',
}

# Búum til lista yfir stöðvarnar og setjum mælingar í uppflettanlegt form:
weather = []
for station in tree.findall('station'):
    station_id = station.attrib['id']
    weather.append({
        maelistaerd.get(observation.tag, observation.tag): observation.text if observation.tag != 'D' else vindstefna.get(observation.text, '')
        for observation in station
    })

# Svo hægt að vinna með þessa niðurstöðu áfram, s.s. til að birta í appi ...
weather



# eða bara láta rás1 hljómandi texta rúlla ...
def make_monolog(obs):
    return f"Veðurathugun fyrir {obs['name']}. {obs['Vindstefna'] if obs['Vindstefna'] else 'alls óljóst með'} átt, {obs['Vindhraði (m/s)']} m/s, hiti {obs['Hiti (°C)']} stig."

for station in weather:
    print(make_monolog(station))



