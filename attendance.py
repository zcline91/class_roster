import csv
import datetime

with open('roster.csv', 'r', encoding="utf-8") as rosterfile:
    roster = list(csv.DictReader(rosterfile))
the_date = datetime.date.today()
sections = set(student['Section'] for student in roster)

# Choose section
if len(sections) > 1:
    sections.add("all")
    att_section = None
    while att_section not in sections:
        att_section = input(
            "Which section is this attendance for? " +
            f"(options: {', '.join(sorted(sections))}): "
            )
else:
    att_section = "all"

# Set roster and filename
if att_section == "all":
    att_roster = roster
    att_filename = f'attendance_{the_date}.csv'
else:
    att_roster = [student for student in roster 
        if student["Section"] == att_section]
    att_filename = f'attendance_{att_section}_{the_date}.csv'

# Take attendance
with open(att_filename, 'w', encoding="utf-8", newline='') as attendancefile:
    fieldnames = ['email', 'status']
    attendance = csv.DictWriter(attendancefile, fieldnames=fieldnames)
    attendance.writeheader()
    for student in att_roster:
        attendance.writerow({
            'email': student['Email Address'], 
            'status': student['Status']
            })
