# WebSocket Chat App - CI/CD with GitHub Actions

## Overview
This project is a WebSocket-based chat application that allows users to join rooms, send messages, and interact in real time. To ensure the reliability of the project, we have implemented a CI/CD pipeline using GitHub Actions. The pipeline automates testing before merging changes into the main branch.

## Features
- **WebSocket Communication**: Real-time messaging using Flask-SocketIO.
- **Chat Rooms**: Users can join different rooms and send messages.
- **Text Effects & Emojis**: Users can format messages and use emojis.
- **CI/CD Pipeline**: Automated testing and validation before deployment.

## Running the Project
### **1. Installation**
Ensure you have Python and dependencies installed:
```sh
pip install -r requirements.txt
```

### **2. Starting the WebSocket Server**
Run the server:
```sh
python app.py
```
Access the chat at:
```
http://127.0.0.1:5000/
```

### **3. Running Tests Locally**
To verify the integrity of the helper functions, run:
```sh
python -m unittest discover -s . -p "test_utils.py"
```

## CI/CD Pipeline (GitHub Actions)
### **Workflow Process**
- **Feature Branch (`feature/tests`)**: Runs automated tests before merging into `main`.
- **Tests Included:**
  - `sum_numbers()` (validates positive & negative sums)
  - `is_palindrome()` (checks for palindromes)
  - `factorial()` (ensures correct factorial calculation & raises errors on negatives)
  - `is_even()` (checks if a number is even)

### **Workflow Configuration (`.github/workflows/main.yml`)**
The CI/CD pipeline is triggered on:
- **Push to `feature/tests` branch**
- **Pull requests to `main` branch**

### **Running Tests in CI/CD**
1. GitHub automatically runs the tests when pushing changes to `feature/tests`.
2. If all tests pass, the branch is safe to merge into `main`.
3. If tests fail, the workflow prevents broken code from being deployed.

### **Deployment**
Once merged into `main`, the application can be deployed manually or via automated deployment steps added to the pipeline.

## Contributing
1. **Fork the repository**.
2. **Create a feature branch** (`feature/new-feature`).
3. **Commit and push changes**.
4. **Create a pull request (PR)**.
5. **Ensure tests pass before merging**.

## Future Enhancements
- **User Authentication**: Implement user accounts & authentication.
- **Database Integration**: Store chat messages persistently.
- **UI Improvements**: Enhance frontend UI with React.

## License
MIT License. Feel free to use and contribute!

