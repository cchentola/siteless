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
    List some potential customer personas.
    For each persona, include a short definition of no more than 10 tokens.
    Example: First-time homebuyer: A person who is looking to buy their first home.
    """

GOALS = """
    What are the top 5 conversion goals for target customer persona: $selected_persona?
"""

JOURNEY_MAP = """
    Now, the owner wants to focus on $selected_persona. 
    List stages in the customer journey that the persona would go through to achieve $goals.
    Include the following stardard stages:
    - Awareness
    - Consideration
    - Evaluation
    - Purchase
    - Ownership
    - Loyalty
    - Evangelism
    Add additional stages if applicable.
"""

CONTENT = """
    Now, suggest five options of $content_type, i.e. $type_description to help convert $persona from $stage to the next in this journey map $journey_map.
    Use no more than $tokens tokens.
"""
