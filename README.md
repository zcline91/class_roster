# Class Roster Scripts

This makes the process of taking attendance and assigning groups for group work a little less painful.
The current setup is for use with Moodle's attendance system, although I'm sure it can be adapted for use other learning management systems.

## Set-up

1. Run `pyinstaller --onefile attendance.py` and `pyinstaller --onefile groups.py` and move the resulting two executables as well as the roster.csv file to the desired location.

2. Change the roster.csv file to reflect your class roster. Likely, there is a way to automate the creation of the a roster CSV either using your school's LMS or regsitration system. However it is created, be sure the final result has columns labeled "Nickname", "Email Address", and "Status".
   - The "Nickname" field is for what to call people when printing groups. It's a good idea for this field to be unique to avoid confusion about which student is in which group.

3. (Optional) To customize the display of groups, you can alter the values of `PRINT_WIDTH`, `MAX_NAME_LENGTH`, and `SPACE_BETWEEN_GROUPS` in groups.py before compiling.

## Taking Attendance

Open roster.csv and set "Status" to 'P' for present, 'L' for late, 'E' for excused, and 'A' for absent. (These correspond to Moodle's status acronyms.) Once the "Status" field has been set, run attendance.exe to create a csv file for uploading to Moodle. In Moodle, go to the attendace session and select "Upload attendance by CSV".

## Splitting the Class into Groups

Update the roster.csv file as in the previous section -- to ensure there aren't absent people being put into groups -- and run groups.exe.
