# test_fixture_scopes.py
import pytest

# Fixture with module scope
@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetup for module_fixture")
    yield
    print("\nTeardown for module_fixture")

def test_module_scope_1(module_fixture):
    print("Running test_module_scope_1")

def test_module_scope_2(module_fixture):
    print("Running test_module_scope_2")

# Note: Session-scoped fixtures won't be demonstrated here as they require running pytest with multiple files.
