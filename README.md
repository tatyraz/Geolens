# GeoLens: AI-Powered Geopolitical Media Bias Detector

**GeoLens** is an advanced analysis system built with **Google ADK** designed to identify and mitigate geopolitical bias in news reporting. By leveraging the **Gemini 2.5 Flash** model, it dissects news articles to reveal hidden framings, missing perspectives, and provides a balanced rewrite of the content.

## System Architecture

The following text-based A2A (Agent-to-Agent) flow illustrates how the specialized agents connect to process a news URL:

**User Input (URL)**  
      ↓  
**Extractor Agent** (Scrapes article text and identifies core claims/framing)  
      ↓  
**Bias Classifier Agent** (Analyzes types and severity of bias found in the extraction)  
      ↓  
**Perspective Agent** (Identifies what information or voices were omitted)  
      ↓  
**Scorer Agent** (Assigns a 0-100 neutrality score based on cumulative findings)  
      ↓  
**Rewriter Agent** (Produces a final, neutral summary of the article)  
      ↓  
**Root Agent (GeoLens)** (Orchestrates the components and delivers the complete analysis report)

---

## Agent Profiles

GeoLens utilizes **five specialized agents**, each with a distinct role in the geopolitical analysis pipeline:

1.  **Extractor Agent**: Acts as the primary data miner. It uses the `scrape_article` tool to retrieve text and isolates **3-5 key claims**, identifies **emotionally loaded words**, and defines the article's initial **framing**.
2.  **Bias Classifier Agent**: Serves as a media bias expert. It categorizes bias into five specific types—**political, emotional, omission, framing, or source bias**—and rates the **severity** as Low, Medium, or High.
3.  **Perspective Agent**: Functions as a journalism auditor. This agent looks for **missing voices**, **omitted context**, and flags **unanswered questions** that may lead to a one-sided narrative.
4.  **Scorer Agent**: Operates as a neutrality metricist. It calculates a **Neutrality Score out of 100** and provides a breakdown of language, perspective, framing, and source bias.
5.  **Rewriter Agent**: Acts as a neutral journalist. It synthesizes the analysis to **rewrite the article** (max 150 words), removing bias and incorporating missing perspectives to ensure a fair presentation of all sides.

---

## Setup Instructions

To run GeoLens locally, follow these steps based on the project structure:

### 1. Prerequisites
Ensure you have **Python 3.10+** installed along with the following dependencies:
*   **google-adk**: For agent orchestration.
*   **trafilatura**: For web scraping and text extraction.

```bash
pip install google-adk trafilatura
```

### 2. Configuration
The project uses the **Gemini 2.5 Flash** model. You will need to ensure your environment is configured with the necessary Google Cloud or AI Studio API credentials to access this model via the ADK.

### 3. Project Structure
Organize your files as shown in the sources:
*   `agent.py`: Contains the `root_agent` and core scraping tool.
*   `agents/extractor.py`: Logic for the Extractor Agent.
*   `agents/bias_classifier.py`: Logic for the Bias Classifier Agent.
*   `agents/perspective.py`: Logic for the Perspective Agent.
*   `agents/scorer.py`: Logic for the Scorer Agent.
*   `agents/rewriter.py`: Logic for the Rewriter Agent.

### 4. Running the Project
Initialize the `root_agent` from `agent.py`. When prompted, provide a **news article URL**. The system will automatically:
1.  **Scrape** the content using `trafilatura`.
2.  **Process** the text through the agent chain.
3.  **Output** a comprehensive report including key claims, bias detection, missing context, a neutrality score, and a neutral rewrite.