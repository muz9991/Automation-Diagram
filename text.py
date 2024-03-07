import xml.etree.ElementTree as ET
import re

# Load and parse the XML content of the .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Funnel Blueprint Template.drawio.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# The name to search for and replace
search_name = "Bernadette Willems"
new_business_name = "YOUR_NEW_BUSINESS_NAME"  # Replace with the desired new business name

# List of workflow descriptions to choose from
workflow_descriptions = [
    "[MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking",
    "[MED-FAM]-002: WF-1a Discovery Call Booking Reminders",
    "[MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage",
    "[MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage",
    "[MED-FAM]-003: WF-1a MIAM Email → Signed Contract C1",
    "[MED-FAM]-003: WF-2a Contacting C2",
    "[MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid"
]

# Select a specific workflow description
# For this example, selecting the first option. Replace 0 with the index of your choice.
selected_workflow_description = workflow_descriptions[0]

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
def update_workflow_description(root, new_workflow_description):
    updated = False
    pattern = re.compile(r'\[MED-FAM\]-\d{3}: WF-[\d\.a-z]+ .*? → .*?')

    for elem in root.iter():
        if elem.tag == 'mxCell' and 'value' in elem.attrib:
            cell_value = elem.attrib['value']
            if pattern.search(cell_value):
                new_value = pattern.sub(new_workflow_description, cell_value)
                elem.set('value', new_value)
                updated = True
    return updated

# Perform the replacements
business_name_updated = replace_business_name(root, search_name, new_business_name)
workflow_description_updated = update_workflow_description(root, selected_workflow_description)

# Save the updated XML back to a different .drawio file if any updates were made
if business_name_updated or workflow_description_updated:
    updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/uUpdated_Funnel_Blueprint_Template.drawio.xml'
    tree.write(updated_file_path)
    print(f'Updates completed successfully. Updated file: {updated_file_path}')
else:
    print('No updates were made. Please check the provided names and descriptions.')
