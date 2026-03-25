````md
# Backend Run and Test Guide

This file describes how to start, verify, and test the backend for the Financial Research RAG Assistant project.

---

## 1. Open the project

Open the project folder in VS Code.

Project root should contain files like:

- README.md
- requirements.txt
- backend/
- docs/

---

## 2. Activate the virtual environment

From the project root, run:

```bash
source financial-rag-env/bin/activate
````

You should then see `(financial-rag-env)` in the terminal.

---

## 3. Start the backend server

Run:

```bash
uvicorn backend.app.main:app --reload
```

Expected successful output should look similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

## 4. Open backend in browser

### Root endpoint

Open:

```text
http://127.0.0.1:8000/
```

Expected result:
A JSON response showing the backend is running.

### Swagger API docs

Open:

```text
http://127.0.0.1:8000/docs
```

Expected result:
FastAPI Swagger UI page with available endpoints.

### Health endpoint

Open:

```text
http://127.0.0.1:8000/api/v1/health
```

Expected result:
A JSON response with health status, environment, and version.

---

## 5. Run backend tests

Open a new terminal from the project root.

Activate the environment again if needed:

```bash
source financial-rag-env/bin/activate
```

Run tests:

```bash
pytest
```

If needed, run:

```bash
python -m pytest
```

Expected result:
At least the health test should pass.

---

## 6. Stop the backend server

In the terminal where uvicorn is running, press:

```text
CTRL + C
```

This stops the local backend server.

---

## 7. Quick backend check sequence

Use this short sequence for normal daily work:

```bash
source financial-rag-env/bin/activate
uvicorn backend.app.main:app --reload
```

Then open:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* [http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)

Then in another terminal:

```bash
source financial-rag-env/bin/activate
pytest
```

---

## 8. Common problems

### Problem: `ModuleNotFoundError`

Cause:
Import paths are wrong.

Fix:
Use imports starting with:

```python
from backend.app...
```

not:

```python
from app...
```

### Problem: command not found / package missing

Cause:
Virtual environment is not activated.

Fix:

```bash
source financial-rag-env/bin/activate
```

### Problem: port already in use

Cause:
Another backend instance is already running.

Fix:
Stop the existing process or use another port.

---

## 9. Current backend launch command

```bash
uvicorn backend.app.main:app --reload
```

## 10. Current virtual environment

```text
financial-rag-env
```

