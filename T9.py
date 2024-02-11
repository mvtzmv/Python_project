class Node:
    def __init__(self):
        self.children = dict()
        self.words = set()
# definiujemy klase Note i w konstruktorze tworzymy sobie parametry
# word - słowa a children to podpowiedzi słów

class T9Dictionary:

    def __init__(self):
        self.root = Node()
#mamy zmienną root i ją definiujemy
    def wordToDigits(self, word):
        # przypisanie liter do numerów na klawiaturze
        digits_in_word = ''
        for character in word:
            if (character >= 'a' and character <= 'c'):
                digits_in_word = digits_in_word + '2'
            elif (character >= 'd' and character <= 'f'):
                digits_in_word = digits_in_word + '3'
            elif (character >= 'g' and character <= 'i'):
                digits_in_word = digits_in_word + '4'
            elif (character >= 'j' and character <= 'l'):
                digits_in_word = digits_in_word + '5'
            elif (character >= 'm' and character <= 'o'):
                digits_in_word = digits_in_word + '6'
            elif (character >= 'p' and character <= 's'):
                digits_in_word = digits_in_word + '7'
            elif (character >= 't' and character <= 'v'):
                digits_in_word = digits_in_word + '8'
            elif (character >= 'w' and character <= 'z'):
                digits_in_word = digits_in_word + '9'

        return digits_in_word

    def prepareDictionary(self, filename):
        with open(filename) as file:
            for word in file:
                self.insertWord(word)
#zaciągamy nasz słownik
    def insertWord(self, word):
        word = word.lower()
        word = word.rstrip()
        word_in_digits = self.wordToDigits(word)
        word_in_digits_length = len(word_in_digits)

        current_node = self.root
        word_exists = True
        for i in range(word_in_digits_length):
            current_digit = int(word_in_digits[i])

            # Sprawdzamy czy w slowniku dzieci aktualnego wezla znajduje sie dana cyfra (klucz)
            if current_digit in current_node.children and word_exists:

                # Znalezlismy dany klucz wsrod dzieci, dlatego mozemy przejsc do przeszukiwania dzieci dla kolejnej cyfry (klucza)
                current_node = current_node.children[current_digit]

                # Jesli cyfra, ktora aktualnie sprawdzalismy jest ostatnia dla danego slowa
                # to sprawdzamy czy dodawane slowo (word) znajduje sie juz w zbiorze slow
                if i == word_in_digits_length - 1 and word not in current_node.words:
                    current_node.words.add(word)

                continue

            # Jesli co najmniej raz nie udalo sie znalezc dziecka z danym kluczem, to ta czesc bedzie sie wykonywala do konca

            word_exists = False
            current_node.children[current_digit] = Node()
            if i == word_in_digits_length - 1:
                current_node.children[current_digit].words.add(word)

            current_node = current_node.children[current_digit]

            # ------------- End of loop ---------------

    def showStartingWith(self, word_in_digits):
        word_in_digits_length = len(word_in_digits)

        wordsList = []
        current_node = self.root
        for i in range(word_in_digits_length):
            current_digit = int(word_in_digits[i])

            # Jesli w mapie dzieci nie ma dziecka o danej cyfrze(kluczu), to z pewnoscia nie uzyskamy podpowiedzi
            if current_digit not in current_node.children:
                return wordsList


            current_node = current_node.children[current_digit]

        def showWords(current_node):
            for word in current_node.words:
                wordsList.append(word)
                # print(word)

            for key in current_node.children.keys():
                showWords(current_node.children[key])

        showWords(current_node)

        return wordsList


t9 = T9Dictionary()
t9.prepareDictionary('words10k.txt')

########################### TK INTER ########################
from tkinter import *


#wygląd apki + jej funckjonalność czyli co przypisujemy do czego
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("T9 dictionary")

        self.display = Entry(master)
        self.display.grid(column=0, row=0, columnspan=3, sticky=N + E + S + W)

        self.button_1 = Button(master, text="clear", command=lambda: self.click_event("C"))
        self.button_1.grid(column=0, row=1, sticky=N + E + W + S)
        # self.button_1.bind(1, lambda: self.click_event())

        self.button_2 = Button(master, text="2 abc", command=lambda: self.click_event("2"))
        self.button_2.grid(column=1, row=1, sticky=N + E + W + S)

        self.button_3 = Button(master, text="3 def", command=lambda: self.click_event("3"))
        self.button_3.grid(column=2, row=1, sticky=N + E + W + S)

        self.button_4 = Button(master, text="4 ghi", command=lambda: self.click_event("4"))
        self.button_4.grid(column=0, row=2, sticky=N + E + W + S)

        self.button_5 = Button(master, text="5 jkl", command=lambda: self.click_event("5"))
        self.button_5.grid(column=1, row=2, sticky=N + E + W + S)

        self.button_6 = Button(master, text="6 mno", command=lambda: self.click_event("6"))
        self.button_6.grid(column=2, row=2, sticky=N + E + W + S)

        self.button_7 = Button(master, text="7 pqrs", command=lambda: self.click_event("7"))
        self.button_7.grid(column=0, row=3, sticky=N + E + W + S)

        self.button_8 = Button(master, text="8 tuv", command=lambda: self.click_event("8"))
        self.button_8.grid(column=1, row=3, sticky=N + E + W + S)

        self.button_9 = Button(master, text="9 wxyz", command=lambda: self.click_event("9"))
        self.button_9.grid(column=2, row=3, sticky=N + E + W + S)

        self.listbox = Listbox(master)
        self.listbox.grid(column=0, row=4, sticky=N + E + W + S, columnspan=3)

        for row in range(5):
            master.rowconfigure(row, weight=1)

        for column in range(3):
            master.columnconfigure(column, weight=1)

    def click_event(self, key):
        if key == "C":
            self.display.delete(0, END)
            self.listbox.delete('0', 'end')
        else:
            self.listbox.delete(0, END)
            self.display.insert(END, key)
            words_list = t9.showStartingWith(self.display.get())

            for word in words_list:
                self.listbox.insert(END, word)


root = Tk()
app = Calculator(root)
root.mainloop()