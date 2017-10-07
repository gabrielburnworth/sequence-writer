Sequence Writer
---

Python module to write [FarmBot](https://github.com/FarmBot)
[Celery Script](https://github.com/FarmBot/farmbot-js/wiki/Celery-Script)
JSON Sequences

```python
with Sequence("My Sequence", "green") as s:
    s.wait(milliseconds=1000)
    s.take_photo()
```

```JSON
{
  "name": "My Sequence",
  "color": "green",
  "body": [
    {
      "kind": "wait",
      "args": {
        "milliseconds": 1000
      }
    },
    {
      "kind": "take_photo",
      "args": {}
    }
  ]
}
```

For more examples, see [/examples.py](/examples.py).
