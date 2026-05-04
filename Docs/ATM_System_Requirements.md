# ATM System Requirements

## 1. Actors:

- Users 
- ATM System
- Bank System

## 2. Functional Requirements (testable statements)

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

## 3. Notes / Clarifications
- PIN validation is handled by the Bank System.
- Transaction approval depends on available balance and bank response.
- Session management includes timeout handling and re-authentication rules.

## 4. Edge Cases (Recommended Additions)
- If card is unreadable, system shall reject insertion and prompt retry.
- If Bank System is unavailable, system shall display service error and end session.
- If cash dispenser fails, system shall rollback transaction and notify user.
- If user enters invalid PIN format, system shall prompt re-entry.

## 5. Assumptions
- Bank System is always reachable unless explictly failed.
- ATM operates in real-time with network connectivity.
- One user session at a time.

## 6. Future Improvements 
- Add multi-language support
- Add biometric authentication
- Add mobile banking integration
- Add fraud detection rules