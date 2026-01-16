def build_class_roster(enrollment_data):
    result = {}
    for dict in enrollment_data:
        result[dict["student_id"]] = dict['full_name']

    return result

def verify_attendance(roster_dict, sign_in_ids):
    roster_set = set(roster_dict.keys())
    sign_in_set = set(sign_in_ids)

    absent = roster_set - sign_in_set
    unregistered = sign_in_set - roster_set

    return absent , unregistered
    
def generate_absent_report(roster_dict,absent_ids):
    report=[
        f"ABSENT: {roster_dict[student_id]} (ID: {student_id})"
        for student_id in absent_ids]
    
    report.sort()
    return report

enrollment = [
    {'student_id': 501, 'full_name': "Sam Porter"},
    {'student_id': 502, 'full_name': "Fragile Express"},
    {'student_id': 503, 'full_name': "Die Hardman"}]
signed_in = [501, 503, 999]

roster=build_class_roster(enrollment)
absent,unregistered=verify_attendance(roster,signed_in)
report=generate_absent_report(roster,absent)

print("Absent IDs:", absent)
print("Unregistered IDs:" ,unregistered)
print("Report:",report)
