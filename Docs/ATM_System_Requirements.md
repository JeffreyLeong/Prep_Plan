ATM System Requirements

Actors:

- Users 
- ATM System
- Bank System

Requirements (testable statements)

- The ATM System shall accept a debit card and initiate a session.
- The ATM System shall prompt the User to enter a PIN after a debit card is inserted.
- The ATM System shall validate the entered PIN with the Bank System.
- The ATM System shall deny access after 3 consecutive invalid PIN attempts and retain the card.
- The ATM System shall process the selected transaction by sending a request to the Bank System.
- The ATM System shall display an error message if the Bank System declines the transaction.
- The ATM System shall dispense cash for approved withdrawal transactions within 10 seconds of approval.
- The ATM System shall update the User’s account balance after a successful transaction.
- The ATM System shall offer the User the option to print a receipt after each transaction.
- The ATM System shall allow the User to perform another transaction or end the session.
- The ATM System shall automatically end the session after 30 seconds of inactivity.