import xml.etree.ElementTree as ET

# The path to your .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Funnel Blueprint Template.drawio.xml'

# Load and parse the XML content of the .drawio file
tree = ET.parse(file_path)
root = tree.getroot()

# Specify the ID of the element you want to update
element_id = 'AB2HBRWyPQBId71OJ_yW-11'

# Specify the new name for the business
new_business_name = 'Steph'

# Function to update the text content for the specified ID
def update_business_name(root, element_id, new_name):
    # Search for the element with the specified ID
    for elem in root.iter():
        if elem.get('id') == element_id:
            for value in elem.iter('mxCell'):
                if 'value' in value.attrib:
                    value.set('value', new_name)
                    return True
    return False

# Update the business name in the diagram
updated = update_business_name(root, element_id, new_business_name)

if updated:
    # Save the updated XML back to a .drawio file
    updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Updated_Funnel_Blueprint_Template.drawio.xml'
    tree.write(updated_file_path)
    print(f'Business name updated successfully. Updated file: {updated_file_path}')
else:
    print('Element with the specified ID was not found.')
