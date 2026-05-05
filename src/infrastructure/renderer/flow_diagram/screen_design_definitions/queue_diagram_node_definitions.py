# /src/infrastructure/flow_diagram/queue_diagram_node_definitions.py

from src.application.flow_diagram.flow_diagram_types import (
    FlowNode,
    FlowEdge,
    NodeClassName,
)

from src.infrastructure.renderer.screen_design_detail.use_cases.use_cases_dtos import (
    UC_QUEUE_01,
    UC_QUEUE_02,
    UC_QUEUE_03,
    UC_ESC_01,
)

from src.infrastructure.renderer.screen_design_detail.workflows.workflow_dtos import (
    WF_QUEUE_01, WF_QUEUE_02, WF_QUEUE_03, WF_QUEUE_04,
    WF_QUEUE_DET_01, WF_QUEUE_DET_02, WF_QUEUE_DET_03, WF_QUEUE_DET_04,
)

from src.infrastructure.renderer.screen_design_detail.screens.screen_specification import (
    REVIEW_QUEUE_SCREEN_SPEC,
    REVIEW_QUEUE_DETAIL_SCREEN_SPEC
)

from src.infrastructure.renderer.screen_design_detail.data_models.client.client_contracts_dtos import (
    REVIEW_QUEUE_CLIENT_CONTRACTS,
    REVIEW_QUEUE_DETAIL_CLIENT_CONTRACTS,
)

from src.infrastructure.renderer.screen_design_detail.data_models.backend.backend_dtos import (
    REVIEW_QUEUE_BACKEND_DTOS,
    REVIEW_QUEUE_DETAIL_BACKEND_DTOS,
)


"""
FLOW DIAGRAM NODES
"""

QUEUE_REVIEW_NODE = FlowNode(
    title="Review Queue",
    label="Queue Review",
    class_name=NodeClassName.PAGE,
    screen_spec=REVIEW_QUEUE_SCREEN_SPEC,
    use_cases=tuple([
        UC_QUEUE_01,
    ]),
    workflows=tuple([
        WF_QUEUE_01, WF_QUEUE_02, WF_QUEUE_03, WF_QUEUE_04,
    ]),
    client_contracts=REVIEW_QUEUE_CLIENT_CONTRACTS,
    backend_data_model=REVIEW_QUEUE_BACKEND_DTOS,
    rules_engine=None,
    description="Show Review Queue.",
)

QUEUE_DETAIL_NODE = FlowNode(
    title="Queue Detail",
    label="Queue Detail",
    class_name=NodeClassName.PAGE,
    screen_spec=REVIEW_QUEUE_DETAIL_SCREEN_SPEC,
    use_cases=tuple([
        UC_QUEUE_02, UC_QUEUE_03, UC_ESC_01,
    ]),
    workflows=tuple([
        WF_QUEUE_DET_01, WF_QUEUE_DET_02, WF_QUEUE_DET_03, WF_QUEUE_DET_04,
    ]),
    client_contracts=REVIEW_QUEUE_DETAIL_CLIENT_CONTRACTS,
    backend_data_model=REVIEW_QUEUE_DETAIL_BACKEND_DTOS,
    rules_engine=None,
    description="Show Queue detail.",
)

"""
FLOW DIAGRAM EDGES
"""

QUEUE_EDGE_1 = FlowEdge(
    source="ADL_Home",
    target="Queue_Review",
    action_label=None
)

QUEUE_EDGE_2 = FlowEdge(
    source="Queue_Review",
    target="Queue_Detail",
    action_label="Tap Queue Item",
)

QUEUE_EDGE_3 = FlowEdge(
    source="Queue_Detail",
    target="Patient_Summary",
    action_label="Tap Open Patient",
)

QUEUE_EDGE_4 = FlowEdge(
    source="Queue_Detail",
    target="Priority",
    action_label="Tap Prioritize",
)

QUEUE_EDGE_5 = FlowEdge(
    source="Queue_Detail",
    target="ADL_Entry",
    action_label="Tap Enter ADL",
)

QUEUE_EDGE_6 = FlowEdge(
    source="Queue_Detail",
    target="OBS_Entry",
    action_label="Tap Add Observation",
)

QUEUE_EDGE_7 = FlowEdge(
    source="Queue_Detail",
    target="Queue_Review",
    action_label="Back",
)

QUEUE_EDGE_8 = FlowEdge(
    source="Queue_Review",
    target="ADL_Home",
    action_label="Back",
)
