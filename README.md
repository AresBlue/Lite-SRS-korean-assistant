**This is a simple SRS tool.**
I created for self use. I have a beginners level experience in coding and as such, some of the design choices in this are... less than perfect. But I decided to upload this to GitHub to push my into learning how to better design and figure out this small project.

**How to use:**
The tool is entirely based around CLI, and you should first grab a vocab list, preferably the one I set the PDF_parser.py to operate with, which I have zero ownership or affiliation with. it's just a simple PDF vocab list that was easy to regex into binary dict in list:

**Link: https://learning-korean.com/pdf/** Place one of the vocab PDFs into the program's main directory.

**Guide**
From here, run either Run-Lite-SRS-Linux-macOS.sh or Run-Lite-SRS-Windows.bat, and from there, you will be directed to point the PDF_parser towards the vocab list PDF within main directory by name and asked if the parser grabbed the layout succesfully.
From here, you will be given the session word list, and then each time you rerun the script, you will have the previous word list quizzed on what they mean, its slightly off pedantic, but it's fully functional.

**Customization:**
Current customization is just to alter the session size for each day as well as the percentages of past words and words you got wrong in previous runs, which is within the config.py script at the very top, change it as seen fit.

REQUIREMENTS:
PyPDF2 python.


