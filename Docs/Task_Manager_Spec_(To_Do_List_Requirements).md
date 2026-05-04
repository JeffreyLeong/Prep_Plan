# Task Manager Spec (To-Do List)

## 1. Actors
- User
- System

## 2. Functional Requirements

- The System shall allow the User to log in with a valid username and password.
- The System shall reject login attempts with invalid credentials.
- The System shall restrict access to tasks unless the User is authenticated.

- The System shall allow the User to create a task with a non-empty title.
- The System shall reject task creation if the title is empty.
- The System shall allow the User to view all existing tasks.
- The System shall allow the User to edit an existing task.
- The System shall allow the User to delete an existing task.
- The System shall notify the User if they attempt to edit or delete a task that does not exist.
- The System shall store all created tasks, including completed tasks.

## 3. Non-Functional Requirements

- The System shall respond to user actions within 2 seconds.
- The System shall persist task data between sessions.
- The System shall support at least one concurrent user session.
- The System shall lock the user session after 10 minutes of inactivity.

## 4. Edge Cases

- The System shall prevent duplicate task titles (optional constraint).
- The System shall handle invalid menu inputs without crashing.
- The System shall prevent division of null or undefined task references (i.e., invalid selections).

## 5. Assumptions

- The User has a valid account prior to using the system.
- The System uses persistent storage for saving tasks.