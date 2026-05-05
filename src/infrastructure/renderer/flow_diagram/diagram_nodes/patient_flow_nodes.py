# /src/infrastructure/flow_diagram/patient_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.screen_design_definitions.patient_diagram_node_definitions import (
    ADL_ENTRY_NODE,
    ADL_HOME_NODE,
    HISTORY_NODE,
    OBS_ENTRY_NODE,
    PATIENT_SUMMARY_NODE,
    PRIORITY_NODE,

    PATIENT_EDGE_1,
    PATIENT_EDGE_2,
    PATIENT_EDGE_3,
    PATIENT_EDGE_4,
    PATIENT_EDGE_5,
    PATIENT_EDGE_6,
    PATIENT_EDGE_7,
    PATIENT_EDGE_8,
    PATIENT_EDGE_9,
)

# ⚠️ Sequence of keys determines flow chart layout
PATIENT_FLOW_NODES: dict[str, FlowNode] = {
    "ADL_Home": ADL_HOME_NODE,
    "Patient_Summary": PATIENT_SUMMARY_NODE,
    "ADL_Entry": ADL_ENTRY_NODE,
    "OBS_Entry": OBS_ENTRY_NODE,
    "Priority": PRIORITY_NODE,
    "History": HISTORY_NODE,
}

PATIENT_FLOW_EDGES: list[FlowEdge] = [
    PATIENT_EDGE_1,
    PATIENT_EDGE_2,
    PATIENT_EDGE_3,
    PATIENT_EDGE_4,
    PATIENT_EDGE_5,
    PATIENT_EDGE_6,
    PATIENT_EDGE_7,
    PATIENT_EDGE_8,
    PATIENT_EDGE_9,
]
