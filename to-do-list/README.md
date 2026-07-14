# Simple To-Do List (Python)

## Project Description
This is a simple command-line To-Do List application written in Python. It allows users to add tasks, view all saved tasks, and exit the program. The tasks are stored in a Python list while the program is running.

## Features
- Add new tasks
- View all tasks
- User-friendly menu
- Handles invalid menu choices
- Simple and easy-to-understand code

## Requirements
- Python 3.x

## How to Run
1. Install Python 3 on your computer.
2. Save the program as `todo_list.py`.
3. Open Command Prompt or Terminal.
4. Navigate to the folder where the file is saved.
5. Run the program using:

```bash
python todo_list.py
```

## Menu Options
### 1. Add Task
Allows the user to enter a new task and saves it in the task list.

### 2. View Tasks
Displays all the tasks currently stored in the list. If there are no tasks, the program displays a message saying the list is empty.

### 3. Exit
Closes the application.

## Example Output

```
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit

Enter your choice (1-3): 1
Enter a task: Finish Python assignment
Task added successfully!

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Exit

Enter your choice (1-3): 2

Your Tasks:
1. Finish Python assignment
```

## Project Structure

```
project-folder/
│
├── todo_list.py
└── README.md
```

## Future Improvements
- Delete a task
- Edit a task
- Mark tasks as completed
- Save tasks in a file so they remain after closing the program
- Add due dates and priorities

## Author
**Kashaf Tanveer**

## License
This project is free to use for learning and educational purposes.
