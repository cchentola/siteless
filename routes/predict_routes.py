from openai import OpenAI
from fastapi import APIRouter

from config import MODEL, PERSONA_STAGES
from models import VisitorData, VisitorType
from prompt_templates import SYSTEM

predict_router = APIRouter(prefix="/predict")


@predict_router.post("/visitor_data/")
def predict_persona_stage(visitor_data: VisitorData) -> VisitorType:
    client = OpenAI()
    visitor_data = visitor_data.model_dump()
    prompt = f"""
        Based on the following user features {visitor_data}, predict the persona of the user and stage they are at in their journey?
        Choose your answer from the provided dictionary:
        {PERSONA_STAGES}  
    """

    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        response_format=VisitorType,
    )
    return completion.choices[0].message.parsed
