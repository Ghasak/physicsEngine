# Physics Engine

## How to run
We will consider this engine as a `python` package. So, the implementation is
based on `module` syntax not `script` syntax.

- Considering the Entry point for our project at:
```python
python -m src.main
```

## Import and pyright LSP
I have used the `pyproject.toml` to configur the `pyright` using the code snippet offered from
- [pyright import using src error](https://github.com/microsoft/pyright/issues/3378)
and finding it here:
- [pyright import snippet](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#sample-config-file)

```toml
[tool.pyright]
include = ["src"]

```



