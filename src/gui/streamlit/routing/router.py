# /src/gui/streamlit/routing/router.py

import streamlit as st

from src.gui.streamlit.routing.route_types import RouteHandler
from src.gui.streamlit.routing.routes import ROUTES


DEFAULT_ROUTE = "Patient Flow"


def get_selected_route() -> str | None:
    selected_route = st.sidebar.radio(
        label="Navigation",
        options=list(ROUTES.keys()),
        index=list(ROUTES.keys()).index(DEFAULT_ROUTE),
    )

    return selected_route


def render_route(route_name: str) -> None:
    route_handler: RouteHandler | None = ROUTES.get(route_name)

    if route_handler is None:
        st.error(f"Unknown route: {route_name}")
        return

    route_handler()


def render_router() -> None:
    selected_route: str | None = get_selected_route()
    render_route(selected_route)
