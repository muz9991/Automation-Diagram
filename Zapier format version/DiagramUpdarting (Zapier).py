import xml.etree.ElementTree as ET
import json


'''
updates_json = 
{
    "vWboUKJ7EncdgkkKniVJ": "Asset ",
    "f106602c-feb2-e66a-4537-3a34d633f6aa": " Module Overview",
    "6PWxGtqC4kEad1Gby_Kv": "[MED-FAM]-001: WF-1.0 Enquiry → Discovery Call Booking",
    "p7mvYu89VrXbENbP1_v3": "[MED-FAM]-002: WF-1a Discovery Call Booking Reminders",
    "D9qbxVrSXw9fbJ4gGtpQ": "[MED-FAM]-002: WF-1b C1 Discovery Call Outcome Triage",
    "Y5UYIZtpkocbGI6UbQnA": "[MED-FAM]-002: WF-1c C2 Discovery Call Outcome Triage",
    "A485VMch9vQ3RFNtXNY8": "[MED-FAM]-003: WF-1a MIAM Email → Signed Contract",
    "Tz7Jego96uNzSW-XCynq": "[MED-FAM]-003: WF-2a Contacting C2",
    "pmE3DuMBG-1117bvLWQ5": "[MED-FAM]-004: WF-1.0 Mediation Confirmation → Signed & paid"
}
'''
diagram_id_to_mxcell_id = {
    "vWboUKJ7EncdgkkKniVJ": "AB2HBRWyPQBId71OJ_yW-12",
    "f106602c-feb2-e66a-4537-3a34d633f6aa": "O5Cyq6NREbMeisfC8xo0-3",
    "6PWxGtqC4kEad1Gby_Kv": "4yWAkR8pzB3zzQDbWqw--31",
    "p7mvYu89VrXbENbP1_v3": "2tSnXhB2M8sNZobx151B-7",
    "D9qbxVrSXw9fbJ4gGtpQ": "bqfVK91TgHqyL-_8v1_e-6",
    "Y5UYIZtpkocbGI6UbQnA": "shu6U-08ORLhxLvYIuO6-7",
    "A485VMch9vQ3RFNtXNY8": "lqf3qd-tQyry-E2M1xLv-6",
    "Tz7Jego96uNzSW-XCynq": "tpmut8-QV2Y60LBQgdAo-7",
    "pmE3DuMBG-1117bvLWQ5": "PvWFEwlFV45Gfdx5ZtZF-7",

}

def update_diagrams_and_headings_in_zapier(xml_content, updates_json):
    root = ET.fromstring(xml_content)
    updates = json.loads(updates_json)

    for diagram_id, new_name in updates.items():
        # Update diagram name
        diagram = root.find(f".//diagram[@id='{diagram_id}']")
        if diagram is not None:
            diagram.set('name', new_name)

        # Update corresponding mxCell heading
        mxcell_id = diagram_id_to_mxcell_id.get(diagram_id)
        if mxcell_id:
            mxcell = root.find(f".//mxCell[@id='{mxcell_id}']")
            if mxcell is not None:
                new_heading = f"<div style='text-align: center;'><b>{new_name}</b></div>"
                mxcell.set('value', new_heading)


    updated_xml_content = ET.tostring(root, encoding='unicode')

    return {'updated_xml_content': updated_xml_content}


xml_content = input_data['xml_content']
updates_json = input_data['updates_json']



output = update_diagrams_and_headings_in_zapier(xml_content, updates_json)
# print(output)
