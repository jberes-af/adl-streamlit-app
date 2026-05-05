# /src/gui/streamlit/screens/queue_flow.py

from src.application.flow_diagram.flow_diagram_mapper import (
    build_flow_diagram_node_dict,
    build_flow_diagram_edge_tuple,
    build_node_label_to_id_map,
)

from src.application.flow_diagram.build_mermaid_diagram import (
    build_mermaid_flow_chart_definition)

from src.infrastructure.renderer.flow_diagram.diagram_nodes.queue_flow_nodes import (
    QUEUE_FLOW_EDGES,
    QUEUE_FLOW_NODES,
)

from src.gui.streamlit.components.flow_diagram import (
    render_mermaid_flow_diagram)

import streamlit as st


def render_queue_flow_screen() -> None:
    queue_flow_nodes: dict[str, dict[str, str]] = (
        build_flow_diagram_node_dict(QUEUE_FLOW_NODES))

    queue_flow_edges: list[tuple[str, str, str | None]] = (
        build_flow_diagram_edge_tuple(QUEUE_FLOW_EDGES))

    label_to_id_map: dict[str, str]  = (
        build_node_label_to_id_map(QUEUE_FLOW_NODES)
    )

    st.title("'Queue View' Flow")
    st.caption("Click any box in the flowchart to view details.")

    render_mermaid_flow_diagram(
        chart_definition=build_mermaid_flow_chart_definition(
            flow_nodes=queue_flow_nodes,
            flow_edges=queue_flow_edges,
        ),
        node_info=queue_flow_nodes,
        node_label_to_id=label_to_id_map,
    )


"""
def render_queue_flow_screen() -> None:
    st.title("'Queue View' Flow")
    st.caption("Click any box in the flowchart to view details.")

    render_mermaid_flow_diagram(
        chart_definition=build_mermaid_flow_chart_definition(
            flow_nodes=QUEUE_FLOW_NODES,
            flow_edges=QUEUE_FLOW_EDGES,
        ),
        node_info=QUEUE_FLOW_NODES,
        node_label_to_id={
            node_data["label"]: node_id
            for node_id, node_data in QUEUE_FLOW_NODES.items()
        },
    )
"""
