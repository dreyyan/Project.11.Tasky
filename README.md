# Tasky
_NLP-Based A.I. Task Assistant_

**Tasky** is a Python-based, NLP-powered task management system designed to simplify to-do list management through natural language commands. By leveraging intelligent text parsing, Tasky allows users to add, remove, update, and view tasks seamlessly without navigating complex menus. With robust input validation, it ensures smooth, error-free interactions, making it ideal for students, professionals, or anyone managing a busy schedule.

The primary purpose of Tasky is to provide an intuitive, efficient platform for organizing daily tasks, deadlines, and reminders, catering to both beginners and power users with its flexible command structure.

## FEATURES
✅ **Natural Language Commands** – Add, remove, update, and view tasks using intuitive text inputs.  
✅ **Intelligent Parsing** – Understands flexible phrasing for user-friendly task management.  
✅ **Minimalistic CLI** – Functional, lightweight command-line interface for quick interactions.  

## FUTURE IMPLEMENTATIONS
🚀 **Advanced Storage** – Integrate .csv or .sql for persistent storage and task analytics.  
🚀 **Graphical Interface** – Transition to a desktop or mobile app with a user-friendly GUI.  
🚀 **Enhanced Task Management** – Support task categories, priorities, and deadline tracking.  
🚀 **AI Enhancements** – Improve NLP capabilities for more complex command parsing.  

## UPDATES
🔄 Improved validation for task existence before updates or removals.  
🔄 Reduced redundant code for cleaner, faster performance.  

## PROJECT DETAILS
📌 **Author:** dreyyan  
📌 **Started:** 2025-04-05  
📌 **Finished:** 2025-04-06  

## TECH STACK
🛠️ **Language:** Python  
🛠️ **Libraries:** Standard Python libraries (NLP libraries TBD, e.g., spaCy or NLTK)  

## INSTALLATION
### Prerequisites
- Python 3.8 or higher
- Create a virtual environment (recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On Unix/Mac
  venv\Scripts\activate     # On Windows
  ```

### Install Dependencies
Tasky uses standard Python libraries for core functionality. If NLP libraries are added (e.g., spaCy, NLTK), install them:
```
pip install spacy nltk  # Example; adjust based on actual dependencies
```

### Verify Installation
Check Python version:
```
python --version
```

## USAGE
### Running the Application
Start Tasky from the project root:
```
python main.py
```

### Example Workflow
1. **Launch the App**: Run `python main.py` to start the CLI interface.
2. **Add Tasks**: Enter commands like "Add meeting at 3 PM" or "Create task: study for exam."
3. **Manage Tasks**: Use commands like "Remove task: meeting" or "Update study task to tomorrow."
4. **View Tasks**: Input "Show all tasks" to display your to-do list.

### Configuration
- No external configuration files required; settings are managed via the CLI.
- Ensure NLP models (if used) are downloaded (e.g., `python -m spacy download en_core_web_sm` for spaCy).

## DEBUGGING
For issues, check console output for errors related to input parsing or task management. Run with:
```
python main.py
```
Report issues via GitHub Issues for detailed troubleshooting.

## PROJECT STRUCTURE
- `main.py`: Entry point for the application (assumed; adjust based on actual structure).
- Other files may include modules for NLP parsing, task management, and CLI rendering (not specified in provided details).

## CONTRIBUTING
Contributions are welcome! Fork the repo, make changes, and submit a pull request:
1. Create a feature branch: `git checkout -b feature/new-feature`
2. Commit changes: `git commit -m "Add new feature"`
3. Push: `git push origin feature/new-feature`
4. Open a pull request

Report issues or suggest features via GitHub Issues.

## LICENSE
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.