Team 7 GitHub repository:

https://github.com/tringo286/Team-7/

Mary Markart - marymarkart (https://github.com/marymarkart)

Vladislav Semenyutin - skiffin-git (https://github.com/skiffin-git)

Tri Ngo  - tringo286 (https://github.com/tringo286)

Quan Le - QuanLew (https://github.com/QuanLew)

**Date: 9/14/2021**

**Product Name: StudyBuddy**

**Problem Statement: Group creates an app that helps students to study more effectively through memorization with flash cards, uploading and searching notes, and time management**

**Non-Functional Requirements:**

1. The system responds to each user input within 1 second
2. Must be able to run on web
3. The app will be in English

# Use Case 

## Mary

### **1) Test case name: Add To-Do tracker**

## Summary

Allow the user to add items to a to-do tracker

## Actors

The user

## Preconditions

 The user has an active account

## Triggers:

The user clicks "Create To-Do Tracker"

## Primary Sequence

1. The user clicks "Create To-Do Tracker" from Account page
2. The system displays a form for the user to add items to the To-Do tracker
3. The user enters the To-Do items into the item text field
4. The user clicks "Create Tracker"
5. The system displays the newly created To-Do tracker

## Primary Postconditions

* The user can view the To-Do tracker

## Alternate Sequences

The user marks a to-do list item as "Done"

* The user clicks a check box next to the To-Do list item
* The system removes the To-Do list item from the tracker
* The system displays a message letting the user know the item was marked completed successfully

### Alternate Trigger

The user clicks the checkbox next to To-Do tracker item

### Alternate PostConditions

* The To-Do tracker item is no longer displayed on the tracker

### **2) Test case name: Add tags to notes**

## Summary

The user can add tags to notes so that they are easy to find

## Actors

The user 

## Preconditions

 The user has an active account and is currently viewing notes

## Triggers:

The user clicks "Add a tag"

## Primary Sequence

1. The user clicks "Add a tag"
2. The user enters a tag they want associated with the current notes
3. The system groups the current notes with notes containing the same tag

## Primary Postconditions

* The current notes are now related to notes containing the same tag

## Alternate Sequences

The user removes a tag

* The user clicks "Delete Tag"
* The system removes the current notes from the group of notes containing the deleted tag

### Alternate Trigger

The user clicks "Delete Tag"

### Alternate PostConditions

* The current notes should no longer be related to the other notes containing the deleted tag

## Mary

### **3) Test case name:** Render markdown notes

## Summary

The system renders user input into markdown notes

## Actors

The user

## Preconditions

 The user has an active account

## Triggers:

The user creates a new note and writes markdown text

## Primary Sequence

1. The user types input in markdown format
2. The system renders the input into markdown style

## Primary Postconditions

* The notes are formatted using markdown style

## Alternate Sequences

None

### Alternate Trigger

None

### Alternate PostConditions

None

## Mary

### **4) Test case name:** Add flashcards to a mind map

## Summary

Allow the user to create a memory map using flashcards

## Actors

The user

## Preconditions

 The user has an active account

## Triggers:

The user clicks "Mind Map"

## Primary Sequence

1. The user clicks "Mind Map"
2. The system displays the current memory map
3. The user clicks the main idea associated with the flashcards they want to add
4. The system displays the main idea's map
5. The user clicks the main theme of the main idea they want to add the flashcards to
6. The system displays a list of flashcards that are not yet assigned to the mind map
7. The user selects the flashcards they want to add to that main theme and clicks "Save"
8. The system displays the updated mind map

## Primary Postconditions

* The mind map is updated with the desired flashcards

## Alternate Sequences

1. There are no unassigned flashcards
   * After the user clicks on a main theme, the system displays a message letting the user know there are no available flashcards

2. The user wants to add a main idea
   * The user clicks on "Mind Map"
   * The user clicks "Add Main Idea" and inputs a new Main idea

3. The user wants to add a main theme
   * The user clicks on "Mind Map"
   * The system displays Main Ideas
   * The user clicks on a main idea
   * The system displays the main idea's mind map
   * The user clicks "Add Theme" and inputs a new main theme

### Alternate Trigger

1. The user clicks on main theme when there are no unassigned flashcards
2. The user clicks on "Add Main Idea"
3. The user clicks on "Add Theme"

### Alternate PostConditions

1. The Mind map does not change
2. The Main idea is added to the list of main ideas
3. The Theme is added to the mind map

## Vlad

### 5) Test Case Name: Input a markdown file and output flash cards.

## Summary

input a markdown file and output flash cards

### Actors

* The user

* The web site

### Preconditions

* A web page dedicated for flash cards

### Triggers:

* User clicks on button named "create a flash card"

### Primary Sequence

1. User clicks on button named "Create a flash card"
2. Web site lets user to type two inputs: one for question and one for answer
3. User put his question and answer
4. User clicks on button named "save"
5. Web site creates a flash card with the inputs

### Primary Postconditions

* A flash card with question and answer

### Alternate Sequences

If user left one of inputs empty:

- Web site output an error message "empty question / answer side"

* Web site don't let user create a flash card until user input something

* User clicks on button called "Cancel" while writing inputs for a flash card

* Web site delete a flash card and returns to the previous step

### Alternate Trigger

* No alternate trigger

### Alternate Post Conditions

* No alternate post conditions

# Vlad

## 6) Test Case Name: Share flash cards with other people (add to their account)

### Summary

* Share flash cards with other people (add to their account)

### Actors

* The user 

* The web site

### Preconditions

* Have at least one flash card on user's #1 account

### Triggers:

User #1 clicks on button called "share flash cards" 

### Primary Sequence

1. User clicks on button called "share flash cards"
2. User selects flash cards that he/she wants to share
3. When user  finished selecting flash cards, he/she press on button called "Send"
4. Web site opens an input for the name of another account
5. Web site copy flashcards from user and add them to account with the name from input 

### Primary Postconditions

* User sent his flash card to a different account

### Alternate Sequences

If user not found:

* Web site outputs an error: "No account with such name was found."

If user with name from input already had those flash cards:

* Web site outputs an error: "The account with name 'name' already has these flash cards"

### Alternate Trigger

* no alternate trigger

### Alternate Post. Conditions

*  No alternate post conditions

# Vlad

## 7) Test Case Name: Change order of flash cards based on how often user got answer correct

## Summary

* Change order of flash cards based on how often user got answer correct

### Actors

* The user
* The web site

### Preconditions

* The user need to have at least 3 flash cards on his account
* (optional) In settings user's account should have a checkbox "on" for this feature

### Triggers:

* User checks the answer of a flash card

### Primary Sequence

1. When user checks answer, there should be two buttons: "Got it right!" or "Got it wrong"
2. User pressed on one of the buttons
3. If user pressed "Got it right" button => count adds +1 to correct answers and shuffle the card in the end of the deck
4. If user pressed "Got it wrong" button => this card shuffles in the middle (between this card and the end) of the deck.

### Primary Postconditions

* User's deck of flash cards shuffled according on which button he/she pressed

### Alternate Sequences

* If user didn't press any of the buttons and flips the card back => do nothing

### Alternate Trigger

* No alternate sequences

### Alternate Postconditions

* No alternate postconditions

# Vlad

## 8) Test Case Name: Create a pdf file of flash cards to print

### Summary

Create a pdf file of flash cards to print

### Actors

* The user
* The web site

### Preconditions

 User's account must have at least one flash card

### Triggers:

* User presses on button "download flash cards"

### Primary Sequence

1. User presses on button "download flash cards"
2. Web site create a pdf file and upload there all flash cards with questions and answers
3. Web site open a new tab and let user to download the file
4. User presses download, and get the pdf file

### Primary Postconditions

* User got a pdf file of all flash cards with questions and answers

### Alternate Sequences

* The button to "download" should appear only when at least one flash cards was created

### Alternate Trigger

* No alternate trigger

### Alternate Postconditions

* No alternate postconditions

## Tri

### **9) Test case name: Find text**

### Summary

A user who has logged in and entered a file can search text in that file.

### Actors

The user.

### Preconditions

The user has logged and entered a file. 

### Triggers:

User selects “search” option.

### Primary Sequence

1. System prompts the user to enter text. 
2. System searches for the text in the file.
3. System shows matching results.





















### Primary Postconditions

The system displays a message that searching is completed.









### Alternate Sequences

The user entered text that does not exist.

- The system displays a message that no matches were found. 
- The system prompts the user to enter a text that exists. 









### Alternate Trigger



### Alternate PostConditions



## Tri

### **10) Test case name: Rename files **

### Summary

A user who has logged in and can rename any file.

### Actors

The users.

### Preconditions

The user has logged in.

### Triggers:

User selects “rename” option.

### Primary Sequence

1. System shows files. 
2. User select a file and rename it.
3. System renames the file.



















### Primary Postconditions

The system displays a message that the file was renamed. 









### Alternate Sequences

The user entered an invalid name.

- The system displays an error message to the user.
- The system prompts the user to enter a valid name.









### Alternate Trigger



### Alternate PostConditions



## Tri

### **11) Test case name: Convert notes to pdf  **

### Summary

A user who has logged in can convert notes to pdf.

### Actors

The users

### Preconditions

The user has logged in.

### Triggers:

User selects “covert” option.

### Primary Sequence

1. System shows notes. 
2. User select notes to convert.
3. System converts the notes to pdf files.
4. System prompt locations to save the files. 
5. User select location. 



















### Primary Postconditions

System displays a message that notes were converted to the user.









### Alternate Sequences











### Alternate Trigger



### Alternate PostConditions



## Tri

### **12) Test case name: Share notes  **

### Summary

A user who has logged in can share notes with other account.

### Actors

The user.

### Preconditions

A user has logged in can share notes with other accounts. 

### Triggers:

User selects “share” option.

### Primary Sequence

1. System shows notes. 
2. User select notes to share.
3. System prompt the user to enter the account’s name.
4. System share the notes to other accounts.



















### Primary Postconditions

System displays a message that notes were shared other accounts.









### Alternate Sequences

The user entered an account's name that does not exist. 

- System displays an error message to the user. 
- System prompt the user to enter a valid account’s name.









### Alternate Trigger



### Alternate PostConditions



## Quan

### **13) Test case name:**

### Summary

#

### Actors

#

### Preconditions

#

### Triggers:

#

### Primary Sequence

#

#

#

#

#

#

#

#

#

#

### Primary Postconditions

#

#

#

#

#

### Alternate Sequences

#

#

#

#

#

### Alternate Trigger

#

### Alternate PostConditions

#

## Quan

### **14) Test case name:**

### Summary

#

### Actors

#

### Preconditions

#

### Triggers:

#

### Primary Sequence

#

#

#

#

#

#

#

#

#

#

### Primary Postconditions

#

#

#

#

#

### Alternate Sequences

#

#

#

#

#

### Alternate Trigger

#

### Alternate PostConditions

#

## Quan

### **15) Test case name:**

### Summary

#

### Actors

#

### Preconditions

#

### Triggers:

#

### Primary Sequence

#

#

#

#

#

#

#

#

#

#

### Primary Postconditions

#

#

#

#

#

### Alternate Sequences

#

#

#

#

#

### Alternate Trigger

#

### Alternate PostConditions

#

## Quan

### **16) Test case name:**

### Summary

#

### Actors

#

### Preconditions

#

### Triggers:

#

### Primary Sequence

#

#

#

#

#

#

#

#

#

#

### Primary Postconditions

#

#

#

#

#

### Alternate Sequences

#

#

#

#

#

### Alternate Trigger

#

### Alternate PostConditions

#
