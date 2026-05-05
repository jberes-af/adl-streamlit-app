# /src/infrastructure/flow_diagram/queue_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.screen_design_definitions.patient_diagram_node_definitions import (
    ADL_ENTRY_NODE,
    ADL_HOME_NODE,
    OBS_ENTRY_NODE,
    PATIENT_SUMMARY_NODE,
    PRIORITY_NODE,
)

from src.infrastructure.renderer.flow_diagram.screen_design_definitions.queue_diagram_node_definitions import (
    QUEUE_REVIEW_NODE,
    QUEUE_DETAIL_NODE,

    QUEUE_EDGE_1,
    QUEUE_EDGE_2,
    QUEUE_EDGE_3,
    QUEUE_EDGE_4,
    QUEUE_EDGE_5,
    QUEUE_EDGE_6,
    QUEUE_EDGE_7,
    QUEUE_EDGE_8,

)

QUEUE_FLOW_NODES: dict[str, FlowNode] = {
    "ADL_Home": ADL_HOME_NODE,
    "Queue_Review": QUEUE_REVIEW_NODE,
    "Queue_Detail": QUEUE_DETAIL_NODE,
    "Patient_Summary": PATIENT_SUMMARY_NODE,
    "Priority": PRIORITY_NODE,
    "ADL_Entry": ADL_ENTRY_NODE,
    "OBS_Entry": OBS_ENTRY_NODE,
}

QUEUE_FLOW_EDGES: list[FlowEdge] = [
    QUEUE_EDGE_1,
    QUEUE_EDGE_2,
    QUEUE_EDGE_3,
    QUEUE_EDGE_4,
    QUEUE_EDGE_5,
    QUEUE_EDGE_6,
    QUEUE_EDGE_7,
    QUEUE_EDGE_8,
]
