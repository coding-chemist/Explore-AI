Pre-commit hooks

This repository uses pre-commit to run formatting and linting hooks automatically before commits.

Install and enable hooks (recommended):

```bash
python3 -m pip install --user pre-commit
pre-commit install
# To run all hooks once on all files:
pre-commit run --all-files
```

If you use an editor integration (VS Code, PyCharm), you can configure it to run the hooks on save.
