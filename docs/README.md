# 📌 TinyML Math API

## 🚀 Overview
The **TinyML Math API** is a Flask-based RESTful API that performs basic mathematical operations and leverages a **TinyML model** for predictions. It is backed by a **PostgreSQL database** and is deployed using **Render** with CI/CD automation via **GitHub Actions**.

## 🌍 Live API Deployment on RENDER
🔗 **Live API:** [https://tiny-ml-math-api.onrender.com](https://tiny-ml-math-api.onrender.com)

### **📌 Available API Endpoints**
| **Method** | **Endpoint** | **Description** |
|-----------|------------|----------------|
| **GET** | `/` | Health check – returns `Math API is running!` |
| **POST** | `/sum` | Perform addition (`{ "operand1": float, "operand2": float }`) |
| **GET** | `/sum/all` | Retrieve all stored sums |
| **GET** | `/sum/result/<int:target_result>` | Get sums filtered by result |
| **GET** | `/predict_math?a=10&b=2&operation=2` | Use ML model to predict (0=Add, 1=Subtract, 2=Multiply, 3=Divide) |

## 🛠️ Tech Stack
- **Flask** – Python web framework  
- **PostgreSQL** – Relational database  
- **SQLAlchemy & Alembic** – ORM & Database migrations  
- **TinyML** – Machine Learning model for math predictions  
- **Gunicorn** – WSGI HTTP Server  
- **Render** – Cloud deployment  
- **GitHub Actions** – CI/CD pipeline  

## 📂 Repository Structure
```
Tiny_ML_Math_API/
│── app.py                  # Main application file
│── config.py               # Configuration settings
│── database/               # Database models
│── migrations/             # Alembic migration files
│── requirements/           # Dependencies
│── tests/                  # Unit tests
│── .github/workflows/      # CI/CD pipeline
│── README.md               # Project documentation
```

## 📥 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/lobsterhandz/Tiny_ML_Math_API.git
cd Tiny_ML_Math_API
```

### **2️⃣ Create and Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements/requirements.txt
```

### **4️⃣ Set Up the Database**
```sh
flask db upgrade
```

### **5️⃣ Run the Flask Application**
```sh
flask run
```

## 🚀 Deployment Instructions
### **🔹 Pushing Changes to GitHub**
```sh
git add .
git commit -m "Updated API functionality"
git push origin feature/tests  # Change the branch if needed
```

### **🔹 Deploying to Render**
```sh
curl -X POST "https://api.render.com/deploy/srv-XXXXX?key=YYYYYY"
```

## 📌 GitHub Repository
🔗 **GitHub Repo:** [Tiny_ML_Math_API](https://github.com/lobsterhandz/Tiny_ML_Math_API)

##📌 Demonstrating PostgreSQL Data Retrieval

This API stores math operations in a PostgreSQL database hosted on Render. The following steps verify that data retrieval works correctly.

##1️⃣ **Storing Data in PostgreSQL**

To store an operation, send a request using the frontend:

Visit the live demo: TinyML Math Webpage

Input:

Number 1: 5
Number 2: 4
Operation: Addition

Click Calculate.

The result 9 will be stored in PostgreSQL.



---

##2️⃣ Retrieving Data from PostgreSQL

**Option 1: Web Browser (Simplest)**

Open the API endpoint:
👉 View Stored Data

Expected JSON response:

{
  "operations": [
    {
      "id": 1,
      "operand1": 5,
      "operand2": 4,
      "operation": "addition",
      "result": 9
    }
  ]
}

This confirms that data retrieval is working.


**Option 2: Postman (API Testing)**

Make a GET request to:

https://tiny-ml-math-api.onrender.com/sum/all

View the JSON response.


**Option 3: Terminal (cURL)**

Run the following:

curl -X GET "https://tiny-ml-math-api.onrender.com/sum/all" -H "Accept: application/json"


---

##📌 Notes

✅ This API is fully integrated with PostgreSQL.
✅ Data is stored and retrieved dynamically from the database.
