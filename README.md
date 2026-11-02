# Mini Task Tracker

A simple menu-based Python program for managing tasks from the command line. Tasks are saved to `tasks.json`, so they are still there the next time you run the program.

## Project Goal

Practice core Python skills: functions, lists and dictionaries, loops, input validation, error handling, and reading/writing JSON files.

## Features

- **Add** a task (empty titles are rejected); new tasks start as Pending
- **View** a numbered list showing each task as Pending or Done
- **Complete** a task by its number
- **Delete** a task by its number
- **Auto-save** to `tasks.json` after every add, complete, or delete
- **Auto-load** saved tasks at startup (starts with an empty list if the file is missing or corrupted)
- **Error handling** for blank titles, invalid menu choices, invalid task numbers, and a missing JSON file

## How to Run

### Locally
```bash
python mini_task_tracker.py
```

### In Google Colab
1. Upload `mini_task_tracker.py` to the Colab runtime (Files panel).
2. Run in a cell:
   ```python
   !python mini_task_tracker.py
   ```
   Or paste the code into a cell and call `main()`.

> **Note:** Files in a hosted Colab runtime are temporary. Download `tasks.json` or save it to Google Drive if you want to keep it. To test persistence, relaunch the program in the same active runtime.

## Example

```
--- TASK TRACKER ---
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
```

## Data Format

Each task is stored as:

```json
{"title": "Read notes", "done": false}
```

## Files

- `mini_task_tracker.py` - the program
- `README.md` - this file
- `tasks.json` - created automatically on first save
