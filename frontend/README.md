# TinyML Math API Demo Frontend

This is a simple frontend for interacting with the TinyML Math API. It allows users to enter two numbers, select a mathematical operation, and see the computed result.

## Live Demo
You can access the frontend here: [TinyML Math Webpage](https://tiny-ml-math-webpage.onrender.com)

The backend API is hosted here: [TinyML Math API](https://tiny-ml-math-api.onrender.com)

## How It Works
1. Enter two numbers in the input fields.
2. Select an operation (Addition, Subtraction, Multiplication, or Division).
3. Click the **Calculate** button to send a request to the API.
4. The result will be displayed below the button.

## Code Overview

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Demo - TinyML Math</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            text-align: center;
            padding: 50px;
        }
        .container {
            max-width: 600px;
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        .btn-primary {
            background-color: #007BFF;
            border: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-4">TinyML Math API Demo</h1>
        <p>Enter two numbers and select an operation.</p>
        <input type="number" id="num1" class="form-control mb-2" placeholder="First Number">
        <input type="number" id="num2" class="form-control mb-2" placeholder="Second Number">
        <select id="operation" class="form-select mb-3">
            <option value="0">Addition</option>
            <option value="1">Subtraction</option>
            <option value="2">Multiplication</option>
            <option value="3">Division</option>
        </select>
        <button class="btn btn-primary" onclick="callAPI()">Calculate</button>
        <h3 class="mt-4">Result: <span id="result">-</span></h3>
    </div>
    <script>
        async function callAPI() {
            const num1 = document.getElementById("num1").value;
            const num2 = document.getElementById("num2").value;
            const operation = document.getElementById("operation").value;
            try {
                const response = await fetch(`https://tiny-ml-math-api.onrender.com/predict_math?a=${num1}&b=${num2}&operation=${operation}`, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                const data = await response.json();
                document.getElementById("result").innerText = data.result || "Error";
            } catch (error) {
                document.getElementById("result").innerText = "API Error";
            }
        }
    </script>
</body>
</html>
```

## Deployment
This frontend is hosted as a static site on Render. It communicates with the API using `fetch()` to send GET requests.

## Known Issues
- **CORS Policy Issue:** If the API request is blocked due to CORS, update the backend to include `Flask-CORS` to allow cross-origin requests.
- **Server Downtime:** The backend may take a few seconds to start if it's on a free Render plan.

## Contributing
Feel free to fork and modify the project. You can submit pull requests to improve functionality or styling.

## License
This project is open-source under the MIT License.

---

### Additional Notes
- If any issues arise with fetching results, inspect the console in the browser (`F12` -> Console tab) to debug API calls.
- For backend API details, check the [TinyML Math API GitHub Repository](https://github.com/lobsterhandz/Tiny_ML_Math_API).
