import json
from string import Template

from fastapi import APIRouter
from openai import OpenAI

from models import JourneyMap, Content
from prompt_templates import CONTENT, SYSTEM
from config import CONTENT_TYPES, MODEL

content_router = APIRouter(prefix="/content")


@content_router.post("/")
def get_content_suggestions(
    customer_journey: JourneyMap,
    content_type: str,
) -> dict[str, list[str]]:
    client = OpenAI()
    persona = customer_journey.persona
    stages = customer_journey.stages
    journey_map = "->".join(stages)
    options = {}

    for stage in stages:
        prompt = Template(CONTENT).safe_substitute(
            persona=persona,
            content_type=content_type,
            type_description=CONTENT_TYPES[content_type]["description"],
            tokens=CONTENT_TYPES[content_type]["max_tokens"],
            stage=stage,
            journey_map=journey_map,
        )
        if content_type == "h3":
            prompt = (
                prompt
                + "Incorporate a placeholder $location in the suggestion to be inserted with customer location dynamically."
            )
        completion = client.beta.chat.completions.parse(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            response_format=Content,
        )

        options[stage] = json.loads(completion.choices[0].message.content)["options"]

    return options
