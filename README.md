**This is a simple SRS tool.**
I created for self use. I have a beginners level experience in coding and as such, some of the design choices in this are... less than perfect. But I decided to upload this to GitHub to push my into learning how to better design and figure out this small project.

**How to use:**
The tool is entirely based around CLI, and you should first grab a vocab list, preferably the one I set the PDF_parser.py to operate with, which I have zero ownership or affiliation with, it's just a simple PDF vocab list that was easy to regex into binary dict in list:

**Link: https://learning-korean.com/pdf/**

**Guide**
From here, run either Run-Lite-SRS-Linux-macOS.sh or Run-Lite-SRS-Windows.bat, and from there everything should be self explanatory. Also, note; please run within a pre-existing terminal, otherwise you'll need to read the words of the day from the intrim.json directly due to the autoclosing terminal... I'll add in a keyboard interupt hold soon.

**Customization:**
Current customization is just to alter the session size for each day, which is within the main.py script at the very top, change it as seen fit.

REQUIREMENTS:
PyPDF2 python.
