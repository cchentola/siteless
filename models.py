from pydantic import BaseModel


class Business(BaseModel):
    summary: str
    specific: bool
    region: str | None = None
    state: str | None = None
    city: str | None = None


class CompetitorResponse(BaseModel):
    competitors: list[str]


class Competitor(BaseModel):
    summary: str
    competitors: list[str]


class PersonaResponse(BaseModel):
    personas: list[str]


class Personas(BaseModel):
    summary: str
    personas: list[str]


class GoalsResponse(BaseModel):
    goals: list[str]


class Goals(BaseModel):
    persona: str
    goals: list[str]


class JourneyMap(BaseModel):
    persona: str
    stages: list[str]


class Content(JourneyMap):
    persona: str
    stage: str
    options: list[str]


class StageFeatures(BaseModel):
    persona: str
    features: dict


class Stage(BaseModel):
    stage: str


class VisitorData(BaseModel):
    clicks: int
    time_spent: int
    pages_viewed: int
    click_ids: list[str]


class VisitorType(BaseModel):
    persona: str
    stage: str
