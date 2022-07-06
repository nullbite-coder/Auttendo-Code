
# Auttendo - Automatic Attendance System

Auttendo is a Real Time – Automatic Attendance Management System using Facial Recognition of Student. The student attendance management system is in charge of keeping track of the student's attendance records. It generates student attendance based on their presence in class. It keeps track of attendance on a daily basis. The attendance will be calculated only if the student presents the specific day.
It can be installed on camera servers that can detect the presence of all students or employees entering the institute or organisation. It makes it easier to record, recognise, and save data in a CSV file in real time.

## Working

In Auttendo we have created UI based software to use this facial attendance system. The Software UI is user friendly and can be used by any person. In Auttendo we have made different modules which are – 
1.	User Interface: It contains list of menu items which can be accessed to have the complete view of the system. The system takes the input such as ID, Name, Semester and Mobile Number of the students for registration purpose. The ‘Take Images’ button is used to capture the images of the students. ‘Train System’ button is used to train the captured images. ‘Take Attendance’ button is used to store the attendance results in an excel sheet. 
2.	Face Detection: Multiple images of the students are captured and the images are pre-processed for detecting only the faces of the students
3.	Training: The captured images of the students are stored in a local database. The stored images are trained and are assigned corresponding labels such as Id and name.
4.	Face Recognition: On carrying out the recognition process, feature comparison takes place with respect to the features stored in the database. The face is displayed along with corresponding roll no and the name of the student and used for marking the attendance.
5.	Storing Attendance Result: The corresponding attendance of the students is stored in an excel sheet.
6.	Automatic Mail to Higher Authority: One additional module has been created to mail the CSV file automatically to the higher authorities.


## Installation

Open the terminal in the main base folders.

```bash
  python main.py
```
It will open the desktop application made using KIVY Framework.

Or you install the EXE file, from our releases.
## Screenshots
### 1. Home Screen
![App Screenshot](https://github.com/nullbite-coder/Auttendo-Code/blob/main/screenshots/01.jpg)
### 2. Menu Screen
![App Screenshot](https://github.com/nullbite-coder/Auttendo-Code/blob/main/screenshots/02.jpg)
### 3. System Requirements Screeen
![App Screenshot](https://github.com/nullbite-coder/Auttendo-Code/blob/main/screenshots/03.jpg)
### 4. Add User Screen
![App Screenshot](https://github.com/nullbite-coder/Auttendo-Code/blob/main/screenshots/04.jpg)
### 5. Check or Mail Attendance
![App Screenshot](https://github.com/nullbite-coder/Auttendo-Code/blob/main/screenshots/05.jpg)

