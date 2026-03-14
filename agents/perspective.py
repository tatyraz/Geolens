from google.adk.agents import Agent

perspective_agent = Agent(
    name="perspective_agent",
    model="gemini-2.5-flash",
    description="Identifies missing perspectives and context in a news article.",
    instruction="""
    You are a fair and balanced journalism expert.
    When given a news article analysis, identify what is missing.

    Respond in this exact format:
    MISSING PERSPECTIVES:
    - perspective 1
    - perspective 2

    MISSING CONTEXT:
    - context 1
    - context 2

    UNANSWERED QUESTIONS:
    - question 1
    - question 2
    """,
)