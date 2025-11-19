# PyTest University Assignment - Complete Testing Suite

## 📚 Project Overview

This project demonstrates a comprehensive PyTest testing suite for a .NET Core Web API. It showcases all key PyTest features required for a university assignment:

- ✅ **Assertions** - Multiple assertion types and patterns
- ✅ **Fixtures** - Reusable test data and objects
- ✅ **Parameterized Tests** - Testing with multiple input combinations
- ✅ **Mocking** - Mocking external dependencies and API calls
- ✅ **Test Coverage** - Measuring and reporting code coverage
- ✅ **HTML Reporting** - Generating professional test reports
- ✅ **Runnable Example** - Complete game service module with tests

---

## 📊 Coverage Reports (Industry Standard & Impressive!)

### Where to Find Your Coverage Reports:

**🎯 Interactive HTML Coverage Report (RECOMMENDED)**
- **Location**: `htmlcov/index.html`
- **How to view**: 
  ```bash
  xdg-open htmlcov/index.html  # Linux
  open htmlcov/index.html      # macOS
  ```
- **Features**: 
  - Visual line-by-line coverage
  - Color-coded coverage indicators
  - Shows exactly which lines were executed
  - Professional presentation for assignments

**📟 Terminal Coverage Report**
- Shows coverage summary after running: `pytest test_unit.py -v`
- Displays at the end of test output (not visible when piping to `head`)

### How to Generate/View Coverage:

```bash
# Option 1: Run tests and see terminal coverage at the end
pytest test_unit.py -v

# Option 2: Generate fresh HTML coverage report
pytest --cov=. --cov-report=html --cov-report=term-missing

# Option 3: View existing HTML coverage report
xdg-open htmlcov/index.html

# Option 4: Generate coverage report with missing lines highlighted
pytest --cov=game_service --cov-report=term-missing
```

**⚠️ Important**: When you run `pytest test_unit.py -v --tb=short | head -100`, the `| head -100` pipe cuts off the output before the coverage report appears. The coverage report prints **at the very end** of the test run, so use the HTML report or run without piping to see it!

### Example Coverage Output:

When you run `pytest test_unit.py -v` (without piping), you'll see this at the end:

```
---------- coverage: platform linux, python 3.x.x -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
game_service.py              XX      X    XX%
test_unit.py                XXX      0   100%
---------------------------------------------
TOTAL                       XXX      X    XX%
```

---

## 📂 Project Structure

```
backend/
├── game_service.py              # Main application module (GameService class)
├── conftest.py                  # PyTest fixtures and configuration
├── test_unit.py                 # Comprehensive unit tests
├── test_api_endpoints.py        # Integration tests for API
├── requirements.txt             # Python dependencies
├── pytest.ini                   # PyTest configuration
├── pytest.ini                   # PyTest configuration
├── PYTEST_GUIDE.md              # Detailed testing guide
└── htmlcov/                     # Coverage HTML reports
    └── index.html               # Main coverage report
```

---

## 🚀 Quick Start

### 1. Prerequisites

```bash
# Required software
- Python 3.9 or higher
- pip (Python package manager)
- .NET SDK 9.0 (for integration tests)
```

### 2. Setup Environment

```bash
# Navigate to project directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### Run All Tests

```bash
# Run all tests with verbose output
pytest -v

# Run only unit tests
pytest test_unit.py -v

# Run only integration tests (requires API running)
pytest test_api_endpoints.py -v -m integration

# Run specific test class
pytest test_unit.py::TestCalculator -v

# Run specific test
pytest test_unit.py::TestCalculator::test_addition -v
```

### Run Tests by Markers

```bash
# Run only unit tests
pytest -m unit -v

# Run only integration tests
pytest -m integration -v

# Run slow tests
pytest -m slow -v

# Exclude slow tests
pytest -m "not slow" -v
```

### Run Parameterized Tests

```bash
# Run all parameterized tests
pytest test_unit.py::TestParameterizedCalculator -v
```

---

## 📊 Test Coverage

### Generate Coverage Report

```bash
# Run tests with coverage
pytest --cov=. --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=. --cov-report=html

# Open HTML report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows

# Generate coverage report using coverage.py
coverage run -m pytest test_unit.py
coverage report
coverage html
```

### Coverage Commands

```bash
# Run with coverage and show missing lines
pytest --cov=. --cov-report=term-missing --cov-report=html

# Generate XML report (for CI tools)
pytest --cov=. --cov-report=xml

# Set minimum coverage threshold
pytest --cov=. --cov-fail-under=80
```

---

## 📝 HTML Test Reports

### Generate HTML Report

```bash
# Generate standalone HTML report
pytest --html=reports/test_report.html --self-contained-html

# Generate with CSS assets
pytest --html=reports/test_report.html

# Open the report
open reports/test_report.html  # macOS
xdg-open reports/test_report.html  # Linux
start reports/test_report.html  # Windows
```

---

## 🎯 Key PyTest Features Demonstrated

### 1. Assertions (`test_unit.py`)

```python
# Basic assertions
assert result == expected
assert value > 0
assert isinstance(obj, type)

# Collection assertions
assert len(items) == 4
assert item in collection

# String assertions
assert "substring" in string
assert string.startswith("prefix")

# Approximate comparisons
assert value == pytest.approx(3.14, rel=1e-2)

# Exception assertions
with pytest.raises(ValueError) as exc_info:
    function_that_raises()
assert "error message" in str(exc_info.value)
```

**Examples in code:**
- `TestGameServiceBasics`: Game service method assertions
- `TestComplexAssertions`: Advanced assertion patterns
- `TestExceptionHandling`: Exception testing

### 2. Fixtures (`conftest.py`)

```python
@pytest.fixture
def sample_data():
    """Provide test data."""
    return {"key": "value"}

@pytest.fixture
def game_service():
    """Provide GameService instance."""
    return GameService()

@pytest.fixture(scope="session")
def test_config():
    """Session-scoped configuration."""
    return {"timeout": 5}
```

**Examples in code:**
- `game_service`: Provides GameService instance
- `sample_game_data`: Test data fixture
- `sample_games_list`: List of test games
- `test_config`: Session-scoped config
- `temp_game_data`: Temporary file fixture

### 3. Parameterized Tests

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
```

**Examples in code:**
- `TestGameServiceBasics`: 15+ parameterized test cases
- `test_calculate_game_score`: Game score calculations with multipliers
- `test_format_game_name`: Game name formatting variations
- `test_is_game_expensive`: Price threshold testing

### 4. Mocking

```python
# Using unittest.mock
@patch('module.requests.get')
def test_with_mock(mock_get):
    mock_get.return_value.json.return_value = {...}
    result = function()
    mock_get.assert_called_once()

# Using pytest-mock
def test_with_mocker(mocker):
    mock = mocker.patch('module.function')
    mock.return_value = "mocked"
```

**Examples in code:**
- `TestGameServiceMocking`: Mocking API calls
- `test_get_all_games_mocked`: Mock HTTP responses
- `test_get_game_by_id_success`: Mock successful API
- `test_get_game_by_id_not_found`: Mock 404 errors
- `test_mock_with_pytest_mock`: Using pytest-mock plugin

### 5. Test Organization

```python
@pytest.mark.unit
class TestGameService:
    """Unit tests for game service."""
    pass

@pytest.mark.integration
def test_api_endpoint():
    """Integration test."""
    pass

@pytest.mark.slow
def test_slow_operation():
    """Slow test."""
    pass
```

---

## 🎯 Key PyTest Features Demonstrated

### Example 1: Basic Assertion Test

```python
def test_format_game_name(game_service):
    """Test game name formatting."""
    result = game_service.format_game_name("super mario")
    assert result == "Super Mario"
    assert result.startswith("Super")
```

### Example 2: Parameterized Test

```python
@pytest.mark.parametrize("base_score,multiplier,expected", [
    (100, 1.0, 100.0),
    (100, 2.0, 200.0),
    (50, 1.5, 75.0),
])
def test_calculate_game_score(game_service, base_score, multiplier, expected):
    """Test game score calculation with multiple inputs."""
    assert game_service.calculate_game_score(base_score, multiplier) == expected
```

### Example 3: Mocking Test

```python
@patch('game_service.requests.get')
def test_get_games_mocked(mock_get, game_service):
    """Test API call with mock."""
    mock_response = Mock()
    mock_response.json.return_value = [{"id": 1, "name": "Game 1"}]
    mock_get.return_value = mock_response
    
    result = game_service.get_all_games()
    assert len(result) == 1
    mock_get.assert_called_once()
```

### Example 4: Exception Test

```python
def test_negative_score_raises_error(game_service):
    """Test exception handling."""
    with pytest.raises(ValueError, match="Base score cannot be negative"):
        game_service.calculate_game_score(-10, 2.0)
```

---

## 📊 Expected Coverage Report

After running tests with coverage, you should see:

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
game_service.py              XX      X    XX%   XX-XX
test_unit.py                XXX      0   100%
-------------------------------------------------------
TOTAL                       XXX      X    XX%
```

**Note:** Actual coverage percentages will vary based on which code paths are executed during tests.

---



## 🛠️ Useful Commands Reference

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html --cov-report=term-missing

# Generate HTML report
pytest --html=reports/test_report.html --self-contained-html

# Run specific markers
pytest -m unit -v
pytest -m integration -v

# Run with specific Python version
python3.11 -m pytest -v

# Show available fixtures
pytest --fixtures

# Show available markers
pytest --markers

# Collect tests without running
pytest --collect-only

# Run tests in parallel (install pytest-xdist)
pytest -n auto

# Stop on first failure
pytest -x

# Show local variables on failure
pytest -l

# Increase verbosity
pytest -vv

# Quiet mode
pytest -q
```

---

## 📚 Additional Resources

- [PyTest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [pytest-mock Documentation](https://pytest-mock.readthedocs.io/)

---

## 🐛 Troubleshooting

### Issue: Tests fail with "Connection Refused"

**Solution**: Make sure the .NET API is running on port 8080:
```bash
dotnet run
```

### Issue: Coverage report shows 0%

**Solution**: Ensure you're running coverage from the correct directory:
```bash
cd backend
pytest --cov=. --cov-report=term
```

### Issue: pytest-html not generating report

**Solution**: Create reports directory and install plugin:
```bash
mkdir -p reports
pip install pytest-html
pytest --html=reports/test_report.html --self-contained-html
```

---



---

## 👨‍💻 Author

Created for university PyTest assignment demonstrating comprehensive testing practices.

## 📄 License

This project is for educational purposes.

---

**Happy Testing! 🎉**
