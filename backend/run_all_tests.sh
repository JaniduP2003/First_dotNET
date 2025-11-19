#!/bin/bash

# PyTest Test Runner Script
# This script runs all tests with various configurations

echo "========================================"
echo "   PyTest Comprehensive Test Suite     "
echo "========================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print section headers
print_section() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo -e "${YELLOW}Warning: Virtual environment not activated${NC}"
    echo "Run: source venv/bin/activate"
    echo ""
fi

# 1. Run all unit tests
print_section "1. Running All Unit Tests"
pytest test_unit.py -v

# 2. Run unit tests with coverage
print_section "2. Running Unit Tests with Coverage"
pytest test_unit.py --cov=. --cov-report=term-missing

# 3. Generate HTML coverage report
print_section "3. Generating HTML Coverage Report"
pytest test_unit.py --cov=. --cov-report=html
echo -e "${GREEN}✓ Coverage report generated: htmlcov/index.html${NC}"

# 4. Generate HTML test report
print_section "4. Generating HTML Test Report"
mkdir -p reports
pytest test_unit.py --html=reports/test_report.html --self-contained-html
echo -e "${GREEN}✓ Test report generated: reports/test_report.html${NC}"

# 5. Run parameterized tests only
print_section "5. Running Parameterized Tests"
pytest test_unit.py::TestParameterizedCalculator -v

# 6. Run tests with mocking
print_section "6. Running Tests with Mocking"
pytest test_unit.py::TestGameServiceMocking -v

# 7. Run tests by markers
print_section "7. Running Tests by Markers"
echo "Running unit tests only:"
pytest -m unit -v --tb=line

# 8. Show test collection
print_section "8. Test Collection Summary"
pytest --collect-only -q

# 9. Show fixtures
print_section "9. Available Fixtures"
pytest --fixtures -q | head -30

# 10. Coverage summary
print_section "10. Final Coverage Summary"
coverage report

# Print final summary
echo ""
echo -e "${GREEN}========================================"
echo "   All Tests Completed Successfully!"
echo "========================================${NC}"
echo ""
echo "Generated Reports:"
echo "  - HTML Coverage:  htmlcov/index.html"
echo "  - Test Report:    reports/test_report.html"
echo ""
echo "To view reports:"
echo "  open htmlcov/index.html"
echo "  open reports/test_report.html"
echo ""
