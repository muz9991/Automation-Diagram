import xml.etree.ElementTree as ET
import re

# Load and parse the XML content of the .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Funnel Blueprint Template.drawio.xml'  # Update this path to the actual file location
tree = ET.parse(file_path)
root = tree.getroot()

# Diagram names to mxCell ID mapping
diagram_name_to_mxcell_id = {
    "Asset List & Key": "AB2HBRWyPQBId71OJ_yW-12",
    "[MED-FAM] Module Overview": "O5Cyq6NREbMeisfC8xo0-3",
    "[MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking": "4yWAkR8pzB3zzQDbWqw--31",
    "[MED-FAM]-002: WF-1a Discovery Call Booking Reminders": "2tSnXhB2M8sNZobx151B-7",
    "[MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage": "bqfVK91TgHqyL-_8v1_e-6",
    "[MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage": "shu6U-08ORLhxLvYIuO6-7",
    "[MED-FAM]-003: WF-1a MIAM Email → Signed Contract": "lqf3qd-tQyry-E2M1xLv-6",
    "[MED-FAM]-003: WF-2a Contacting C2": "tpmut8-QV2Y60LBQgdAo-7",
    "[MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid": "PvWFEwlFV45Gfdx5ZtZF-7"
}

# Example: Selected diagram and new heading text
selected_diagram_name = "[MED-FAM] Module Overview"  # Replace with your selected diagram name
new_heading_text = "asdadadad"  # Replace with your new heading text

# Update heading based on diagram name
def update_heading_for_diagram(root, diagram_name, new_heading):
    mxcell_id = diagram_name_to_mxcell_id.get(diagram_name)
    if mxcell_id:
        for elem in root.iter():
            if elem.tag == 'mxCell' and elem.get('id') == mxcell_id:
                # Update 'value' attribute to new_heading
                elem.set('value', new_heading)
                return True
    return False

# Perform the heading update
heading_updated = update_heading_for_diagram(root, selected_diagram_name, new_heading_text)

# Save the updated XML back to a different .drawio file if any updates were made
if heading_updated:
    updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Diagram Funnel Blueprint Template.drawio.xml'  # Update this path to the actual file location # Update this path as needed
    tree.write(updated_file_path)
    print(f'Heading updated successfully for diagram "{selected_diagram_name}". Updated file: {updated_file_path}')
else:
    print(f'No heading was updated. Please check the provided diagram name and mxCell ID.')

