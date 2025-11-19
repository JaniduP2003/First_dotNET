# PyTest Quick Start Guide for .NET Core Web API Testing

This guide demonstrates how to perform black-box API testing on a .NET Core backend using PyTest.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: Check with `python3 --version` or `python --version`
- **pip**: Python package installer (usually comes with Python)
- **.NET SDK**: To run the .NET Core backend (check with `dotnet --version`)

## 🚀 Setup

### Step 1: Create a Python Virtual Environment

Creating a virtual environment isolates your Python dependencies from the system-wide packages.

```bash
# Navigate to the backend directory
cd /home/janidu/Documents/GitHub/First_dotNET/backend

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

After activation, your terminal prompt should be prefixed with `(venv)`.

### Step 2: Install Python Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:
- **pytest**: Testing framework
- **requests**: HTTP library for making API calls
- **pytest-mock**: Mocking library for PyTest

## ▶️ How to Run the Tests

### Step 1: Launch the .NET API Backend

Before running the tests, ensure your .NET API is running.

**Option A: Using dotnet run**
```bash
# In a separate terminal window, navigate to the backend directory
cd /home/janidu/Documents/GitHub/First_dotNET/backend

# Run the .NET application
dotnet run
```

**Option B: Using the published version**
```bash
# If you have a published version
cd /home/janidu/Documents/GitHub/First_dotNET/backend/published
./backend
```

The API should start and listen on `http://localhost:8080` (or the port specified in your `launchSettings.json`).

> **Note**: If your API runs on a different port, update the `base_url` fixture in `test_api_endpoints.py`.

### Step 2: Run the PyTest Suite

With your virtual environment activated and the API running:

```bash
# Run all tests with verbose output
pytest test_api_endpoints.py -v

# Run tests with detailed output including print statements
pytest test_api_endpoints.py -v -s

# Run tests and show a coverage report (if pytest-cov is installed)
pytest test_api_endpoints.py -v --tb=short

# Run a specific test class
pytest test_api_endpoints.py::TestGamesEndpoint -v

# Run a specific test case
pytest test_api_endpoints.py::TestGamesEndpoint::test_get_games_returns_200_ok -v
```

## 📊 Understanding the Test Output

PyTest will display results in your terminal:

```
========================= test session starts ==========================
collected 9 items

test_api_endpoints.py::TestGamesEndpoint::test_get_games_returns_200_ok PASSED     [ 11%]
test_api_endpoints.py::TestGamesEndpoint::test_get_games_returns_json_list PASSED  [ 22%]
test_api_endpoints.py::TestGamesEndpoint::test_get_games_list_structure PASSED     [ 33%]
test_api_endpoints.py::TestGamesEndpoint::test_get_games_handles_500_error PASSED  [ 44%]
...

========================== 9 passed in 0.45s ===========================
```

- ✅ **PASSED**: Test succeeded
- ❌ **FAILED**: Test failed (assertion error or exception)
- ⚠️ **SKIPPED**: Test was skipped
- **ERROR**: Error during test collection or setup

## 📁 Project Structure

```
backend/
├── test_api_endpoints.py    # PyTest test suite
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── venv/                     # Virtual environment (created by you)
└── ...                       # Your .NET backend files
```

## 🧪 Test Coverage

The test suite includes:

1. **Basic HTTP Tests**:
   - Verify `/games` endpoint returns 200 OK
   - Verify `/games` returns a JSON list
   - Verify `/genres` endpoint returns 200 OK

2. **Mocked Error Scenarios**:
   - Simulate 500 Internal Server Error
   - Simulate network timeout

3. **Health Check Tests**:
   - Verify API is accessible and running

## 🛠️ Customization

### Change API Base URL

If your API runs on a different host or port, modify the `base_url` fixture in `test_api_endpoints.py`:

```python
@pytest.fixture
def base_url():
    return "http://localhost:8080"  # Change port here
```

### Add More Tests

Follow the existing pattern to add new test methods:

```python
def test_your_new_test(self, base_url, api_headers):
    response = requests.get(f"{base_url}/your-endpoint", headers=api_headers)
    assert response.status_code == 200
```

## 🐛 Troubleshooting

### Issue: "Cannot connect to API"
- **Solution**: Ensure the .NET backend is running on the expected port.
- **Check**: Run `curl http://localhost:5000/games` to verify API is accessible.

### Issue: "ModuleNotFoundError: No module named 'pytest'"
- **Solution**: Activate your virtual environment and reinstall dependencies:
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### Issue: Tests fail with connection errors
- **Solution**: Verify the API is running and the port number is correct in `test_api_endpoints.py`.

## 📚 Additional Resources

- [PyTest Documentation](https://docs.pytest.org/)
- [Requests Library Documentation](https://requests.readthedocs.io/)
- [pytest-mock Documentation](https://pytest-mock.readthedocs.io/)

## 🎯 Next Steps

1. Extend the test suite to cover POST, PUT, and DELETE operations
2. Add tests for authentication and authorization
3. Implement data validation tests
4. Create fixtures for test data setup and teardown
5. Integrate with CI/CD pipelines

---

**Happy Testing! 🚀**
