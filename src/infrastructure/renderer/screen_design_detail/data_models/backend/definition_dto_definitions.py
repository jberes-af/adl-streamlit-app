# /src/infrastructure/renderer/screen_design_detail/data_models/backend/definition_dto_definitions.py


ADL_CATEGORY_DEFINITION_DTO: str = """
@dataclass
class AdlCategoryDefinitionDTO:
    category: str
    display_name: str
    description: str
    score_scale_code: str
    is_active: bool = True
"""

OBSERVATION_CATEGORY_DEFINITION_DTO: str = """
@dataclass
class ObservationCategoryDefinitionDTO:
    category: str
    display_name: str
    description: str
    is_active: bool = True
"""

ADL_SCORE_SCALE_DEFINITION_DTO: str = """
@dataclass
class ScoreOptionDTO:
    numeric_value: int
    category: str
    label: str
    description: str = ""
    sort_order: int = 0
"""

REVIEW_SIGNAL_RULE_DEFINITION_DTO: str = """
@dataclass(frozen=True)
class ReviewSignalRuleDefinitionDTO:
    rule_id: str
    signal_type: str
    severity: str
    description: str
    is_active: bool = True
"""

ESCALATION_REASON_DEFINITION_DTO: str = """
@dataclass(frozen=True)
class EscalationReasonDefinitionDTO:
    reason_code: str
    label: str
    default_priority: str = "medium"
    is_active: bool = True
"""


