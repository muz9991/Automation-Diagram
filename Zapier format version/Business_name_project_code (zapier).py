import xml.etree.ElementTree as ET
import re

def replace_business_name(xml_root, search_name, new_name):
    updated = False
    for elem in xml_root.iter():
        if elem.tag == 'mxCell' and 'value' in elem.attrib:
            if search_name in elem.attrib['value']:
                elem.set('value', elem.attrib['value'].replace(search_name, new_name))
                updated = True
    return updated

def replace_project_code(xml_root, old_code, new_code):
    updated = False
    pattern = re.compile(re.escape(old_code))
    for elem in xml_root.iter():
        if 'value' in elem.attrib:
            elem.attrib['value'] = pattern.sub(new_code, elem.attrib['value'])

    # Additionally, update diagram names if they contain the project code
    for diagram in xml_root.findall('.//diagram'):
        if old_code in diagram.get('name', ''):
            diagram.set('name', pattern.sub(new_code, diagram.get('name')))
            updated = True
    return updated

def process_drawio_xml(input_data):
    xml_content = input_data['xml_content']
    new_business_name = input_data['new_business_name']
    old_code = "[MED-FAM]"
    new_code = input_data['new_project_code'] 
    search_name = "Bernadette Willems"
    root = ET.fromstring(xml_content)
    
    business_name_updated = replace_business_name(root, search_name, new_business_name)
    project_code_updated = replace_project_code(root, old_code, new_code)
    
    # Initialize output outside of conditionals
    output = {}
    if business_name_updated or project_code_updated:
        updated_xml_content = ET.tostring(root, encoding='unicode')
        # Prepare output based on the operations performed
        output = {'updated_xml_content': updated_xml_content}
    else:
        output = {'message': 'No updates were made. Please check the provided names and descriptions.'}

    return output

output = process_drawio_xml(input_data)
