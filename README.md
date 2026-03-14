# GeoLens: AI-Powered Geopolitical Media Bias Detector

**GeoLens** is an advanced media analysis system built with **Google ADK** and **Gemini 2.5 Flash**. It is designed to deconstruct news articles, identify underlying geopolitical biases, uncover missing perspectives, and provide a neutral alternative to biased reporting.

---

## 🏗 System Architecture (Agent-to-Agent Flow)

The system operates through a root orchestrator that delegates tasks to specialized agents and tools.

```text
[User Input: URL(s)] 
       |
       v
[Root Agent: geolens] <-----------------------+
       |                                      |
       +--- [Tool: scrape_article]            |
       |                                      |
       +--- [Agent: extractor_agent] ---------+--> (Claims, Framing, Loaded Words)
       |                                      |
       +--- [Agent: bias_classifier_agent] ---+--> (Bias Types, Direction, Severity)
       |                                      |
       +--- [Agent: perspective_agent] -------+--> (Missing Context/Voices)
       |                                      |
       +--- [Agent: scorer_agent] ------------+--> (Neutrality Score 0-100)
       |                                      |
       +--- [Agent: rewriter_agent] ----------+--> (Neutral 150-word Rewrite)
       |                                      |
       +--- [Tool: search_related_articles] --+--> (Comparative Source Analysis)
       |
[Final Output Report]
```

---

## 🤖 Agent Profiles

GeoLens utilizes five specialized agents to provide a comprehensive bias report:

1.  **Extractor Agent (`extractor_agent`)**: Acts as a media analyst to scrape article text and extract the 3-5 most important claims, emotionally loaded words, and the overall framing of the piece.
2.  **Bias Classifier Agent (`bias_classifier_agent`)**: An expert in detection who categorizes bias into specific types: political, emotional, omission, framing, or source bias. It determines the bias direction and rates severity (Low, Medium, or High).
3.  **Perspective Agent (`perspective_agent`)**: A journalism expert focused on balance; it identifies missing voices, omitted context, and critical unanswered questions within a report.
4.  **Scorer Agent (`scorer_agent`)**: Quantifies neutrality on a scale of 0-100. It provides a breakdown across four categories—Language, Perspective, Framing, and Source—concluding with a one-sentence verdict.
5.  **Rewriter Agent (`rewriter_agent`)**: A neutral journalist that strips away loaded language and incorporates missing perspectives to create a fair, concise summary (max 150 words).

---

## 🛠 Tools

### News Search Tool (`search_related_articles`)
This tool allows GeoLens to look beyond a single source. It uses `googlesearch-python` to find three related news articles on the same topic. For each result, it uses `trafilatura` to fetch the content and provides a short summary, enabling the system to show how different outlets cover the same event.

---

## ⚙️ Local Setup

To run GeoLens locally, ensure you have Python installed and follow these steps:

1.  **Clone the repository and install dependencies:**
    ```bash
    pip install google-adk trafilatura googlesearch-python
    ```
2.  **Configure Environment Variables:**
    Set your Gemini API key:
    ```bash
    export GOOGLE_API_KEY='your_gemini_api_key'
    ```
3.  **Directory Structure:**
    Ensure your files are organized as follows:
    *   `agent.py` (Root agent)
    *   `agents/` (Contains `extractor.py`, `bias_classifier.py`, etc.)
    *   `tools/` (Contains `news_search.py`)

4.  **Run the application:**
    ```bash
    python agent.py
    ```

---

## 📖 Example Usage

### 1. Single Article Analysis
Input a single URL to receive a deep dive into its framing and neutrality.
*   **Input:** `https://example-news.com/geopolitical-event`
*   **Output includes:** Key claims, identified bias types (e.g., "Omission bias"), a neutrality score (e.g., "65/100"), and a 150-word neutral rewrite.

### 2. Two Article Comparison
Input two URLs to see how different media outlets contrast in their coverage.
*   **Input:** `URL_1`, `URL_2`
*   **Output includes:** Individual analysis for both articles followed by a **Bias Comparison** that highlights which article is more biased, what agenda each outlet is pushing, and a combined neutral summary of the event.