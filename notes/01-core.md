# Sort records with tie breakers: implementation

## What the example does

Sort by score descending, then name ascending. Python sorting is stable, so records with equal keys preserve their original relative order.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  {
    "name": "B",
    "score": 2
  },
  {
    "name": "A",
    "score": 2
  },
  {
    "name": "C",
    "score": 3
  }
]
```

Expected result:

```json
[
  {
    "name": "C",
    "score": 3
  },
  {
    "name": "A",
    "score": 2
  },
  {
    "name": "B",
    "score": 2
  }
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
