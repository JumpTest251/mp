import xml.etree.ElementTree as ET

def parse_xml_string(xml_string):
    try:
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError as e:
        raise ValueError("Invalid XML string provided.") from e