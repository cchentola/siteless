SYSTEM = """
    You are a website content generation assistant.
    Your objective is to suggest contents to help a site owner maximize customer conversion rate.
    """

COMPETITOR = """
    Based on the owner's description of their business: ```$summary```,
    What are their top three competitors in $location?
"""


CUSTOMER_PERSONAS = """
    Based on the owner's decription of their business ```$summary``` and $competitors,
    list some potential customer personas.
    """

JOURNEY_MAP = """
    Now, the owner wants to focuse on $selected_persona.
    List stages in the customer journey that the persona would go through.
"""

STAGE_FEATURES = """
    Given a customer persona $persona and their journey map $stages, what data collected by Google Tag Manager would be useful to predict the stage the customer is at?
"""

CONTENT = """
    Now, suggest five options of $content_type, i.e. $type_description to help convert $persona from $stage to the next in this journey map $journey_map,
"""
