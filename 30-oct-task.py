from crewai import Agent, Crew, Task, Process

# Agent 1: Researcher
researcher = Agent(
    name="Researcher",
    description="Finds information about Artificial Intelligence.",
    role="AI Research Expert",
    goal="Gather the latest and most relevant info about AI.",
    backstory="An expert researcher who has spent years studying AI advances."
)

# Agent 2: Reporter
reporter = Agent(
    name="Reporter",
    description="Writes a summary based on research findings.",
    role="Technical Writer",
    goal="Create a clear and concise summary for AI research topics.",
    backstory="A seasoned reporter specializing in scientific news."
)

# Research task
research_task = Task(
    agent=researcher,
    description="Research what is Artificial Intelligence."
)

# Reporting task
report_task = Task(
    agent=reporter,
    description="Summarize the findings about Artificial Intelligence."
)

# Crew setup: sequential execution
crew = Crew(
    agents=[researcher, reporter],
    tasks=[research_task, report_task],
    process=Process.sequential
)

if __name__ == "__main__":
    crew.kickoff(inputs={"topic": "Artificial Intelligence"})