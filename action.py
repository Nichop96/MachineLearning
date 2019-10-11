import xml.etree.ElementTree as ET


class Action:
    def __init__(self, xml_action):
        root = ET.fromstring(xml_action)
        self.name = root.find("Name").text