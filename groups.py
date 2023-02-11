import csv
import random

import numpy as np


PRINT_WIDTH = 80 # Sets maximum width to print groups
MAX_NAME_LENGTH = 15 # Sets the maximum length to print names 
SPACE_BETWEEN_GROUPS = 4 # Sets spacing between groups printed on same row
# The last two options determine how many groups can be printed per row

def printline(x, y, z, alignment="l"):
    assert alignment in ('l', 'r', 'c')
    if alignment == "l":
        print(f"{x:<23}{y:<23}{z:<23}")
    elif alignment == "c":
        print(f"{x:^23}{y:^23}{z:^23}")
    elif alignment == "r":
        print(f"{x:>23}{y:>23}{z:>23}")

with open('roster.csv', 'r', encoding="utf-8") as rosterfile:
    roster = list(csv.DictReader(rosterfile))
sections = set(student['Section'] for student in roster)

# Choose section
if len(sections) > 1:
    sections.add("all")
    gr_section = None
    while gr_section not in sections:
        gr_section = input(
            "Which section is this attendance for? " +
            f"(options: {', '.join(sorted(sections))}): "
            )
else:
    gr_section = "all"

# Set roster
if gr_section == "all":
    gr_roster = roster
else:
    gr_roster = [student for student in roster 
        if student["Section"] == gr_section]

students = [student['Nickname'] for student in gr_roster 
    if student['Status'] in ('P', 'L')]
random.shuffle(students)
print(f"Total students: {len(students)}")

# Select groups
groupsize = int(input("Desired group size: "))
num_groups = len(students) // groupsize
if not len(students) % groupsize == 0:
    l_or_s = None
    while l_or_s not in ("l", "s", "L", "S"):
        l_or_s = input("Allow larger or smaller groups? (l/s): ")
    if l_or_s in ("s", "S"):
        num_groups += 1
groups = np.array_split(students, num_groups)

# Print groups
grp_per_row = PRINT_WIDTH // MAX_NAME_LENGTH
groups_by_row = [groups[i:i+grp_per_row] 
    for i in range(0, len(groups), grp_per_row)]
for row_num, row in enumerate(groups_by_row):
    print('\n')
    print((gap := ' ' * SPACE_BETWEEN_GROUPS).join(
        [f"Group {row_num * grp_per_row + i + 1}".center(MAX_NAME_LENGTH) 
            for i in range(len(row))]
        ))
    print((gap).join(['-'*MAX_NAME_LENGTH] * len(row)))
    for i in range(max((len(group) for group in row))):
        line = ''
        for group in row:
            try:
                line += (group[i][:MAX_NAME_LENGTH].ljust(MAX_NAME_LENGTH 
                    + SPACE_BETWEEN_GROUPS))
            except IndexError:
                line += ' ' * (MAX_NAME_LENGTH + SPACE_BETWEEN_GROUPS)
        print(line)
input('')
