NotetoQuizlet is a program aiming to quicken the process of translating words from one language to another,
thereafter creating a Quizlet based on those words. By taking the words from textdocuments saved in your folder 
of choice, translating them in DeepL's translator and then using Quizlet via. GUI automation - simulating
mouse-usage and keyboard-usage. 

REQUIREMENTS:
IT IS A REQUIREMENT THAT YOU HAVE DOWNLOADED DeepL(one of/if not the best translator): 
This link will take you to the download page: https://www.DeepL.com/windows/download/full/DeepLSetup.exe

IT IS A REQUIREMENT THAT YOU HAVE A QUIZLET ACCOUNT AND ARE LOGGED IN

HOW TO USE NotetoQuizlet
1. Create a folder wherever you like. This will be the folder containing the words you want translated and on Quizlet
2. Create the text documents inside the folder. WHEN SAVING THE TEXT DOCUMENTS IT IS IMPORTANT THAT YOU SAVE THEM AS
DOCUMENTS WITH UTF-8 ENCODING, OTHERWISE THE PROGRAM MIGHT NOT BE ABLE TO READ CHARACTERS LIKE: ä¨öáñ etc. 
IT IS ALSO VERY IMPORTANT THAT THE WORDS ARE SINGULAR AND IN THIS FORMAT:     
Say i wanted to translate german words. After each word there must be a newline, which is done by pressing enter:
König			
Apfel
Wasser			

3. Choose the language you want to translate from by clicking one of the buttons in the category: "Translate from:"
4. Choose the language you want to translate to by clicking one of the buttons in the category: "Translate to:"
5. Click "Browse for the folder with your text files inside" and navigate to the folder.
6. Click "Browse files for DeepL.exe" and navigate to your DeepL executable usually looks like: 
			C:\Users\Asser\AppData\Local\DeepL\DeepL.exe
      It is important that you choose the DeepLexecutable from the DeepL folder and not .\app-1.11.1 or the likes
7. When you're ready to have the program begin translating and uploading the quizlets click (remember you can't
use your mouse or keyboard whilst the program is running):
			"Start the translating process and upload to Quizlet"
		    DON'T USE YOUR MOUSE OR KEYBOARD OTHERWISE THE PROGRAM WON'T WORK
8. Enjoy

Stopping the program:
Stopping the program can be done by slamming your mouse into the top-left corner of your screen. You might
have to do this multiple times before having success

Reasons the program might not work for you:

1. P: The program won't write any of my words in the DeepL translator.
   S: Create the text documents inside the folder. WHEN SAVING THE TEXT DOCUMENTS IT IS IMPORTANT THAT YOU SAVE THEM AS
   DOCUMENTS WITH UTF-8 ENCODING, OTHERWISE THE PROGRAM MIGHT NOT BE ABLE TO READ CHARACTERS LIKE: ä¨öáñ etc.  
   Say i wanted to translate german words. After each word there must be a newline, which is done by pressing enter:

2. P: The program messed up the translating of one of my documents
   S: Sometimes the program messes up and locates elements on the screen in the wrong places. Simply retrying
   could fix the problem. Reminder to delete the filenameittranslated translations/final.txt files 
   in your folder as these files might stop you from running the program

Say we have a textfile: Textfile.txt with with UTF-8 encoding - can be chosen when clicking files -> Save as in the 
.txt document

Textfile.txt the content seen when opening the txt must be fo: 
König			<-wrote word and pressed enter
Apfel			<-wrote new word and pressed enter
Wasser			<-wrote new word (for the last word it does not matter if you have pressed enter)

3. P: The program opens https://quizlet.com/create-set but stops therafter
   S: This probably happened because of the browser window opening on another screen than your mainscreen. You must
   Delete the filenameittranslated translations.txt and filenameittranslated final.txt files in your folder
   and restart the program. If it still does not work reference Problem 3

4. P: The program will not start when clicking the "Start the translating process and upload to Quizlet" button 
   If you have already run the program it will create txt files called filenameittranslated translations.txt
   and filenameittranslated final.txt. When a file has associated "x translations/final.txt" files, it will not
   be included in the translating and uploading to Quizlet process. If all your files have these associated files
   The button "Start the translating process and upload to Quizlet" will not work.
   S: Delete the X translations.txt and X final.txt in your folder with your .txt files

5. P: The program relies on image recognition, which is used to locate elements on the screen based off of data
   from images. These images were created on my computer, which might have another colourscheme, which could result in
   the program not being able to find the screen element it is searching for.
   S: No solution is known yet, although, I might be able to rewrite the program in the future improving compatability

6. P: Sometimes Deepl.exe just won't open via. the script command 
   S:Can sometimes be solved by closing DeepL entirely
   and clicking the "Start the translating process and upload to Quizlet" button. 
 
7. P: If Options.txt in your NotetoQuizlet folder is empty the program can't run:
   S: You have to go through steps 1-6 found in HOW TO USE NotetoQuizlet.	

8. P: The program says: "Fatal error detected". "Failed to execute script NotetoQuizlet copy" upon closing
   S: This happens when the program has not been given all the information it needs to
   Start the translating process and upload to Quizlet. Go through steps 1-6 in HOW TO USE

Features I'm working on:
As you all know for some language learning it is very important to have the definite pronoun paired with the word.
In the future I might be able to automate the process of finding the definite pronoun of the word and having it
paired with the word for the Quizlet sets it will create. As of now it has not been implemented  
