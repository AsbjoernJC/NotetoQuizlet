import webbrowser, pyperclip, pyautogui, time, re, requests, os, subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog, Text

#All variables should be readable and make sense in english

class Locator:     

    def __init__(self, id, confidence): 
        self.id = id    
        self.confidence = confidence      

    def __str__(self):
        return("Trying to locate " + self.id + " with a confidence of " + str(self.confidence))

    ##########Used for continually searching for a screen element untill it has popped up on the screen.
    #Maximizing time efficiency
    def wait_n_locate(self):     #Also an instance method. This one has two parameters
        time.sleep(0.2)
        try:
            position = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))
            return position
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate()

    ##########Used for continually searching for a screen element untill it has popped up on the screen and then cliks it.
    #Maximizing time efficiency
    def wait_n_locate_click(self):
        time.sleep(0.2)
        try:
            x = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))  
            pyautogui.click(x)
            return("202")
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate_click()

Deepl_trans_left_side = []
class DeeplLeft(Locator):   #used specifically for the left text field in Deepl as 
    #it opens up with black borders around the text field or with no black borders. Could just have named it wait_n_locate_click again.
    def try_marked_unmarked(self):
        time.sleep(0.2)
        try:        
            if Deepl_trans_left_side == []:
                f = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))
                DeeplTyskTekstfelt = f
                Deepl_trans_left_side.append(DeeplTyskTekstfelt)
        except TypeError:
            if Deepl_trans_left_side == [] and self.id=='.img\\DeeplTyskTekstfeltKey2.PNG':
                DeeplLeft(".img\\DeeplTyskTekstfeltKey.PNG", 0.25).try_marked_unmarked() #black border
            else:
                DeeplLeft(".img\\DeeplTyskTekstfeltKey2.PNG", 0.25).try_marked_unmarked() #no black border

class Importer(Locator):    #Used for a single element as it just wouldn't work otherwise for some reason
    def wait_n_locate_click(self):
        time.sleep(0.2)
        try:
            x = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence))  
            pyautogui.click(x)
            return("202")
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate_click()    



def wait_on_pyautogui(imagetolocate, confidence):      
    try:
        pyautogui.center(pyautogui.locateOnScreen(imagetolocate, confidence))
    except TypeError:
        time.sleep(0.2)
        wait_on_pyautogui(imagetolocate, confidence)

def CopynPaste():          
    pyautogui.hotkey("ctrl", "a");
    pyautogui.hotkey("ctrl", "c")


def OrdtilQuizlet(txtfile, txtfolder, languagefrom, languageto):        

    #txtfile is the file containing the words that will be translated
    #txtfolder is the folder containing all the txtfiles that will be translated 
    #languagefrom is the language the txtfile will be translated from
    #languageto is the language the txtfile will be translated into

    pathTranslations = txtfolder + "\\" + txtfile + " translations.txt"
    pathFinal = txtfolder + "\\" + txtfile + " final.txt"
    txtfilepath = txtfolder + "\\" + txtfile + ".txt"
    
    
    #Part reading the file that will be translated
    read_words = open(txtfilepath, "r", encoding="utf-8") 
    read_wordslist = read_words.readlines()         
    read_words.close()
    
    #Formatting
    format_txtdoc = open(txtfilepath, "w", encoding="utf-8")
    read_wordslistformatted = []
    for word in read_wordslist:
            read_wordslistformatted.append(word.strip())  #removes \n from list values and "\n" list values
    for word in read_wordslistformatted:
        if word == "":
            read_wordslistformatted.remove("")    #removes "" list values
    read_wordslistformatted = "\n".join(read_wordslistformatted)
    format_txtdoc.write(read_wordslistformatted)
    format_txtdoc.close() 

    #############################Part working with Deepl.exe
    #Opens Deepl.exe
    subprocess.run(saveexe[0])

    time.sleep(0.6)
    

    Deepl_left_side = DeeplLeft(".img\\DeeplTyskTekstfeltKey.PNG", 0.25)
    Deepl_left_side.try_marked_unmarked()   #When first opening Deepl the left field of text
    #Will either have a black border or it won't. the .try_marked_unmarked() method 
    #switches between the two possibilities
        
    ############Part finding the DeeplIntoButton (translate into):
    DeeplIntoButton = Locator(".img\\DeeplIntoButton.PNG", 0.3)
    DeeplIntoButton.wait_n_locate_click()
    #Chooses the language to translate the words into in Deepl
    #File format: D:\\BatFiles\\Quizletbilleder\\LanguageDeepl.PNG
    Deepltranslang = Locator(".img\\" + languageto + "Deepl.PNG", 0.6)
    Deepltranslang.wait_n_locate_click()
    time.sleep(0.6)

    pyautogui.click(Deepl_trans_left_side[0])  #Clicks the lext field of text
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")  
    pyautogui.hotkey("delete")      #removes any words in the field of text
    time.sleep(0.4)

    #Part opening the file that will be translated
    TyskeOrd = open(txtfilepath, "r", encoding="utf-8")        
    pyperclip.copy(TyskeOrd.read()) #copys the words that will be translated
    pyautogui.hotkey("ctrl", "v")   #pastes it into Deepl's left field of text
    TyskeOrd.close()

    #Part copying the translated words: 
    time.sleep(1.2)
    pyautogui.hotkey("tab")
    time.sleep(0.4)
    pyautogui.hotkey("tab") 
    time.sleep(0.6)
    pyautogui.hotkey("ctrl", "a")       
    pyautogui.hotkey("ctrl", "c")      #copys the translated words

    time.sleep(0.3)
    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")   
    TyskeOrd.write(pyperclip.paste()) 
    TyskeOrd.close()
    
    TyskeOrd = open(pathTranslations, "r", encoding="utf-8") 
    text = TyskeOrd.read()  
    TyskeOrd.close()

    #Formatting
    for i in range(len(text)):
        if text[-1] == "\n":
            text = text[:-1-1]
            continue
        break


    OversættelseRegex = re.compile(r"""\n(\n){2}""") #Finding three newline characters in a row. 
    #As this happens when Deepl doesn't come up with a translation and leaves the field empty
    OversættelseRegex.findall(text)
    FixedString = OversættelseRegex.sub("\n\n404Deepl\n", text)

 
    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")
    pyperclip.copy(FixedString)
    TyskeOrd.write(pyperclip.paste())
    TyskeOrd.close

    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")
    TyskeOrd.write(FixedString)
    TyskeOrd.close
    
    #Del der læser filerne 
    read_words = open(pathTranslations, "r", encoding="utf-8") 
    read_wordslist = read_words.readlines()        
    read_words.close()
    ##Del der formaterer  
    format_txtdoc = open(pathTranslations, "w", encoding="utf-8")
    read_wordslistformatted = []
    for word in read_wordslist:
            read_wordslistformatted.append(word.strip())  #Removes \n from list values and "\n" list values
    for word in read_wordslistformatted:
        if word == "":
            read_wordslistformatted.remove("")    #Removes "" list values
    read_wordslistformatted = "\n".join(read_wordslistformatted)
    format_txtdoc.write(read_wordslistformatted)
    format_txtdoc.close() 

    ####################################################################################### Part that merges the txt files 
    languagefromtxt = open(txtfilepath, "r", encoding="utf-8")     #The file containing the words that were translated
    languagetotxt = open(pathTranslations, "r", encoding="utf-8")   #The file containing the translations

    languageto_list = languagefromtxt.readlines()    #list med tyske ord
    languagefrom_list = languagetotxt.readlines()       #list from FileName translations.txt

    #Part formatting list 1 so it's only the words: No new line characters etc. 
    list_without_newline = []
    for word in languageto_list:
        list_without_newline.append(word.strip())  #removes \n from list values and "\n" list values    languagefromtxt.close()

    #Part formatting list 2 so it's only the words no new line characters etc. 
    list_words_only = []
    for word in languagefrom_list:
        list_words_only.append(word.strip())  #removes \n from list values and "\n" list values    languagetotxt.close()

    languagefrom_with_tabchar = []        #Same as List1 but the words have a tab character at the end
    languageto_with_newlinechar = []        #Same as List2 but the words have a newline character at the end.

    #Tilføjer et tab character for enden af hvert af de tyske ord
    for word in list_without_newline:     
        word = word + "\t"
        #This is the format needed for uploading a new Quizlet set
        languagefrom_with_tabchar.append(word)
    for word in list_words_only:   
        word = word + "\n"
        #This is the format needed for uploading a new Quizlet set   
        languageto_with_newlinechar.append(word)


    merged_list = []    #Creates a list of tuples from languagefrom_with_tabchar(languagefrom words with a \t character at the end) 
    #and languageto_with_newlinechar(translate to words with a \n character at the end)
    Quizlet_ready_list = []     #Creates a list from the words inside the tuples in merged_list 
    for i in range(len(languageto_list)):
        try:
            TupList = (languagefrom_with_tabchar[i], languageto_with_newlinechar[i])
            merged_list.append(TupList)
        except IndexError:
            TupList = (languagefrom_with_tabchar[i], "TransError")
            #Deepl doesn't always return with a translation, which could lead to languageto_with_newlinechar having a shorter length
            #Notifies the user that something went wrong during the translation
    
    for tuple in merged_list:
        for word in tuple:
            Quizlet_ready_list.append(word) 
            #Takes the strings inside of the tuples inside of merged_list and converts it to a list
    
    
    EndString = "".join(Quizlet_ready_list) #Makes the combined list of the words and their translations into a string, so it can be pasted into Quizlet
    pyperclip.copy(EndString)
    TestFil = open(pathFinal, "w", encoding="utf-8")        
    TestFil.write(EndString)
    TestFil.close
    
    #Has to be duplicated for it to work ? ? ? ? ? ? ? ?   ? ? ? Might be because fil1 and fil2 were never closed?
    EndString = "".join(Quizlet_ready_list)
    pyperclip.copy(EndString)
    TestFil = open(pathFinal, "w", encoding="utf-8")        
    TestFil.write(EndString)
    TestFil.close

    ################################Webbrowsing part - Quizlet
    webbrowser.open("https://quizlet.com/create-set")

    def wait_on_browser():      #You're a genius. When i first stumbled upon how i could use 
        #pyautogui.locateOnScreen without it being executed before the webbrowser was fully loaded. 
        #whilst also continually trying to locate the screen element minimizing any delay
        try:
            Import = pyautogui.center(pyautogui.locateOnScreen(".img\\ImportQuizlet.PNG", confidence=0.4))
        except TypeError:
            time.sleep(0.1)
            wait_on_browser()
    wait_on_browser()     



    ##############Clicks on import from word, excel, google docs, etc.
    Import = Importer(".img\\ImportQuizlet.PNG", 0.4)
    Import.wait_n_locate_click()
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.6)
    
    ############ Clicks on Import in the import from word, excel, google docs, etc. window
    ImportImport = Locator(".img\\ImportImport.PNG", 0.4)
    ImportImport.wait_n_locate_click()

    ########Create button
    CreateButton, confidence = ".img\\CreateButton.PNG", 0.4
    wait_on_pyautogui(CreateButton, confidence)
    pyautogui.click(CreateButton) 
    
    TitleQuizlet = Locator(".img\\TitleQuizlet.PNG", 0.4)
    TitleQuizlet.wait_n_locate_click()
    time.sleep(0.2) 
    pyautogui.typewrite(txtfile)    

    #####Choose language on Quizlet will always pick the left side first
    ChooseLanguage = Locator(".img\\ChooseLanguage.PNG", 0.4)
    ChooseLanguage.wait_n_locate_click()
    time.sleep(0.2)
    pyautogui.typewrite(languagefrom)      
    time.sleep(0.5)
    pyautogui.hotkey("enter")
    time.sleep(0.5)

    #####Choose language on Quizlet will click on the last side left
    ChooseLanguage = Locator(".img\\ChooseLanguage.PNG", 0.4)
    ChooseLanguage.wait_n_locate_click()
    time.sleep(0.2)
    pyautogui.typewrite(languageto)
    pyautogui.hotkey("enter")
    time.sleep(0.2)

    ########Create button
    CreateButton, confidence = ".img\\CreateButton.PNG", 0.4
    wait_on_pyautogui(CreateButton, confidence)
    pyautogui.click(CreateButton) 


root = tk.Tk()
saveexe = []
savedir = []

root.title("NoteToQuizlet")
logo = ".\\Deepl.ico"
root.iconbitmap(logo)

##################
savedoptions = []
savedlangoptions = []       #index[0] will always be languagefrom
def options_look():
    if os.path.isfile(".\\Options.txt"):
        with open(".\\Options.txt", "r", encoding="utf-8") as f:
            Options = f.readlines()
            for word in Options:
                if word[:11] in ["Translating"]:        #Translating from language: " + languagefrom[-1] + "\n" + "Translating to language:
                    pathregex = re.compile(r"""(:\s)(\w+)""", re.DOTALL)
                    mo = pathregex.search(word)
                    mostrip=mo.group(2)
                    savedlangoptions.append(mostrip)
                else:
                    pathregex = re.compile(r""" (\w\:(.)+)""", re.DOTALL)       #finds D:/ followed by anything
                    mo = pathregex.search(word)
                    mostrip = mo.group().strip()
                    savedoptions.append(mostrip)
options_look()

FileLog = []

#Lets the user choose their directory with txt files they want translated and uploaded to Quizlet
def BrowseFolder():
    foldername = filedialog.askdirectory()  
    if foldername == "":
        return
    elif foldername in FileLog:
        return
    else:
        FileLog.append(foldername)
        savedir.append(foldername)
    
    for file in FileLog: ##############Visual bug, it doesn't always remove and add a new label.
        if FileLog.count(foldername) == 1:
            try:
                label4.destroy()
            except NameError:
                try:
                    label.destroy()              
                except UnboundLocalError:
                    label = tk.Label(frame2, pady=5, text=file, fg="white", bg="gray")
                    label.pack(side=LEFT)

#Lets the user find Deepl.exe
FileLog2 = []
def BrowseDeepl():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    if filename == "": 
        return
    elif filename in FileLog2:
        return
    else:
        FileLog2.append(filename)
        saveexe.append(filename)

    for file in FileLog2:       #######Visual bug, it doesn't always remove and add a new label. 
        #Think this is because the widget children has ever changing names when creating more
        if FileLog2.count(filename) == 1:
            try:
                label3.destroy()
            except NameError:
                try:
                    label2.destroy()              
                except UnboundLocalError:
                    label2 = tk.Label(frame3, pady=5, text=file, fg="white", bg="gray")
                    label2.pack(side=LEFT)

tr = ttk.Style()                     # Creating style element
tr.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background="#263D42",         # Setting background to our specified color above
        foreground="white")         # You can define colors like this also

l = ttk.Style()                     # Creating style element
l.configure('Wild.TLabel',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background="#263D42",         # Setting background to our specified color above
        foreground="white")         # You can define colors like this also

#Baggrund
canvas = tk.Canvas(root, height=500, width=700, bg="#263D42")
canvas.pack(expand=YES, fill=BOTH)
pic1 = PhotoImage(file=".img\\QuizletCanvasBaggrundRed2.png")
canvas.create_image(0, 0, image=pic1, anchor=NW)

#Frames holding the radio buttons
frame4 = tk.Frame(canvas, height=500, width=700, bg="#263D42")    #translate from
frame4.place(y=2, x=3)
labelf4 = ttk.Label(frame4, text="Translate from:", style='Wild.TLabel')
labelf4.pack()

frame5 = tk.Frame(canvas, height=500, width=700, bg="#263D42")    #translate to
frame5.place(y=2, x=86)
labelf5 = ttk.Label(frame5, text="Translate to:", style='Wild.TLabel')
labelf5.pack()

#I just learned about nested dictionaries so I went a wee bit crazy
d = {1: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    2: {12:"English", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    3: {13:"French", 12:"English", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    4: {13:"French", 14:"German", 12:"English", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    5: {13:"French", 14:"German", 15:"Spanish", 12:"English", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    6: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 12:"English", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    7: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 12:"English", 19:"Polish", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    8: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 12:"English", 20:"Russian", 21:"Japanese", 22:"Chinese"},
    9: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 12:"English", 21:"Japanese", 22:"Chinese"},
    10: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 12:"English", 22:"Chinese"},
    11: {13:"French", 14:"German", 15:"Spanish", 16:"Portuguese", 17:"Italian", 18:"Dutch", 19:"Polish", 20:"Russian", 21:"Japanese", 12:"English"}}  

df = {1: "English", 2:"French", 3:"German", 4:"Spanish", 5:"Portuguese", 6:"Italian", 7:"Dutch", 8:"Polish", 9:"Russian", 10:"Japanese", 11:"Chinese"}
languagefrom, languageto = [], []

def sel(var, var2):
    try:   
        #bug Languagefrom and languageto keeps appending when clicking the radio buttons
        langf = df[var]
        languagefrom.append(langf)        
        savedlangoptions.insert(0, langf)
        langt =  d[var][var2]
        languageto.append(langt)
        savedlangoptions[-1] = langt
    except KeyError:
        return


#Radiobuttons der bruges til at bestemme, hvilket sprog man vil have det oversat fra og til
#From language R1-12
# Main window
                # Its a light blue color




var = IntVar()
R1 = ttk.Radiobutton(frame4, text="English", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=1)
R1.pack( anchor = W )

R2 = ttk.Radiobutton(frame4, text="French", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=2)
R2.pack( anchor = W )

R3 = ttk.Radiobutton(frame4, text="German", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=3)
R3.pack( anchor = W)

R4 = ttk.Radiobutton(frame4, text="Spanish", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=4)
R4.pack( anchor = W )

R5 = ttk.Radiobutton(frame4, text="Portuguese", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=5)
R5.pack( anchor = W )

R6 = ttk.Radiobutton(frame4, text="Italian", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=6)
R6.pack( anchor = W)

R7 = ttk.Radiobutton(frame4, text="Dutch", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=7)
R7.pack( anchor = W )

R8 = ttk.Radiobutton(frame4, text="Polish", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()),  value=8)
R8.pack( anchor = W )

R9 = ttk.Radiobutton(frame4, text="Russian", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=9)
R9.pack( anchor = W)

R11 = ttk.Radiobutton(frame4, text="Japanese", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=10)
R11.pack( anchor = W )

R12 = ttk.Radiobutton(frame4, text="Chinese", style = "Wild.TRadiobutton", variable=var, command = lambda: sel(var.get(), var2.get()), value=11)
R12.pack( anchor = W )

#To Language F12-22
var2 = IntVar()
R1 = ttk.Radiobutton(frame5, text="English", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=12)
R1.pack( anchor = W )

R2 = ttk.Radiobutton(frame5, text="French", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=13)
R2.pack( anchor = W )

R3 = ttk.Radiobutton(frame5, text="German", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=14)
R3.pack( anchor = W)

R4 = ttk.Radiobutton(frame5, text="Spanish", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=15)
R4.pack( anchor = W )

R5 = ttk.Radiobutton(frame5, text="Portuguese", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=16)
R5.pack( anchor = W )

R6 = ttk.Radiobutton(frame5, text="Italian", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=17)
R6.pack( anchor = W)

R7 = ttk.Radiobutton(frame5, text="Dutch", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=18)
R7.pack( anchor = W )

R8 = ttk.Radiobutton(frame5, text="Polish", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=19)
R8.pack( anchor = W )

R9 = ttk.Radiobutton(frame5, text="Russian", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=20)
R9.pack( anchor = W)

R11 = ttk.Radiobutton(frame5, text="Japanese", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=21)
R11.pack( anchor = W )

R12 = ttk.Radiobutton(frame5, text="Chinese", style = "Wild.TRadiobutton", variable=var2, command = lambda: sel(var.get(), var2.get()), value=22)
R12.pack( anchor = W )

#Changes the language settings based on Options.txt, which saves the usersettings, the language they are translating from and to + paths to deepl.exe and txtfiles
def get_key(fromlangaugeval): 
	for key, value in df.items(): 
		if fromlangaugeval == value: 
			return key 

	return "key doesn't exist"
try: 
    a = get_key(savedlangoptions[0])
    var.set(a)
except IndexError:
    print("No savedlangoptions")

def get_key(fromlangaugeval, tolangaugeval): 
	for key, value in d[fromlangaugeval].items(): 
		if tolangaugeval == value: 
			return key 
try: 
    a = get_key(var.get(), savedlangoptions[-1])
    var2.set(a)
except IndexError:
    print("No savedlangoptions")   

#frame containing the buttons for browsing files 
frame = tk.Frame(canvas, height=100, width=700, bg="gray")
frame.place(x=210, rely=0.7)
#frame2 contains the label with the path to the folder with .txt files
frame2 = tk.Frame(root, height=100, width=355, bg="gray")
frame2.pack(side=LEFT, fill=BOTH, expand=YES)
#frame3 contains the label with the path to deepl.exe
frame3 = tk.Frame(root, height=100, width=355, bg="gray")
frame3.pack(side=RIGHT, fill=BOTH, expand=YES)


#Buttons for browsing files
OneNote = tk.Button(frame, text="Browse for the folder with your text files inside",
 padx=20, pady=5, fg="white", bg="#263D42", command=BrowseFolder)
OneNote.pack()

Deepl = tk.Button(frame, text="Browse files for Deepl.exe",
 padx=75, pady=5, fg="white", bg="#263D42", command=BrowseDeepl)
Deepl.pack()

def OrdtilQuizlet2():
        for word in savedoptions:                   
            if word[-4:] in [".exe"]:
                saveexe.append(word)
            else:
                savedir.append(word)
        for dirpath, dirnames, files in os.walk(savedir[0]):
            for txtfile in files:
                if txtfile[-16:] in ["translations.txt"]:
                    continue
                elif txtfile[-9:] in ["final.txt"]:
                    continue
                elif (lambda newfile: txtfile[:-4] + " final.txt")(txtfile) in files: #Checking if there's a file with the same name but final.txt at the end
                    continue
                elif txtfile[-4:] in [".txt"]:       
                    txtfile = txtfile[:-4]
                    OrdtilQuizlet(txtfile, savedir[0], savedlangoptions[0], savedlangoptions[-1])

                continue     

#The button to start the process of translating and uploading to Quizlet 
Start = OneNote = tk.Button(frame, text="Start the translating process and upload to Quizlet",
 padx=11, pady=5, fg="white", bg="#263D42", command = OrdtilQuizlet2)
Start.pack()


#Label containing the path to the folder containing the txt file
labelOnenote = tk.Label(frame2, text="Path to your folder:", fg="white", padx=10, pady=5, bg="gray")
labelOnenote.pack(side=LEFT)

#label containing the path to the Deepl.exe
labelDeepl = tk.Label(frame3, text="Path to Deepl.exe:", fg="white", padx=10, pady=5, bg="gray")
labelDeepl.pack(side=LEFT)

exesave = []
foldersave = []
for path in savedoptions:
    if path[-4:] in [".exe"]:               
        label3 = tk.Label(frame3, pady=5, fg="white", text=path, bg="gray")
        label3.pack(side=LEFT)
        exesave.append(path)      
    elif path[:11] in ["Translating"]:
        print("Skipped translation option")
    else:           
        label4 = tk.Label(frame2, text=path, fg="white", padx=10, pady=5, bg="gray")     
        label4.pack(side=LEFT)
        foldersave.append(path)




root.mainloop()

def save_options():             #Maybe use try and except to work around it displaying an error when savedoptions is empty
    #If/else statement is probably a better workaround
    with open(".\\Options.txt", "w", encoding="utf-8") as f:         
        for word in savedoptions:                    
            if word[-4:] in [".exe"]:
                saveexe.append(word)
            else:
                savedir.append(word)
        f.write("Path to your txt files: " + savedir[0] + "\n" + "Path to your Deepl.exe: " + saveexe[0] + "\n"
                + "Translating from language: " + savedlangoptions[0] + "\n" + "Translating to language: " + savedlangoptions[-1] + "\n")
save_options()


