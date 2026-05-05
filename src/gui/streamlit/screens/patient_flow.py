# /src/gui/streamlit/screens/patient_flow.py

from src.application.flow_diagram.flow_diagram_mapper import (
    build_flow_diagram_edge_tuple,
    build_flow_diagram_node_dict,
    build_node_label_to_id_map,
)

from src.application.flow_diagram.build_mermaid_diagram import (
    build_mermaid_flow_chart_definition)

from src.infrastructure.renderer.flow_diagram.diagram_nodes.patient_flow_nodes import (
    PATIENT_FLOW_NODES,
    PATIENT_FLOW_EDGES,
)

from src.gui.streamlit.components.flow_diagram import (
    render_mermaid_flow_diagram)

import streamlit as st


def render_patient_flow_screen() -> None:
    patient_flow_nodes: dict[str, dict[str, str]] = (
        build_flow_diagram_node_dict(PATIENT_FLOW_NODES))

    patient_flow_edge: list[tuple[str, str, str | None]] = (
        build_flow_diagram_edge_tuple(PATIENT_FLOW_EDGES))

    label_to_id_map: dict[str, str]  = (
        build_node_label_to_id_map(PATIENT_FLOW_NODES)
    )

    st.title("'Patient View' Flow")
    st.caption("Click any box in the flowchart to view details.")

    render_mermaid_flow_diagram(
        chart_definition=build_mermaid_flow_chart_definition(
            flow_nodes=patient_flow_nodes,
            flow_edges=patient_flow_edge,
        ),
        node_info=patient_flow_nodes,
        node_label_to_id=label_to_id_map,
    )
