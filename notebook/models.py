from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class OntologyItem(BaseModel):
    id: str
    name: str
    description: str


class LogRecord(OntologyItem):
    pass


class Procedure(OntologyItem):
    pass


class Step(OntologyItem):
    pass


class StepClass(OntologyItem):
    pass


class LogSymptom(OntologyItem):
    pass


class SystemStatus(OntologyItem):
    pass


class RootCause(OntologyItem):
    pass


class DataGap(OntologyItem):
    pass


class PreventiveAction(OntologyItem):
    pass


class Remediation(OntologyItem):
    pass


class Annotation(OntologyItem):
    pass


class Relationship(BaseModel):
    id: str
    name: str
    description: str
    source_id: str
    target_id: str


class ExtractedRCA(BaseModel):
    log_record: LogRecord
    procedures: List[Procedure] = Field(default_factory=list)
    steps: List[Step] = Field(default_factory=list)
    step_classes: List[StepClass] = Field(default_factory=list)
    log_symptoms: List[LogSymptom] = Field(default_factory=list)
    system_statuses: List[SystemStatus] = Field(default_factory=list)
    root_causes: List[RootCause] = Field(default_factory=list)
    data_gaps: List[DataGap] = Field(default_factory=list)
    preventive_actions: List[PreventiveAction] = Field(default_factory=list)
    remediations: List[Remediation] = Field(default_factory=list)
    annotations: List[Annotation] = Field(default_factory=list)
    relationships: List[Relationship] = Field(default_factory=list)


class MatchResult(BaseModel):
    matched_log_id: Optional[str]
    match_score: float
    confidence: Literal["LOW", "MEDIUM", "HIGH"]
    explanation: str
    remediations: List[Remediation] = Field(default_factory=list)
    preventive_actions: List[PreventiveAction] = Field(default_factory=list)