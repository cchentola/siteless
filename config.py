import json

MODEL = "gpt-4o-mini-2024-07-18"

CONTENT_TYPES = {
    "h1": {"max_tokens": 4, "description": "Main Heading for the home page"},
    "h2": {"max_tokens": 12, "description": "Subheading for the home page"},
    "h3": {"max_tokens": 8, "description": "Sub-subheading for the home page"},
    "p": {"max_tokens": 20, "description": "Paragraph for the home page"},
}

PERSONA_STAGES = {
    "First-time homebuyer": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Purchase",
        "Post-Purchase Support",
        "Ownership",
        "Loyalty",
        "Evangelism",
    ],
    "Real estate investor": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Purchase",
        "Ownership",
        "Loyalty",
        "Evangelism",
        "Post-Investment Engagement",
        "Referral",
    ],
    "Luxury homebuyer": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Purchase",
        "Post-Purchase",
        "Ownership",
        "Loyalty",
        "Evangelism",
        "Referral",
    ],
    "Renters": [
        "Awareness",
        "Interest",
        "Consideration",
        "Evaluation",
        "Decision",
        "Purchase",
        "Move-in",
        "Ownership",
        "Loyalty",
        "Advocacy",
        "Evangelism",
    ],
    "Relocating professionals": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Purchase",
        "Usage",
        "Ownership",
        "Loyalty",
        "Advocacy",
        "Evangelism",
    ],
    "Downsizers": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Consultation",
        "Purchase",
        "Ownership",
        "Loyalty",
        "Evangelism",
    ],
    "Vacation homebuyer": [
        "Awareness",
        "Consideration",
        "Evaluation",
        "Purchase",
        "Ownership",
        "Loyalty",
        "Evangelism",
        "Search",
        "Engagement",
    ],
}
