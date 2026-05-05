# /src/gui/streamlit/routing/routes.py

from src.gui.streamlit.routing.route_types import RouteHandler
from src.gui.streamlit.screens.patient_flow import render_patient_flow_screen
from src.gui.streamlit.screens.queue_flow import render_queue_flow_screen


ROUTES: dict[str, RouteHandler] = {
    "Patient Flow": render_patient_flow_screen,
    "Queue Flow": render_queue_flow_screen,
}
