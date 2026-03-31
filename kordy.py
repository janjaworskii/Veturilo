import re
import pandas as pd
def kordy(plik): 
    osm = open(plik, encoding="utf-8").read()
    pattern = r"L\.marker\(\[(.*?)\]\).*?bindPopup\('(.*?)<br"
    matches = re.findall(pattern, osm)
    df = pd.DataFrame(matches, columns=['Coordinates', 'Station_Name'])
    df['Coordinates'] = df['Coordinates'].astype(str)
    df['Station_Name'] = df['Station_Name'].str.strip()
    return df