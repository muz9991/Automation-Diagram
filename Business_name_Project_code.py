import xml.etree.ElementTree as ET
import re

# Load and parse the XML content of the .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/XLm Diagram/2Funnel Blueprint Template.drawio.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# The name to search for and replace
search_name = "Bernadette Willems"
new_business_name = "YOUR_NEW_BUSINESS_NAME"  # Replace with the desired new business name
old_code = "[MED-FAM]"  
new_code = "[fag]"
# List of workflow descriptions to choose from




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

# Function to update the workflow description
def replace_project_code(xml_root, old_code, new_code):
    updated = False
    pattern = re.compile(re.escape(old_code))
    
    # Update project code in mxCell elements
    for elem in xml_root.iter():
        if 'value' in elem.attrib:
            new_value = pattern.sub(new_code, elem.attrib['value'])
            if new_value != elem.attrib['value']:
                elem.set('value', new_value)
                updated = True

    # Additionally, update diagram names if they contain the project code
    for diagram in xml_root.findall('.//diagram'):
        if old_code in diagram.get('name', ''):
            diagram.set('name', pattern.sub(new_code, diagram.get('name')))
            updated = True

    return updated


# Perform the replacements
business_name_updated = replace_business_name(root, search_name, new_business_name)
project_code_updated = replace_project_code(root, old_code, new_code)
# Save the updated XML back to a different .drawio file if any updates were made
if business_name_updated or project_code_updated:
    updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/XLm Diagram/1Template.drawio.xml'
    tree.write(updated_file_path)
    print(f'Updates completed successfully. Updated file: {updated_file_path}')
else:
    print('No updates were made. Please check the provided names and descriptions.')

