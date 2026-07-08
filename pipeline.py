from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain


def get_last_message_content(result):
    """
    Extract final message content from LangChain agent result.
    """

    message = result["messages"][-1]
    content = message.content

    if isinstance(content, list):
        return "\n".join(str(item) for item in content)

    return str(content)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # Step 1 - Search Agent
    print("\n" + "=" * 50)
    print("Step 1: Running Search Agent...")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Find recent, reliable, and detailed information on this topic: {topic}. "
                    f"Provide titles, summaries, and URLs for all sources."
                )
            }
        ]
    })

    state["search_result"] = get_last_message_content(search_result)

    print("\nSearch Agent Output:")
    print(state["search_result"])

    # Step 2 - Reader Agent
    print("\n" + "=" * 50)
    print("Step 2: Running Reader Agent...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"From the search results below, choose the most relevant URL and scrape it "
                    f"for deeper factual information.\n\n"
                    f"Search Results:\n{state['search_result']}"
                )
            }
        ]
    })

    state["reader_result"] = get_last_message_content(reader_result)

    print("\nReader Agent Output:")
    print(state["reader_result"])

    # Step 3 - Writer Chain
    print("\n" + "=" * 50)
    print("Step 3: Running Writer Chain...")
    print("=" * 50)

    research_combined = (
        f"Search Results:\n{state['search_result']}\n\n"
        f"Scraped Content:\n{state['reader_result']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:")
    print(state["report"])

    # Step 4 - Critic Chain
    print("\n" + "=" * 50)
    print("Step 4: Running Critic Chain...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic Feedback:")
    print(state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("Enter research topic: ")
    run_research_pipeline(topic)