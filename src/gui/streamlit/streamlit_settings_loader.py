# src/gui/streamlit/streamlit_settings_loader.py

import os
from typing import Any


def _get_streamlit_secrets() -> Any | None:
    try:
        import streamlit as st
        return st.secrets
    except Exception:
        return None


def streamlit_secrets_available() -> bool:
    secrets = _get_streamlit_secrets()

    if secrets is None:
        return False

    try:
        # this triggers parsing, so it must be inside try
        return len(secrets) > 0
    except Exception:
        return False


def get_secret(name: str, default: str | None = None) -> str | None:
    secrets = _get_streamlit_secrets()

    if secrets is not None:
        try:
            if name in secrets:
                value = secrets[name]
                return str(value).strip()
        except Exception:
            pass

    value = os.getenv(name, default)
    return value.strip() if value else None


def get_required_secret(name: str) -> str:
    value = get_secret(name)
    if not value:
        raise RuntimeError(f"Missing required setting: {name}")
    return value
