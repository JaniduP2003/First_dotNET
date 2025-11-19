# PyTest University Assignment - Complete Testing Suite

## 📚 Project Overview

This project demonstrates a comprehensive PyTest testing suite for a .NET Core Web API. It showcases all key PyTest features required for a university assignment:

- ✅ **Assertions** - Multiple assertion types and patterns
- ✅ **Fixtures** - Reusable test data and objects
- ✅ **Parameterized Tests** - Testing with multiple input combinations
- ✅ **Mocking** - Mocking external dependencies and API calls
- ✅ **Test Coverage** - Measuring and reporting code coverage
- ✅ **HTML Reporting** - Generating professional test reports
- ✅ **CI Integration** - GitHub Actions workflow for automated testing
- ✅ **Runnable Example** - Complete game service module with tests

---

## 📂 Project Structure

```
backend/
├── game_service.py              # Main application module (GameService & Calculator)
├── conftest.py                  # PyTest fixtures and configuration
├── test_unit.py                 # Comprehensive unit tests
├── test_api_endpoints.py        # Integration tests for API
├── requirements.txt             # Python dependencies
├── pytest.ini                   # PyTest configuration
├── .coveragerc                  # Coverage configuration
├── README.md                    # This file
├── PYTEST_GUIDE.md             # Detailed testing guide
└── .github/
    └── workflows/
        └── pytest-ci.yml        # GitHub Actions CI workflow
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
- `TestCalculator`: Basic arithmetic assertions
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
- `calculator`: Provides Calculator instance
- `sample_game_data`: Test data fixture
- `sample_games_list`: List of test games
- `test_config`: Session-scoped config

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
- `TestParameterizedCalculator`: 20+ parameterized test cases
- `test_addition_parametrized`: Multiple input combinations
- `test_division_parametrized`: Division scenarios
- `test_power_parametrized`: Power calculations
- `test_calculate_game_score`: Game scoring variations

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
class TestCalculator:
    """Unit tests."""
    pass

@pytest.mark.integration
class TestAPI:
    """Integration tests."""
    pass

@pytest.mark.slow
def test_slow_operation():
    """Slow test."""
    pass
```

---

## 🔄 CI/CD Integration

### GitHub Actions Workflow

The `.github/workflows/pytest-ci.yml` file defines a complete CI pipeline:

**Features:**
- ✅ Runs on multiple Python versions (3.9, 3.10, 3.11, 3.12)
- ✅ Caches pip dependencies for faster builds
- ✅ Runs unit tests with coverage
- ✅ Runs integration tests (with .NET API)
- ✅ Generates coverage reports
- ✅ Uploads test artifacts
- ✅ Creates test summaries

**Workflow Jobs:**
1. **test**: Runs unit tests on multiple Python versions
2. **integration-test**: Runs integration tests with live API
3. **coverage-report**: Generates and uploads coverage reports

### Triggering the Workflow

```bash
# Push to trigger CI
git add .
git commit -m "Add comprehensive PyTest suite"
git push origin test-api-pytest

# Manual trigger via GitHub Actions UI
# Go to: Repository → Actions → PyTest CI → Run workflow
```

### Viewing Results

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Select the latest workflow run
4. View test results, coverage, and artifacts

---

## 📖 Test Examples

### Example 1: Basic Assertion Test

```python
def test_addition(calculator):
    """Test basic addition."""
    result = calculator.add(5, 3)
    assert result == 8
    assert result > 0
```

### Example 2: Parameterized Test

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
])
def test_addition_params(calculator, a, b, expected):
    """Test addition with multiple inputs."""
    assert calculator.add(a, b) == expected
```

### Example 3: Mocking Test

```python
@patch('game_service.requests.get')
def test_get_games_mocked(mock_get, game_service):
    """Test API call with mock."""
    mock_get.return_value.json.return_value = [{"id": 1}]
    result = game_service.get_all_games()
    assert len(result) == 1
    mock_get.assert_called_once()
```

### Example 4: Exception Test

```python
def test_division_by_zero(calculator):
    """Test exception handling."""
    with pytest.raises(ValueError, match="divide by zero"):
        calculator.divide(10, 0)
```

---

## 📊 Expected Coverage Report

After running tests with coverage, you should see:

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
game_service.py              45      2    96%   78-79
test_unit.py                180      0   100%
-------------------------------------------------------
TOTAL                       225      2    99%
```

---

## 🎓 Assignment Checklist

- [x] **Assertions**: Multiple types demonstrated in `TestCalculator` and `TestComplexAssertions`
- [x] **Fixtures**: 10+ fixtures in `conftest.py`
- [x] **Parameterized Tests**: 6+ parameterized test methods with 30+ test cases
- [x] **Mocking**: 5+ mocking examples using both `unittest.mock` and `pytest-mock`
- [x] **Test Coverage**: Configured with `.coveragerc` and `pytest.ini`
- [x] **HTML Reporting**: Configured in `pytest.ini` with `pytest-html`
- [x] **CI Integration**: Complete GitHub Actions workflow in `.github/workflows/pytest-ci.yml`
- [x] **Runnable Example**: `game_service.py` with `GameService` and `Calculator` classes
- [x] **Documentation**: Comprehensive README with examples

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
- [pytest-html Documentation](https://pytest-html.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

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

### Issue: GitHub Actions workflow fails

**Solution**: Check the workflow file path is correct:
```bash
.github/workflows/pytest-ci.yml
```

---

## 📝 Assignment Submission

For your university assignment, include:

1. ✅ This README.md file
2. ✅ All source code files (`game_service.py`, `test_unit.py`, etc.)
3. ✅ Configuration files (`pytest.ini`, `.coveragerc`, `requirements.txt`)
4. ✅ GitHub Actions workflow (`.github/workflows/pytest-ci.yml`)
5. ✅ Screenshots of:
   - Test execution output
   - Coverage report (HTML)
   - HTML test report
   - GitHub Actions workflow run
6. ✅ Brief explanation of each PyTest feature demonstrated

---

## 👨‍💻 Author

Created for university PyTest assignment demonstrating comprehensive testing practices.

## 📄 License

This project is for educational purposes.

---

**Happy Testing! 🎉**
