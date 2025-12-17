**This is a simple SRS tool.**
 I created for self use. I have a beginners level experience in coding and as such, some of the design choices in this are... less than perfect. But I decided to upload this to GitHub to push my into learning how to better design and figure out this small project.



**How to use:**
The tool is entirely based around CLI, and you should first grab a vocab list, preferably the one I set up the PDF_parser.py to operate with, which I have zero ownership or affiliation with, it's just a simple PDF vocab list that was easy to regex into binary dict in list.

**Link: https://learning-korean.com/pdf/**

From here, follow these steps:

prereq: PIP PyPDF2 if not installed already.

**1:** Download vocab PDF, place in main program directory run PDF_parser.py, input name of PDF file without file extension('example', not 'example.pdf')
**2:** Run main.py within a CLI interface, PowerShell, CMD, terminal, whatever you want. And from there, you will be given a word list for memorization.
**3:** focus on given word list, and the next day, rerun the program, and it will go over the previously given word list, it's currently pedantic and precise, so don't be too discouraged if wrong.
**4:** Repeat daily


**Customization:**
Current customization is just to alter the session size for each day, which is within the main.py script at the very top, change it as seen fit.


REQUIREMENTS:


PyPDF2 python module.
