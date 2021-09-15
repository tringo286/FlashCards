https://github.com/tringo286/Team-7/
Tri Ngo tringo286
Mary Markart marymarkart

Date: September 14th, 2021

Product Name: ?

Problem Statement: 

Non-Functional Requirements: 

**Account signup**

## Summary

Creating an account for a new user

## Actors

The user

## Preconditions

* The user does not already have an account
## Triggers

The user clicks “Sign Up”

## Primary Sequence

1. User clicks “Sign Up Now”
2. The user enters the email address in the email address text field
3. System checks that email address has not already been used
4. The user enters username in the username text field
5. System checks that username is available
6. The user enters the password in the password text field
7. The user enters password again the password verification text field
8. System checks that passwords entered are the same
9. The user clicks a button to submit 
10. The system creates a new user account

## Primary Postconditions

* The new user account is in the system 
* The user is able to log in

## Alternate Sequences

The email address entered is already in use 

* The system displays an error message to the user*
* The system prompts the user to enter a different email address

The username is not available

* The system displays an error message to the user
* The system prompts the user to enter a different username

The passwords entered do not match

* The system displays an error message to the user 
* The system prompts the user to retype both passwords

### Alternate Trigger

### Alternate PostCondition



**Delete account**

## Summary:

Delete an account 

## Actors

The user

## Preconditions

 The user has an active account

## Triggers:

The user click “Delete my account”

## Primary Sequence

1. The user clicks “Delete my account” from the Account page
2. The system prompts the user to confirm they want to delete their account
3. User confirms they would like to delete their account
4. The system removes the account from the database

## Primary Postconditions

* The user cannot log in
* The account is no longer valid in the system

## Alternate Sequences

The user decides not to delete their account* 

* The user clicks “Delete my account” from the Account page 
* System prompts the user to confirm they want to delete their account
* User clicks “Cancel”

### Alternate Trigger

The user clicks the “Cancel” button

### Alternate PostConditions

* The user’s account is still accessible* The account remains in the system

**Account Login**

## Summary

Log into user account

## Actors

The user

## Preconditions* 

The user must have an active account

## Triggers

The user clicks “Login”

## Primary Sequence

1. The user clicks “Login”
2. The user enters their email address
3. The user enters their password
4. The user clicks “Sign in”
5. The system checks if the user’s email address and password are valid
6. The system displays a successful login page

## Primary Postconditions 

The user is now logged into their account

## Alternate Sequences

The user’s email address is not valid 

* The System displays an error message that the email address is not valid* 
* The system prompts the user to enter a different email address

The user’s password is wrong

* The system displays an error message that the email address is not valid
* The system prompts the user to enter the correct password

### Alternate Trigger

The user enters the wrong email address or password

### Alternate PostConditions 

* The user is not able to login to their account

**Account Logout** 

## Summary

The user logs out of their account

## Actors

The user

## Preconditions* 

* The user has an account and is logged into it

## Triggers

The user clicks “Logout”

## Primary Sequence

1. The user clicks “Logout”
2. The system logs the user out

## Primary Postconditions 

* The user no longer has access to their account
