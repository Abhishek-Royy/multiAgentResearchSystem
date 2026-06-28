from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search,scrape_url
import os
from dotenv import load_dotenv
load_dotenv()

llm=ChatMistralAI(model="mistral-small-2603",temperature=0)


# 1st agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    ) 

# 2nd agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


# Writter chain
writer_prompt=ChatPromptTemplate.from_messages([
    #     ( "system","You are an expert research writer. Write clear, structured and insightful reports."),
    #     ("human","""Write a detailed research reports on the topic below.
    # Topic:{topic}
    # Research Gathered:{research}

    # Structure the report as:
    # - Introduction
    #      - Key finding(minimum 4 well-explained points)
    #      - Conclusion
    #      - Sources or Reference(list all URLs found in the research)
    #      Be detailed, factual and professional.  
    #      """)

       (
        "system",
        """
You are a senior research analyst and professional technical writer.

Your responsibility is to transform raw research collected from multiple web sources into a comprehensive, accurate, and well-structured report.

Guidelines:
- Use ONLY the provided research.
- Never fabricate facts or statistics.
- Maintain a professional, objective, and neutral tone.
- Organize the report using Markdown headings.
- Explain concepts clearly with sufficient detail.
- Combine information from multiple sources into a coherent narrative.
- Remove duplicate information.
- If information from different sources conflicts, mention the disagreement instead of choosing one.
- If some information is unavailable, explicitly state that it could not be verified.
- Preserve technical accuracy.
"""
    ),

    (
        "human",
        """
Write a comprehensive research report on the following topic.

# Research Topic
{topic}

# Research Data
{research}

Generate a report with the following structure:

# Title

A concise and descriptive title.

# Executive Summary

Provide a 3–5 sentence overview of the report.

# Introduction

Introduce the topic and explain why it is important.

# Background

Provide relevant background information and context.

# Key Findings

Present at least 4–6 major findings.

For each finding:
- Use a descriptive heading.
- Explain it in detail.
- Include relevant facts, examples, or statistics if available.
- Mention benefits, limitations, or implications when appropriate.

# Analysis

Analyze the collected information:
- Compare viewpoints if multiple exist.
- Discuss trends or patterns.
- Explain practical implications.

# Conclusion

Summarize the most important insights.

# Future Outlook

Describe expected future developments, challenges, or opportunities.

# References

List every source URL mentioned in the research.
Do not invent URLs.
"""
    )

])

# LCLE pipeline syntax
writer_chain=writer_prompt | llm | StrOutputParser()


# critic_chain
critic_prompt=ChatPromptTemplate.from_messages([
      (
        "system",
        """
You are a senior research editor and quality assurance reviewer.

Your responsibility is to critically evaluate research reports and provide detailed, constructive feedback.

Evaluate the report based on the following criteria:

1. Accuracy
   - Are all claims supported by the provided research?
   - Are there any unsupported assumptions or hallucinations?

2. Completeness
   - Does the report fully answer the research topic?
   - Are any important aspects missing?

3. Organization
   - Is the report logically structured?
   - Are headings and sections clear?

4. Clarity
   - Is the writing concise, readable, and professional?
   - Are technical concepts explained clearly?

5. Depth
   - Does the report go beyond surface-level information?
   - Are findings sufficiently detailed?

6. Consistency
   - Are there contradictions or repeated information?

7. References
   - Are all URLs from the research included?
   - Are references properly listed?

Rules:
- Be objective and constructive.
- Do NOT rewrite the report.
- Identify both strengths and weaknesses.
- Suggest specific improvements.
- If the report is excellent, explicitly state that only minor improvements are needed.
"""
    ),

    (
        "human",
        """
Research Topic:
{topic}

Original Research:
{research}

Generated Report:
{report}

Review the report and provide feedback in the following format:

# Overall Score
(Give a score out of 10)

# Strengths
- List the strengths.

# Weaknesses
- List all weaknesses.

# Missing Information
- Mention important missing points.

# Hallucination Check
- Identify any unsupported or fabricated claims.

# Improvement Suggestions
- Provide actionable recommendations.

# Final Verdict
Choose one:
- Accept
- Minor Revision
- Major Revision
"""
    )
])

critic_chain=critic_prompt | llm | StrOutputParser()

