import xml.etree.ElementTree as ET

# Load and parse the XML content of the .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Funnel Blueprint Template.drawio.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# The name to search for and replace
search_name = "Bernadette Willems"
new_business_name = "Steph"  # Replace with the desired new business name

# Function to search and replace the business name
def replace_business_name(root, search_name, new_name):
    updated = False
    # Search and replace the name
    for elem in root.iter():
        if elem.tag == 'mxCell' and 'value' in elem.attrib:
            if search_name in elem.attrib['value']:
                elem.set('value', elem.attrib['value'].replace(search_name, new_name))
                updated = True
    return updated

# Replace the business name in the diagram
updated = replace_business_name(root, search_name, new_business_name)

if updated:
    # Save the updated XML back to a different .drawio file
    updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Updated_Funnel_Blueprint_Template.drawio.xml'
    tree.write(updated_file_path)
    updated_file_path
else:
    print('The specified name was not found in the diagram.')

