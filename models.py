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


class JourneyMap(BaseModel):
    persona: str
    stages: list[str]


class Content(JourneyMap):
    persona: str
    stage: str
    options: list[str]


class StageFeatures(BaseModel):
    features: list[str]
    # user: list[str]
