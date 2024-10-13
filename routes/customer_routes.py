from string import Template

from openai import OpenAI
from fastapi import APIRouter

from config import MODEL
from models import JourneyMap
from prompt_templates import JOURNEY_MAP, SYSTEM


customer_router = APIRouter(prefix="/customer")


@customer_router.post("/{selected_persona}")
def get_customer_journey(selected_persona: str) -> JourneyMap:
    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": Template(JOURNEY_MAP).safe_substitute(
                    selected_persona=selected_persona
                ),
            },
        ],
        response_format=JourneyMap,
    )
    return completion.choices[0].message.parsed


# def predict_stage(journey_map: JourneyMap):
#     journey_data = journey_map.model_dump()
#     client = OpenAI()
#     # prompt 1: what data do we need to predict the stage?
#     completion = client.beta.chat.completions.parse(
#         model="gpt-4o-mini-2024-07-18",
#         messages=[
#             {"role": "system", "content": SYSTEM},
#             {
#                 "role": "user",
#                 "content": Template(STAGE_FEATURES).safe_substitute(
#                     persona=journey_data["persona"], stages=journey_data["stages"]
#                 ),
#             },
#         ],
#         response_format=StageFeatures,
#     )
#     parameters = completion.choices[0].message.parsed

#     return parameters
#     # # Fetch data from database based on the parameters
#     # google_tag_data: dict = fetch_data(parameters["google"])
#     # # prompt 2: predict the stage based on the data
