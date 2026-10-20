import xml.etree.ElementTree as ET
#xml reading function
def load_articles():
    xml_path = "Data/data.xml"
    tree = ET.parse(xml_path)
    root = tree.getroot()   
    articles = root.findall('article')

    return articles