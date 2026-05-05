# Developer's Notes

📆 Created: **April 30, 2026**
📆 Revised: **April 30, 2026**



## Colors

| Object  | Color  | Hex     | 
|---------|--------|---------|
| Page    | Blue   | #e3f2fd |
| Action  | Orange | #fff3e0 |
| Tap     | Gray   | #f8f8f8 |
| Form    | Green  | #e8f5e9 | 
| Utility | Gray   | #f8f8f8 |

## Summary



**Run App**

```text
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Run app
# python -m streamlit run app.py
streamlit run src/gui/streamlit/app.py

```



```text
[BOOT]
streamlit run app.py
    ↓
app.py imports composition_root
    ↓
composition_root builds:
    - FirebaseAuthProvider
    - LoginUser
    - AuthController

----------------------------------

[RUNTIME]
User enters email/password
    ↓
login_form.py (GUI)
    ↓
AuthController.login()
    ↓
LoginUser.execute()
    ↓
FirebaseAuthProvider.authenticate()
    ↓
AuthenticatedUserDTO
    ↓
Presenter (optional)
    ↓
GUI updates st.session_state
    ↓
Mermaid page renders
```





```text
streamlit run src/gui/streamlit/app.py
        ↓
app.py  ✅ ENTRYPOINT
        ↓
(import triggers)
composition_root.py  ✅ BUILDS SYSTEM
        ↓
settings/config loaded
dependencies wired
        ↓
app.py continues
        ↓
render_login_phase()
        ↓
LoginForm.render()
```

**Premise**

```text
Streamlit handles login and page protection.
HTML/CSS/JS handles Mermaid rendering and popup interaction.
Python clean architecture handles auth, access control, and loading the frontend.
```


```text
app.py   = Streamlit entrypoint, run with streamlit
main.py  = optional Python entrypoint, useful for tests/CLI/future expansion
```

**Implementation**

```text
Authentication/access control → Python clean architecture
Mermaid rendering/clicks/popups → frontend JavaScript
```



- Mermaid logic in Python.

- HTML-CSS in `frontend/`:

```
frontend/
├── index.html
├── css/main.css
└── js/main.js
```

- Streamlit simply embeds HTML after login:

```
User logs in
 ↓
FirebaseAuthProvider validates credentials
 ↓
Streamlit session_state stores authenticated user
 ↓
MermaidPage renders frontend/index.html
```



## Flow & Structure


### Flow


```text
Streamlit protects access
HTML app runs only after login
Mermaid interactivity stays lightweight in JavaScript
```

But the embedded HTML is not a separate protected website. It is content rendered inside Streamlit after authentication.

For your use case, this is probably the cleanest hybrid:

```text
Firebase Auth + Streamlit login
        ↓
Protected Streamlit page
        ↓
Embedded Mermaid HTML/JS app
```

```text
User
 ↓
Streamlit Login Page
 ↓
Firebase Auth verifies user
 ↓
If authenticated:
    Streamlit renders protected page
    ↓
    Embedded HTML/CSS/JS Mermaid app
```

### Folder Structure

#### Simple

```text
project/
├── app.py
├── auth/
│   └── firebase_auth.py
├── mermaid_app/
│   ├── index.html
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
└── requirements.txt
```

#### Clean Architecture

```text

project/
├── app.py                          # Streamlit entry point
├── requirements.txt
│
├── src/
│   ├── domain/
│   │   ├── user.py
│   │   └── chart_node.py
│   │
│   ├── application/
│   │   ├── ports/
│   │   │   ├── auth_provider.py
│   │   │   └── chart_repository.py
│   │   ├── login_user.py
│   │   └── get_chart_node_info.py
│   │
│   ├── interface_adapters/
│   │   ├── streamlit/
│   │   │   ├── login_page.py
│   │   │   └── mermaid_page.py
│   │   └── presenters/
│   │       └── auth_presenter.py
│   │
│   ├── infrastructure/
│   │   ├── firebase/
│   │   │   └── firebase_auth_provider.py
│   │   ├── chart_data/
│   │   │   └── static_chart_repository.py
│   │   └── mermaid/
│   │       └── html_renderer.py
│   │
│   └── main/
│       └── container.py             # dependency wiring
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── main.css
│   └── js/
│       ├── main.js
│       ├── data/
│       │   └── chartNodes.js
│       ├── ui/
│       │   └── popup.js
│       └── mermaid/
│           └── mermaidSetup.js
│
└── assets/
```



## treamlit login flow

```
Streamlit login_form.py
  ↓ raw email/password
AuthController
  ↓ LoginRequestDTO
LoginUser use case
  ↓ AuthProvider interface
FirebaseAuthProvider
  ↓ AuthenticatedUserDTO
AuthPresenter
  ↓ AuthViewModel
Streamlit stores session_state
```

## Mermaid HTML part

That belongs in GUI:

```
gui/streamlit/pages/mermaid_page.py
gui/streamlit/components/mermaid_component.py




domain/              ✅ entities / core concepts
application/         ✅ use cases + ports
infrastructure/      ✅ external libraries + repositories
presentation/        ✅ UI controllers, views, renderers, styles
data/                ✅ static seed/mock data
main.js              ✅ composition root / startup wiring
index.html           ✅ app shell



patient_flow_page.py        → screen/layout
patient_flow_diagram.py     → reusable Streamlit component
patient_flow_service.py     → application logic / chart data assembly
patient_flow_nodes.py       → static data source
```

Because embedded HTML/Mermaid rendering is purely presentation/framework behavior.

## nal recommendation

Use this split:

```
gui/streamlit/             # Streamlit forms, session_state, HTML, Mermaid
interface_adapters/        # controllers + presenters
application/auth/          # DTOs + login use case
domain/auth/               # auth provider protocol
infrastructure/auth/       # Firebase implementation
```

The key rule:

```
Streamlit session_state stays in gui.
Firebase SDK stays in infrastructure.
Login DTOs and use case stay in application.
Controller/presenter stay in interface_adapters.
```



```text
patient_flow_nodes.py
    → title, label, description, dto_code, image

patient_flow_diagram.py
    → embeds HTML shell and base64 images

flow_diagram.js
    → updates the three collapsible sections on click

patient_flow_diagram.css
    → styling for cards, details, code, images
```





### Requirements

```text
streamlit
requests
```

### Layers

- **`domain`**: `User`, `ChartNode`,`ChartFlow`
- **`application`**: - `LoginUser`,  `GetChartNodeInfo`, `AuthProvider` interface,  `ChartRepository` interface
- **`interface_adapters`**:  login form, authenticated Mermaid page,  error/success display formatting.
- **`infrastructure`**: Firebase Auth, static chart data loader, HTML renderer for embedding Mermaid app
- **`main`**: Dependency wiring; connect `LoginUser` to `FirebaseAuthProvider`; connect chart page to `HtmlRenderer`

<br>

## Authentication



For simple login, use Firebase Web App Config.

```text
Firebase project
Firebase Authentication enabled
Email/password sign-in provider enabled
Firebase Web App config
Python package for client sign-in, e.g. Pyrebase/Pyrebase4

Login with email/password        → Web config / API key
Verify token or manage users     → Admin SDK / service account private key

FirebaseClientAuthService = login users
FirebaseAdminService      = verify/manage users
```





## Code Sketch

### Streamlit shell

```python
# app.py

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# from auth.firebase_auth import login_user


MERMAID_APP_DIR = Path("mermaid_app")


def render_mermaid_app() -> None:
    html = (MERMAID_APP_DIR / "index.html").read_text(encoding="utf-8")
    css = (MERMAID_APP_DIR / "css" / "main.css").read_text(encoding="utf-8")
    js = (MERMAID_APP_DIR / "js" / "main.js").read_text(encoding="utf-8")

    full_html = html.replace("</head>", f"<style>{css}</style></head>")
    full_html = full_html.replace("</body>", f"<script>{js}</script></body>")

    components.html(full_html, height=800, scrolling=True)


def main() -> None:
    st.set_page_config(page_title="Protected Mermaid App", layout="wide")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Log in"):
            pass
            # user = login_user(email=email, password=password)
            user = ""

            if user:
                st.session_state.authenticated = True
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid email or password.")

        return

    st.sidebar.success(f"Logged in as {st.session_state.user['email']}")

    if st.sidebar.button("Log out"):
        st.session_state.clear()
        st.rerun()

    st.title("ADL Flow App")
    render_mermaid_app()


if __name__ == "__main__":
    main()
```

<br>

### Firebase login adapter

```python
# firebase/firebase_auth.py

import requests


FIREBASE_API_KEY = "YOUR_FIREBASE_WEB_API_KEY"


def login_user(email: str, password: str) -> dict | None:
    url = (
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        f"?key={FIREBASE_API_KEY}"
    )

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True,
    }

    response = requests.post(url, json=payload, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "email": data["email"],
        "id_token": data["idToken"],
        "refresh_token": data["refreshToken"],
        "local_id": data["localId"],
    }
```

<br>

### Mermaid HTML app

```html
<!-- mermaid_app/index.html -->

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
</head>

<body>
  <div class="mermaid">
flowchart LR
   ADL_Home[ADL Home Page]
   Patient[Patient View]
   ADL_Entry[ADL Entry]
   OBS_Entry[Observation Entry]

   ADL_Home --> Patient
   Patient -->|Tap Enter ADL| ADL_Entry
   Patient -->|Tap Add Observation| OBS_Entry

   click ADL_Home call showInfo("ADL_Home")
   click Patient call showInfo("Patient")
   click ADL_Entry call showInfo("ADL_Entry")
   click OBS_Entry call showInfo("OBS_Entry")
  </div>

  <div id="overlay" onclick="closePopup()"></div>

  <div id="popup">
    <h2 id="popup-title"></h2>
    <p id="popup-body"></p>
    <button onclick="closePopup()">Close</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</body>
</html>
```

<br>

### Mermaid JavaScript

```javascript
// mermaid_app/js/main.js

const nodeInfo = {
  ADL_Home: {
    title: "ADL Home Page",
    body: "Main landing page for the ADL workflow."
  },
  Patient: {
    title: "Patient View",
    body: "Displays patient-specific ADL actions."
  },
  ADL_Entry: {
    title: "ADL Entry",
    body: "Screen used to enter ADL data."
  },
  OBS_Entry: {
    title: "Observation Entry",
    body: "Screen used to add patient observations."
  }
};

mermaid.initialize({
  startOnLoad: true,
  securityLevel: "loose"
});

function showInfo(nodeId) {
  const info = nodeInfo[nodeId];

  document.getElementById("popup-title").innerText = info?.title || nodeId;
  document.getElementById("popup-body").innerText = info?.body || "No details available.";
  document.getElementById("popup").style.display = "block";
  document.getElementById("overlay").style.display = "block";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
  document.getElementById("overlay").style.display = "none";
}
```

### CSS

```css
/* mermaid_app/css/main.css */

body {
  font-family: Arial, sans-serif;
  padding: 24px;
}

#overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.35);
  z-index: 999;
}

#popup {
  display: none;
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  width: 360px;
  background: white;
  border: 1px solid #ccc;
  border-radius: 12px;
  padding: 20px;
  z-index: 1000;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
}
```



---

## Hosting Ideas



Best recommendation: **deploy the whole hybrid app as one Streamlit service on Google Cloud Run**, optionally with **Firebase Hosting in front** for the public URL.

```text
Browser
 ↓
Firebase Hosting custom domain
 ↓
Rewrite to Cloud Run
 ↓
Streamlit app
 ↓
Firebase Auth login
 ↓
Embedded HTML/CSS/JS Mermaid app
```

Why this is best:

| Requirement                  | Best fit                                                |
| ---------------------------- | ------------------------------------------------------- |
| Streamlit login page         | Needs Python server                                     |
| Firebase Auth verification   | Easy inside Streamlit                                   |
| Embedded HTML/JS Mermaid app | Served/rendered by Streamlit                            |
| Production hosting           | Cloud Run is designed for containerized Python web apps |
| Firebase-friendly URL        | Firebase Hosting can rewrite traffic to Cloud Run       |

Google has an official Cloud Run quickstart for Python/Streamlit, and Firebase Hosting officially supports routing dynamic requests to Cloud Run services. ([Google Cloud Documentation](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service?utm_source=chatgpt.com))

Recommended deployment:

```text
Option A — simplest production
Cloud Run only
```

Use this if you are fine with a Cloud Run URL or custom domain directly on Cloud Run.

```text
Option B — best Firebase-integrated setup
Firebase Hosting → Cloud Run
```

Use this if you want Firebase Hosting/custom-domain behavior while still running Streamlit as the backend.

I would **not** split the Mermaid HTML app into separate Firebase static hosting for this hybrid design. Since Streamlit controls access, the safest and simplest setup is:

```text
Protected app = one deployable unit
Streamlit serves/embeds frontend only after auth
```

Suggested repo:

```text
project/
├── app.py
├── Dockerfile
├── requirements.txt
├── firebase.json              # only if using Firebase Hosting rewrite
├── src/
│   ├── domain/
│   ├── application/
│   ├── interface_adapters/
│   ├── infrastructure/
│   └── main/
└── frontend/
    ├── index.html
    ├── css/main.css
    └── js/main.js
```

A typical `firebase.json` would route everything to Cloud Run:

```json
{
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "**",
        "run": {
          "serviceId": "mermaid-streamlit-app",
          "region": "us-central1"
        }
      }
    ]
  }
}
```

Final recommendation:

```text
Best overall:
Cloud Run for Streamlit
+ Firebase Hosting rewrite if you want Firebase/custom-domain integration
+ Firebase Auth inside Streamlit
+ embedded Mermaid frontend bundled with the app
```


### Map Screens to Use Cases

ADL Home
- REVIEW
- ANALYZE (light)
- SYSTEM (signals)

Patient Summary
- REVIEW
- ANALYZE
- ESCALATE
- COMPLETE

Review Queue
- REVIEW
- ANALYZE
- ACKNOWLEDGE

 
Review Queue Detail
- REVIEW
- ANALYZE
- ESCALATE
- ACKNOWLEDGE

ADL Entry
- CAPTURE
- DOCUMENT (notes)
- SYSTEM (comparison logic)

Observation Entry
- CAPTURE
- DOCUMENT

Escalate
- ESCALATE
- DOCUMENT

View History
- REVIEW
- ANALYZE

<br>

## User Object Management

### Summary

User role is a **system-level access control concept**, not a screen architecture concept — it should connect to screens only through **permissions**, not be embedded in `FlowNode`.

>**FlowNode defines capability requirements.
>RoleDefinition defines capability availability.
>User provides the role.**

It is a **separate axis** from your screen architecture.

> **User role does NOT belong inside `FlowNode` (screen architecture).**
> It is a **system-level (access control) concern**, connected via **permissions**, not directly embedded.

### Where “user role” belongs

```text
UserDefinition (runtime)
    ↓
Role (enum)
    ↓
RoleDefinition (domain policy)
    ↓
PermissionRule (what is allowed)
```

### Where `FlowNode` lives

What the app does

```text
FlowNode (screen)
    ↓
ScreenSpec
    ↓
UseCases
    ↓
Workflows
    ↓
DTOs / Rules Engine
```

### The connection point

The **ONLY correct bridge** between these two worlds is:

```python
required_permissions: tuple["Permission-Requirement", ...]
```

```text
FlowNode (screen)
    └── required_permissions

RoleDefinition (user role)
    └── permissions

Access = match(required_permissions, permissions)
```


### Where roles SHOULD appear

#### 1. In RoleDefinition (domain)

```python
class RoleDefinition:
    role: Role
    permissions: tuple[PermissionRule, ...]
```

#### 2. In UseCase (optional, for documentation)

```python
primary_actor: str
supporting_actors: tuple[str, ...]
```

This is **descriptive**, not enforcement.

#### 3. In permission evaluation (runtime)

```python
permission_service.is_allowed(user.role, domain, action)
```
