import pytest
from databricks.sdk.service.workspace import Language

from databricks.labs.ucx.hive_metastore.table_migration_status import TableMigrationIndex
from databricks.labs.ucx.source_code.base import Fixer, Linter
from databricks.labs.ucx.source_code.linters.context import LinterContext

index = TableMigrationIndex([])


def test_linter_returns_correct_analyser_for_python() -> None:
    languages = LinterContext(index)
    linter = languages.linter(Language.PYTHON)
    assert isinstance(linter, Linter)


def test_linter_returns_correct_analyser_for_sql() -> None:
    languages = LinterContext(index)
    linter = languages.linter(Language.SQL)
    assert isinstance(linter, Linter)


def test_linter_raises_error_for_unsupported_language() -> None:
    languages = LinterContext(index)
    with pytest.raises(ValueError):
        languages.linter(Language.R)


def test_fixer_returns_none_fixer_for_python() -> None:
    languages = LinterContext(index)
    fixer = languages.fixer(Language.PYTHON, "diagnostic_code")
    assert fixer is None


def test_fixer_returns_correct_fixer_for_python() -> None:
    languages = LinterContext(index)
    fixer = languages.fixer(Language.PYTHON, "table-migrate")
    assert isinstance(fixer, Fixer)


def test_fixer_returns_none_fixer_for_sql() -> None:
    languages = LinterContext(index)
    fixer = languages.fixer(Language.SQL, "diagnostic_code")
    assert fixer is None


def test_fixer_returns_correct_fixer_for_sql() -> None:
    languages = LinterContext(index)
    fixer = languages.fixer(Language.SQL, "table-migrate")
    assert isinstance(fixer, Fixer) or fixer is None


def test_fixer_returns_none_for_unsupported_language() -> None:
    languages = LinterContext(index)
    fixer = languages.fixer(Language.SCALA, "diagnostic_code")
    assert fixer is None
