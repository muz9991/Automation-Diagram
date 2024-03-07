import xml.etree.ElementTree as ET

# Load and parse the XML content of the .drawio file
file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/Funnel Blueprint Template.drawio.xml'  # Update this path to the actual file location
tree = ET.parse(file_path)
root = tree.getroot()

# Collect current diagram names and IDs
current_diagrams = {diagram.get('id'): diagram.get('name') for diagram in root.findall('.//diagram')}

# Dictionary to hold potential updates (example updates provided)
# Format: diagram_id: "New Diagram Name"
updates = {
    "vWboUKJ7EncdgkkKniVJ": "Asset List & Key",  # Asset List & Key - page 1
    "f106602c-feb2-e66a-4537-3a34d633f6aa": "[MED-FAM] Module Overview",  # [MED-FAM] Module Overview - page 2
    "6PWxGtqC4kEad1Gby_Kv": "[MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking",  # [MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking - page 3
    "p7mvYu89VrXbENbP1_v3": "[MED-FAM]-002: WF-1a Discovery Call Booking Reminders",  # [MED-FAM]-002: WF-1a Discovery Call Booking Reminders - page 4
    "D9qbxVrSXw9fbJ4gGtpQ": "[MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage",  # [MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage - page 5
    "Y5UYIZtpkocbGI6UbQnA": "[MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage",  # [MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage - page 6
    "A485VMch9vQ3RFNtXNY8": "[MED-FAM]-003: WF-1a MIAM Email → Signed Contract",  # [MED-FAM]-003: WF-1a MIAM Email → Signed Contract - page 7
    "Tz7Jego96uNzSW-XCynq": "[MED-FAM]-003: WF-2a Contacting C2",  # [MED-FAM]-003: WF-2a Contacting C2 - page 8
    "pmE3DuMBG-1117bvLWQ5": "[MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid",  # [MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid - page 9
}

# Diagram IDs to their corresponding mxCell IDs
diagram_id_to_mxcell_id = {
    "vWboUKJ7EncdgkkKniVJ": "AB2HBRWyPQBId71OJ_yW-12",  # Asset List & Key - page 1
    "f106602c-feb2-e66a-4537-3a34d633f6aa": "O5Cyq6NREbMeisfC8xo0-3",  # [MED-FAM] Module Overview - page 2
    "6PWxGtqC4kEad1Gby_Kv": "4yWAkR8pzB3zzQDbWqw--31",  # [MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking - page 3
    "p7mvYu89VrXbENbP1_v3": "2tSnXhB2M8sNZobx151B-7",  # [MED-FAM]-002: WF-1a Discovery Call Booking Reminders - page 4
    "D9qbxVrSXw9fbJ4gGtpQ": "bqfVK91TgHqyL-_8v1_e-6",  # [MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage - page 5
    "Y5UYIZtpkocbGI6UbQnA": "shu6U-08ORLhxLvYIuO6-7",  # [MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage - page 6
    "A485VMch9vQ3RFNtXNY8": "lqf3qd-tQyry-E2M1xLv-6",  # [MED-FAM]-003: WF-1a MIAM Email → Signed Contract - page 7
    "Tz7Jego96uNzSW-XCynq": "tpmut8-QV2Y60LBQgdAo-7",  # [MED-FAM]-003: WF-2a Contacting C2 - page 8
    "pmE3DuMBG-1117bvLWQ5": "PvWFEwlFV45Gfdx5ZtZF-7",  # [MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid - page 9
}



def update_diagrams_and_headings(root, current_diagrams, updates, diagram_id_to_mxcell_id):
    for diagram_id, new_name in updates.items():
        # Check if the diagram name has been updated
        if current_diagrams.get(diagram_id) != new_name:
            # Update diagram name
            diagram = root.find(f".//diagram[@id='{diagram_id}']")
            if diagram is not None:
                diagram.set('name', new_name)
                print(f"Diagram ID {diagram_id} name updated to '{new_name}'.")

            # Update corresponding mxCell heading
            mxcell_id = diagram_id_to_mxcell_id.get(diagram_id)
            if mxcell_id:
                mxcell = root.find(f".//mxCell[@id='{mxcell_id}']")
                if mxcell is not None:
                    new_heading = f"<div style='text-align: center;'><b>{new_name}</b></div>"  # Example new heading format
                    mxcell.set('value', new_heading)
                    print(f"Updated mxCell ID {mxcell_id} with new heading: '{new_name}'.")

# Perform the updates
update_diagrams_and_headings(root, current_diagrams, updates, diagram_id_to_mxcell_id)

# Save the updated XML back to a different .drawio file
updated_file_path = '/Users/muzammilmahomed/Documents/Outhouse-uk/Ontraport_export/XLm Diagram/diagrass Funnel Blueprint Template.drawio.xml'  # Update this path as needed
tree.write(updated_file_path)
print(f"Updates completed. Updated file saved to: {updated_file_path}")
