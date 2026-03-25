# Frontend Run and Test Guide

This file describes how to start, verify, and test the frontend for the Financial Research RAG Assistant project.

---

## 1. Open the project

Open the project folder in VS Code.

Project root should contain files like:

- README.md
- backend/
- frontend/
- docs/

---

## 2. Open a terminal and go to the frontend folder

From the project root, run:

```bash
cd frontend
```

You should now be inside the frontend folder.

---

## 3. Install frontend dependencies

If this is the first time running the frontend, install dependencies:

```bash
npm install
```

Expected result:
npm installs the required frontend packages and creates `node_modules/`.

---

## 4. Start the frontend development server

Run:

```bash
npm run dev
```

Expected successful output should look similar to:

```text
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
```

---

## 5. Open frontend in browser

Open:

```text
http://localhost:5173/
```

Expected result:
The Financial Research RAG Assistant frontend loads in the browser.

You should see:

- sidebar navigation
- page header
- chat page content
- backend status badge in the top-right area

---

## 6. Verify frontend-backend connection

Make sure the backend is running separately.

If backend is running correctly, the frontend header badge should show:

```text
Backend: online
```

If backend is not running or not reachable, it will show:

```text
Backend: offline
```

---

## 7. Build the frontend for production

From the `frontend` folder, run:

```bash
npm run build
```

Expected result:
TypeScript compilation and Vite production build complete successfully.

Example output:

```text
vite v5.x.x building for production...
✓ built in xxxms
```

This should create a `dist/` folder inside `frontend/`.

---

## 8. Preview the production build

After building, run:

```bash
npm run preview
```

Expected result:
A local preview server starts for the production build.

Open the local preview URL shown in the terminal.

---

## 9. Stop the frontend server

In the terminal where the frontend is running, press:

```text
CTRL + C
```

This stops the local frontend development server.

---

## 10. Quick frontend check sequence

Use this short sequence for normal daily work:

```bash
cd frontend
npm install
npm run dev
```

Then open:

* http://localhost:5173/

If you want to test production build too:

```bash
npm run build
npm run preview
```

---

## 11. Common problems

### Problem: white blank page

Cause:
A frontend file is missing, broken, or the app failed during render.

Fix:
Check:

- `frontend/index.html`
- `src/main.tsx`
- `src/App.tsx`
- browser developer console for errors

---

### Problem: red TypeScript underlines in VS Code

Cause:
TypeScript config, Vite types, or imports are not resolved correctly.

Fix:
Check:

- `tsconfig.json`
- `tsconfig.app.json`
- `tsconfig.node.json`
- `src/vite-env.d.ts`

Also restart the TypeScript server in VS Code.

---

### Problem: `import.meta.env` error

Cause:
Vite environment types are missing.

Fix:
Create:

```text
src/vite-env.d.ts
```

with:

```ts
/// <reference types="vite/client" />
```

---

### Problem: backend status stays offline

Cause:
Backend is not running, wrong API URL is set, or CORS is blocking requests.

Fix:
Check:

- backend is running on `http://127.0.0.1:8000`
- frontend `.env` contains:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

- backend allows frontend origin such as `http://localhost:5173`

---

### Problem: `npm install` fails because of `package.json`

Cause:
`package.json` is empty or invalid.

Fix:
Make sure `frontend/package.json` contains valid JSON.

---

### Problem: `cd frontend` says no such file or directory

Cause:
You are already inside the `frontend` folder.

Fix:
Run:

```bash
pwd
```

If the terminal already ends in `frontend`, do not run `cd frontend` again.

---

## 12. Current frontend launch command

```bash
npm run dev
```

## 13. Current frontend build command

```bash
npm run build
```

## 14. Current frontend folder

```text
frontend
```