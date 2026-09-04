
from agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain,
)


def run_pipeline(topic: str):

    state = {}

    # Step 1 : Search Agent

    print("\n" + "=" * 60)
    print("Step-1: Search Agent is working...")
    print("=" * 60)

    search_agent = build_search_agent()

    search_result = search_agent.invoke(
        {
            "messages": [
                (
                    "user",
                    f"Find recent, reliable and detailed information about {topic}.",
                )
            ]
        }
    )

    state["search_results"] = search_result["messages"][-1].content

    print("\nSearch Results:\n")
    print(state["search_results"])

    # ==================================================
    # Step 2 : Reader Agent
    # ==================================================
    print("\n" + "=" * 60)
    print("Step-2: Reader Agent is working...")
    print("=" * 60)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke(
        {
            "messages": [
                (
                    "user",
                    f"""
From the search results below, identify the most relevant URL.

Use the scrape_url tool to scrape that URL.

Return only the scraped webpage content.

Search Results:

{state["search_results"]}
"""
                )
            ]
        }
    )

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\nScraped Content:\n")
    print(state["scraped_content"])

    # ==================================================
    # Step 3 : Writer
    # ==================================================
    print("\n" + "=" * 60)
    print("Step-3: Writer Agent...")
    print("=" * 60)

    research = f"""
SEARCH RESULTS

{state['search_results']}

===================================================

SCRAPED CONTENT

{state['scraped_content']}
"""

    state["report"] = writer_chain.invoke(
        {
            "topic": topic,
            "research": research,
        }
    )

    print("\nGenerated Report:\n")
    print(state["report"])

    # ==================================================
    # Step 4 : Critic
    # ==================================================
    print("\n" + "=" * 60)
    print("Step-4: Critic Agent...")
    print("=" * 60)

    state["feedback"] = critic_chain.invoke(
        {
            "topic": topic,
            "research": research,
            "report": state["report"],
        }
    )

    print("\nCritic Feedback:\n")
    print(state["feedback"])

    return state


if __name__ == "__main__":

    topic = input("Enter a research topic: ")

    run_pipeline(topic)
