from string import Template

from fastapi import APIRouter
from openai import OpenAI

from config import MODEL
from models import Business, Competitor, CompetitorResponse, PersonaResponse, Personas
from prompt_templates import COMPETITOR, CUSTOMER_PERSONAS, SYSTEM

owner_router = APIRouter()


@owner_router.post("/business/")
def get_competitors(business: Business):
    business_data = business.dict()
    summary = business_data["summary"]
    location = "the United States"
    if business_data["specific"]:
        location = f"Region: {business_data['region']}, State: {business_data['state']}, City: {business_data['city']}"

    client = OpenAI()

    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": Template(COMPETITOR).safe_substitute(
                    summary=summary,
                    location=location,
                ),
            },
        ],
        response_format=CompetitorResponse,
    )

    return Competitor(
        summary=summary,
        competitors=completion.choices[0].message.parsed.competitors,
    )


@owner_router.post("/competitors/")
def get_customer_personas(competitors: Competitor) -> Personas:
    client = OpenAI()

    competitor_data = competitors.model_dump()
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": Template(CUSTOMER_PERSONAS).safe_substitute(
                    summary=competitor_data["summary"],
                    competitors=",".join(competitor_data["competitors"]),
                ),
            },
        ],
        response_format=PersonaResponse,
    )
    return Personas(
        summary=competitor_data["summary"],
        personas=completion.choices[0].message.parsed.personas,
    )
