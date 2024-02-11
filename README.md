
# T9 Dictionary Application

Author: Maria Żuchowska

## Overview

This application is a T9 predictive text dictionary implemented in Python. It utilizes the T9 (Text on 9 keys) concept, a technology used in mobile phones to type text messages with a numeric keypad. This program converts words into their corresponding T9 numeric codes and vice versa, providing a list of possible word matches from a predefined dictionary file.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- A text file named `words10k.txt` containing the dictionary words (one word per line)

## Installation

No additional installation is required if Python and Tkinter are already installed on your system. Ensure that the `words10k.txt` dictionary file is in the same directory as the script for the application to function correctly.

## Usage

1. Run the T9 Dictionary script:
   ```
   python T9.py
   ```

2. The GUI window titled "T9 dictionary" will open.
3. Use the numeric buttons (2-9) on the interface to enter the T9 code. Each button corresponds to a set of letters, just like on a traditional mobile phone keypad.
4. As you type the numeric code, a list of possible matching words from the dictionary will appear in the list box below.
5. Press the "clear" button to reset and start a new word search.

## Code Overview

__init__ in Node class: This is the constructor for the Node class. It initializes each node with a children dictionary (to store child nodes) and a words set (to store words at each node).

__init__ in T9Dictionary class: This is the constructor for the T9Dictionary class. It initializes the root of the T9 dictionary as a new node.

```def wordToDigits```: This method converts a word into its corresponding T9 digit sequence. For each letter in the word, it assigns a digit (2-9) based on the T9 keypad layout.

```def prepareDictionary```: This method opens a file (containing words) and inserts each word into the T9 dictionary by calling insertWord.

```def insertWord```: This method inserts a word into the T9 dictionary. It first converts the word into a digit sequence and then traverses the trie structure of the dictionary, creating new nodes or adding the word to existing ones as needed.

```def showStartingWith```: Given a sequence of digits, this method finds all words in the dictionary that match this digit sequence. It traverses the trie structure based on the digit sequence and accumulates matching words.

```def showWords``` (nested in showStartingWith): A recursive helper function to traverse the trie and collect words that match the given digit sequence.

__init__ in Calculator class: This is the constructor for the Calculator (GUI) class. It sets up the Tkinter GUI, including buttons for digits and clear, an entry widget for display, and a listbox to show matching words.

```def click_event```: This method handles button click events in the GUI. It updates the display and the listbox with the appropriate digit or clears them if the 'clear' button is pressed.
