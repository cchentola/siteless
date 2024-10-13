from string import Template

from openai import OpenAI
from fastapi import APIRouter

from config import MODEL
from models import JourneyMap, Goals, GoalsResponse
from prompt_templates import JOURNEY_MAP, SYSTEM, GOALS


customer_router = APIRouter(prefix="/customer")


@customer_router.post("/{selected_persona}")
def get_goals(selected_persona: str) -> Goals:
    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": Template(GOALS).safe_substitute(
                    selected_persona=selected_persona
                ),
            },
        ],
        response_format=GoalsResponse,
    )
    return Goals(
        persona=selected_persona, goals=completion.choices[0].message.parsed.goals
    )


@customer_router.post("/goals/")
def get_customer_journey(goals: Goals) -> JourneyMap:
    goals_data = goals.model_dump()
    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": Template(JOURNEY_MAP).safe_substitute(
                    selected_persona=goals_data["persona"],
                    goals=", ".join(goals_data["goals"]),
                ),
            },
        ],
        response_format=JourneyMap,
    )
    return completion.choices[0].message.parsed
