#Virkede som det skulle d. 11-08-2020 14:35 py 3.82  deepl 1.12.2
#Virkede som det skulle d. 11-08-2020 21:41 py 3.7 deepl 1.12.2
#Virkede som det skulle d. 12-08-2020 11:50 py 3.7 deepl 1.12.2
import webbrowser, pyperclip, pyautogui, time, re, requests, os, subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog, Text

class Locator:     

    def __init__(self, id, confidence): 
        self.id = id    
        self.confidence = confidence      

    #def description(self):  #This is an instance method. instance methods are functions that always
        #have the parameter self, just like __init__. Unlike init the parameters aren't a necessisty
        #to describe a dog. An instance method can only be called from an instance of that class.
    def __str__(self):
        return("Trying to locate " + self.id + " with a confidence of " + str(self.confidence))

    ##########Hvis det her ikke virker så kopier versionen fra quizletfratekstdokument.py
    def wait_n_locate(self):     #Also an instance method. This one has two parameters
        time.sleep(0.2)
        try:
            position = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))
            return position
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate()

    def wait_n_locate_click(self):
        time.sleep(0.2)
        try:
            x = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))  
            pyautogui.click(x)
            return("202")
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate_click()

DeeplTyskTekstfeltList = []
class DeeplLeft(Locator):

    def try_marked_unmarked(self):
        time.sleep(0.2)
        try:        
            if DeeplTyskTekstfeltList == []:
                f = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence, grayscale = True))
                DeeplTyskTekstfelt = f
                DeeplTyskTekstfeltList.append(DeeplTyskTekstfelt)
        except TypeError:
            if DeeplTyskTekstfeltList == [] and self.id=='.img\\DeeplTyskTekstfeltKey2.PNG':
                DeeplLeft(".img\\DeeplTyskTekstfeltKey.PNG", 0.05).try_marked_unmarked()
            else:
                DeeplLeft(".img\\DeeplTyskTekstfeltKey2.PNG", 0.05).try_marked_unmarked()

class Importer(Locator):
    def wait_n_locate_click(self):
        time.sleep(0.2)
        try:
            x = pyautogui.center(pyautogui.locateOnScreen(self.id, self.confidence))  
            pyautogui.click(x)
            return("202")
        except TypeError:
            time.sleep(0.1)
            self.wait_n_locate_click()    



def wait_on_pyautogui(imagetolocate, confidence):      #Du er genial brother
    try:
        pyautogui.center(pyautogui.locateOnScreen(imagetolocate, confidence))
    except TypeError:
        time.sleep(0.2)
        wait_on_pyautogui(imagetolocate, confidence)

def CopynPaste():           #Copy og paster
    pyautogui.hotkey("ctrl", "a");
    pyautogui.hotkey("ctrl", "c")


def OrdtilQuizlet(txtfile, txtfolder, languagefrom, languageto):        

    
    pathTranslations = txtfolder + "\\" + txtfile + " translations.txt"
    pathFinal = txtfolder + "\\" + txtfile + " final.txt"
    #SkrivOrdtilQuizlet = open((txtfolder), "w")
    txtfilepath = txtfolder + "\\" + txtfile + ".txt"
    
    
    # #Del der læser filerne 
    læsOrdtilQuizlet = open(txtfilepath, "r", encoding="utf-8") 
    læsOrdtilQuizletlist = læsOrdtilQuizlet.readlines()         #Giver liste af indholdet
    læsOrdtilQuizlet.close()
    
    #Del der formaterer  
    SkrivOrdtilQuizlet = open(txtfilepath, "w", encoding="utf-8")
    læsOrdtilQuizletlistformatted = []
    for word in læsOrdtilQuizletlist:
            læsOrdtilQuizletlistformatted.append(word.strip())  #fjerner \n fra list values og "\n" list values
    for word in læsOrdtilQuizletlistformatted:
        if word == "":
            læsOrdtilQuizletlistformatted.remove("")    #Fjerner "" list values
    læsOrdtilQuizletlistformatted = "\n".join(læsOrdtilQuizletlistformatted)
    SkrivOrdtilQuizlet.write(læsOrdtilQuizletlistformatted)
    SkrivOrdtilQuizlet.close() 

    #############################Del der finder engelske oversættelser af de tyske ord
    #Opens Deepl.exe
    subprocess.run(saveexe[0])

    time.sleep(0.6)
    

    Deepl_left_side = DeeplLeft(".img\\DeeplTyskTekstfeltKey.PNG", 0.25)
    Deepl_left_side.try_marked_unmarked()
        
    ############Del der finder DeeplIntoButton (translate into):
    DeeplIntoButton = Locator(".img\\DeeplIntoButton.PNG", 0.3)
    DeeplIntoButton.wait_n_locate_click()
    #Vælger sprog i deepl at translate into  #Filformat: D:\\BatFiles\\Quizletbilleder\\SprogDeepl.PNG
    Deepltranslang = Locator(".img\\" + languageto + "Deepl.PNG", 0.4)
    Deepltranslang.wait_n_locate_click()
    time.sleep(0.6)

    pyautogui.click(DeeplTyskTekstfeltList[0])  #Trykker i tekstfeltet
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")  #markere alt i tekstfeltet
    pyautogui.hotkey("delete")      #sletter alt i tekstfeltet
    time.sleep(0.4)
    #Del der åbner fil med tyske ord
    TyskeOrd = open(txtfilepath, "r", encoding="utf-8")        
    pyperclip.copy(TyskeOrd.read()) #kopiere de tyske ord
    pyautogui.hotkey("ctrl", "v")   #indsætter dem i deepl
    TyskeOrd.close()

    #Del der kopier de engelske ord: 
    time.sleep(1.2)
    pyautogui.hotkey("tab")
    time.sleep(0.4)
    pyautogui.hotkey("tab") 
    time.sleep(0.6)
    pyautogui.hotkey("ctrl", "a")  #markere alt i tekstfeltet
    pyautogui.hotkey("ctrl", "c")      #sletter alt i tekstfeltet

    time.sleep(0.3)
    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")   
    TyskeOrd.write(pyperclip.paste()) 
    TyskeOrd.close()
    
    TyskeOrd = open(pathTranslations, "r", encoding="utf-8") 
    text = TyskeOrd.read()  #string of translations
    TyskeOrd.close()

    #Formattering
    for i in range(len(text)):
        if text[-1] == "\n":
            text = text[:-1-1]
            continue
        break


    OversættelseRegex = re.compile(r"""\n(\n){2}""") #Leder efter tre newline chars i træk
    OversættelseRegex.findall(text)
    FixedString = OversættelseRegex.sub("\n\n404Deepl\n", text)

    #Hvis denne del ikke er der, vil TyskeOrd.write(FixedString) ikke virke?????
    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")
    pyperclip.copy(FixedString)
    TyskeOrd.write(pyperclip.paste())
    TyskeOrd.close

    TyskeOrd = open(pathTranslations, "w", encoding="utf-8")
    TyskeOrd.write(FixedString)
    TyskeOrd.close
    
    #Del der læser filerne 
    læsOrdtilQuizlet = open(pathTranslations, "r", encoding="utf-8") 
    læsOrdtilQuizletlist = læsOrdtilQuizlet.readlines()         #Giver liste af indholdet
    læsOrdtilQuizlet.close()
    ##Del der formaterer  
    SkrivOrdtilQuizlet = open(pathTranslations, "w", encoding="utf-8")
    læsOrdtilQuizletlistformatted = []
    for word in læsOrdtilQuizletlist:
            læsOrdtilQuizletlistformatted.append(word.strip())  #fjerner \n fra list values og "\n" list values
    for word in læsOrdtilQuizletlistformatted:
        if word == "":
            læsOrdtilQuizletlistformatted.remove("")    #Fjerner "" list values
    læsOrdtilQuizletlistformatted = "\n".join(læsOrdtilQuizletlistformatted)
    SkrivOrdtilQuizlet.write(læsOrdtilQuizletlistformatted)
    SkrivOrdtilQuizlet.close() 
    ####################################################################################### DEL DER MERGER 
    #bugged i denne version  
    Fil1 = open(txtfilepath, "r", encoding="utf-8")
    Fil2 = open(pathTranslations, "r", encoding="utf-8")   

    list1 = Fil1.readlines()    #list med tyske ord
    list2 = Fil2.readlines()       #list fra FileName translations.txt

    #Del der formaterer liste 1 (de tyske ord), så det udenlukkende er ordene
    list1formatted = []
    for word in list1:
        list1formatted.append(word.strip())  #fjerner \n fra list values og "\n" list valuesFil1.close()

    #Del der formaterer liste 2, så det udenlukkende er ordene
    list2formatted = []
    for word in list2:
        list2formatted.append(word.strip())  #fjerner \n fra list values og "\n" list valuesFil1.close()

    NewList1 = []        #Alle de tyske ord med et tab character for enden
    NewList2 = []        #Alle de danske ord med et newline character for enden

    #Tilføjer et tab character for enden af hvert af de tyske ord
    for word in list1formatted:     #List1 ændres så ordene har et tab character for enden
        word = word + "\t"
        NewList1.append(word)
    #Tilføjer et new line character for enden af hvert dansk ord
    for word in list2formatted:     #List2 ændres, så ordene har et newline character for enden
        word = word + "\n"
        NewList2.append(word)


    merged_list = []    #Laver en list of tuples fra NewList1(tyske ord med tab på enden) og Newlist2(danske ord med newline på enden)
    Final_list = []     #laver en list med ordene inde i de tuples fra merged_list
    for i in range(len(list1)):
        try:
            TupList = (NewList1[i], NewList2[i])
            merged_list.append(TupList)
        except IndexError:
            TupList = (NewList1[i], "TransError")
    
    for tuple in merged_list:
    #    print(tuple)
        for word in tuple:
            Final_list.append(word) #Tager ordene fra tuples der er i merged_list og laver det om til en liste
    
    EndString = "".join(Final_list) #Laver en string ud af Final_list
    pyperclip.copy(EndString)
    TestFil = open(pathFinal, "w", encoding="utf-8")        
    TestFil.write(EndString)
    TestFil.close
    
    #SKAL DUPPLIKERES FOR AT VIRKE ? ? ? ? ? ? ? ?   ? ? ? 
    EndString = "".join(Final_list) #Laver en string ud af Final_list
    pyperclip.copy(EndString)
    TestFil = open(pathFinal, "w", encoding="utf-8")        
    TestFil.write(EndString)
    TestFil.close

    ################################WebbrowserdelQuizlet
    webbrowser.open("https://quizlet.com/create-set")

    def wait_on_browser():      #Du er genial brother
        try:
            Import = pyautogui.center(pyautogui.locateOnScreen(".img\\ImportQuizlet.PNG", confidence=0.4))
        except TypeError:
            time.sleep(0.1)
            wait_on_browser()
    wait_on_browser()      #Tror den laver dobbelt



    ##############Trykker på import from word, excel, google docs, etc.
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

    #####Choose language på Quizlet virker    trykker først venstre side
    ChooseLanguage = Locator(".img\\ChooseLanguage.PNG", 0.4)
    ChooseLanguage.wait_n_locate_click()
    time.sleep(0.2)
    pyautogui.typewrite(languagefrom)      
    time.sleep(0.5)
    pyautogui.hotkey("enter")
    time.sleep(0.5)

    #####Choose language på Quizlet virker    trykker siden der er tilbage
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
savedlangoptions = []       #Skal bruges til at sætte value. index[0] vil altid være languagefrom
def options_look():
    if os.path.isfile(".\\Options.txt"):
        with open(".\\Options.txt", "r", encoding="utf-8") as f:
            Options = f.readlines()
            for word in Options:
                if word[:11] in ["Translating"]:        #Translating from language: " + languagefrom[-1] + "\n" + "Translating to language:
                    #pathregex = re.compile(r"""(: (\w)+)""", re.DOTALL)      #match =": German" fikser bare til sidst
                    pathregex = re.compile(r"""(:\s)(\w+)""", re.DOTALL)
                    mo = pathregex.search(word)
                    #mostrip=mo.group(1).replace(": ", "")
                    mostrip=mo.group(2)
                    savedlangoptions.append(mostrip)
                else:
                    pathregex = re.compile(r""" (\w\:(.)+)""", re.DOTALL)       #finds D:/ followed by anything
                    mo = pathregex.search(word)
                    mostrip = mo.group().strip()
                    savedoptions.append(mostrip)
options_look()
#Lader brugeren vælge en mappe
FileLog = []
def BrowseFolder():
    foldername = filedialog.askdirectory()  #filedialog.askdirectory(ingen parametre)
    if foldername == "":
        return
    elif foldername in FileLog:
        return
    else:
        FileLog.append(foldername)
        savedir.append(foldername)
    
    for file in FileLog: #######Visuel bug, den fjerner og tilføjer ikke hele tiden ny label
        if FileLog.count(foldername) == 1:
            try:
                label4.destroy()
            except NameError:
                try:
                    label.destroy()              
                except UnboundLocalError:
                    label = tk.Label(frame2, pady=5, text=file, fg="white", bg="gray")
                    label.pack(side=LEFT)

#Lader brugeren vælge Deepl.exe
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

    for file in FileLog2:       #######Visuel bug, den fjerner og tilføjer ikke hele tiden ny label
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

#Frames til at holde radiobuttons
frame4 = tk.Frame(canvas, height=500, width=700, bg="#263D42")    #holder translate from
frame4.place(y=2, x=3)
labelf4 = ttk.Label(frame4, text="Translate from:", style='Wild.TLabel')
labelf4.pack()

frame5 = tk.Frame(canvas, height=500, width=700, bg="#263D42")    #holder translate to
frame5.place(y=2, x=86)
labelf5 = ttk.Label(frame5, text="Translate to:", style='Wild.TLabel')
labelf5.pack()

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
        #Languagefrom og languageto bliver ved med at appende når man trykker på knapperne
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

#Sætter sprogene til hvad de var sat til baseret på Options.txt
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

#frame der holder knapper til at browse filer
frame = tk.Frame(canvas, height=100, width=700, bg="gray")
frame.place(x=210, rely=0.7)
#frame2 holder label der har txtfolder til onenote filer
frame2 = tk.Frame(root, height=100, width=355, bg="gray")
frame2.pack(side=LEFT, fill=BOTH, expand=YES)
#frame3 holder label der har txtfolder til deepl.exe
frame3 = tk.Frame(root, height=100, width=355, bg="gray")
frame3.pack(side=RIGHT, fill=BOTH, expand=YES)


#Knapper til at browse filer
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
                elif (lambda newfile: txtfile[:-4] + " final.txt")(txtfile) in files:
                    continue
                elif txtfile[-4:] in [".txt"]:       
                    txtfile = txtfile[:-4]
                    OrdtilQuizlet(txtfile, savedir[0], savedlangoptions[0], savedlangoptions[-1])

                continue     

#Knap til at starte Quizlet funktionen
Start = OneNote = tk.Button(frame, text="Start the translating process and upload to Quizlet",
 padx=11, pady=5, fg="white", bg="#263D42", command = OrdtilQuizlet2)
Start.pack()


#Labels tydeliggører paths
labelOnenote = tk.Label(frame2, text="Path to your folder:", fg="white", padx=10, pady=5, bg="gray")
labelOnenote.pack(side=LEFT)

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

def save_options():             
    with open(".\\Options.txt", "w", encoding="utf-8") as f:         
        for word in savedoptions:                    
            if word[-4:] in [".exe"]:
                saveexe.append(word)
            else:
                savedir.append(word)
        f.write("Path to your txt files: " + savedir[0] + "\n" + "Path to your Deepl.exe: " + saveexe[0] + "\n"
                + "Translating from language: " + savedlangoptions[0] + "\n" + "Translating to language: " + savedlangoptions[-1] + "\n")
save_options()


