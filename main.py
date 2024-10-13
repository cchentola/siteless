import json
from collections import defaultdict

from fastapi import FastAPI

from models import Business
from routes.content_routes import content_router, get_content_suggestions
from routes.customer_routes import customer_router, get_customer_journey
from routes.owner_routes import owner_router, get_competitors, get_customer_personas

app = FastAPI()

app.include_router(owner_router, prefix="/owner", tags=["owner"])
app.include_router(customer_router, prefix="/customer", tags=["customer"])
app.include_router(content_router, prefix="/content", tags=["content"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    # business_data = {
    #     "summary": "I own a real estate listing sites.",
    #     "specific": True,
    #     "region": "Northeast",
    #     "state": "New York",
    #     "city": "New York",
    # }
#     competitors = get_competitors(Business(**business_data))
#     print(competitors)
#     personas = get_customer_personas(competitors).model_dump()
#     content_options = defaultdict(dict)
#     for persona in personas["personas"]:
#         content_options[persona] = defaultdict(dict)
#         print(f"Customer persona: {persona}")

#         customer_journey = get_customer_journey(persona)

#         for content_type in ["h1", "h2", "h3", "p"]:
#             options = get_content_suggestions(customer_journey, content_type)
#             for _stage, _options in options.items():
#                 content_options[persona][_stage][content_type] = _options
#         break
#     with open("sample_content_options.json", "w") as f:
#         json.dump(content_options, f)
