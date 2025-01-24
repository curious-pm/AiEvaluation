## Text Embedding Playground

Explore the power of text embeddings through an interactive application that enables semantic analysis and visualization of text relationships.

## Introduction

This application demonstrates how text embeddings, generated using Azure OpenAI, can be used to perform tasks such as:
- Analyzing similarity between texts
- Visualizing text relationships in 2D space
- Supporting applications like semantic search, recommendation systems, and more.

It leverages **Streamlit** for the user interface, **Azure OpenAI's text-embedding-ada-002** for embedding generation, and tools like **scikit-learn** and **Plotly** for visualization.

## Join the Community
[Join Curious PM Community](https://nas.io/curious-pm) to connect, share, and learn with others!

---
# Text Embedding Playground

This project provides an interactive playground to explore text embeddings using Azure OpenAI API. Users can input text, analyze embeddings, and visualize relationships through heatmaps and scatter plots.

## What the Code Does
This application enables users to:

- **Single Text Analysis:** Input a sentence and compare it with predefined reference phrases.
- **Multi-Text Analysis:** Compare multiple texts to analyze similarity and visualize them in a 2D space.
- **Educational Content:** Learn about text embeddings and their applications.

### Features:
- **Predefined Phrases:** Save and analyze a list of reference phrases.
- **Similarity Measurement:** Uses cosine similarity to find closest text matches.
- **Visual Representation:** Heatmaps and scatter plots for understanding relationships between texts.
- **User-Friendly Interface:** Built with Streamlit for ease of use.

---

## What are Text Embeddings?

**Text embeddings** are vectorized numerical representations of text that capture the semantic meaning of words, sentences, or paragraphs. They allow computers to:
- Compare text similarity.
- Perform clustering, classification, and information retrieval tasks.

For example:
- The phrase "I love programming" will have a vector close to "Coding is fun" but far from "It's raining outside."

Text embeddings are widely used in natural language processing (NLP) applications such as:
- Semantic search engines
- Recommendation systems
- Document similarity detection
- Question-answering systems

---

## Applications of Text Embeddings

Here are some real-world use cases:

1. **Semantic Search**: Searching for similar documents or responses by analyzing their embeddings instead of just keywords.
2. **Content Recommendation**: Recommending similar articles, videos, or products based on text descriptions.
3. **Text Classification**: Categorizing texts (e.g., spam detection, sentiment analysis).
4. **Question Answering**: Identifying the most relevant answer to a question using similarity scores.

---

## How to Use It (Step by Step)

### 1. Install Dependencies
Ensure Python is installed, then install required libraries:

```bash
pip install -r requirements.txt
```

### 2. Set Up API Credentials
Create a `.streamlit/secrets.toml` file with the following content:

```toml
[azure_openai]
api_key = "your-api-key-here"
target_url = "your-target-url-here"
```

### 3. Run the Application
Start the Streamlit app with the command:

```bash
streamlit run app.py
```

### 4. Use the Interface
1. **Enter predefined reference phrases.**
2. **Analyze single or multiple texts for similarity.**
3. **Visualize results using heatmaps and scatter plots.**

---

## Folder Structure

```
text_embeddings_playground/
├── README.md             # Documentation explaining the project and usage.
├── app.py                # Main Streamlit application script that handles UI and logic.
└── requirements.txt      # List of required Python libraries to run the application.
```

### Explanation of Files
- **README.md**
  - Contains details about the project, setup instructions, and usage guide.
- **app.py**
  - Core application script containing the Streamlit UI, API interactions, and visualization logic.
- **requirements.txt**
  - Lists all the dependencies required to run the app, ensuring environment consistency.

---

## Expected Output Example

**Input:** "AI is revolutionizing the world"

**Output:**

```
The closest phrases:
1. Artificial intelligence is fascinating (0.92)
2. ChatGPT is a powerful AI tool (0.89)
3. Machine learning is a subset of AI (0.87)
```

---

## Technologies Used

1. **Backend**:
   - **Azure OpenAI**: For generating text embeddings.
   - **Requests**: To interact with Azure APIs.

2. **Frontend**:
   - **Streamlit**: For the user interface.

3. **Visualization**:
   - **Plotly**: For interactive heatmaps and scatter plots.

4. **Machine Learning**:
   - **Scikit-learn**: For cosine similarity and PCA.

---

## Security Considerations

- **Do not share your API keys.**
- Use environment variables for production deployment.
- Regularly update API keys for security.

---

## Link to Hosted Version
[View Live App](#) *(Insert actual deployment link here)*

---

## Screenshots

### Chat Interface:
<img src="https://github.com/user-attachments/assets/f913c6f0-36bc-4a55-aff6-e5f2b85a5392" style="width: 400px; image-rendering: optimizeSpeed;" alt="Chat Interface">

### Single Text Analysis:
<img src="https://github.com/user-attachments/assets/88144ea5-2fc0-418b-9b12-1d5a01172225" style="width: 400px; image-rendering: optimizeSpeed;" alt="Heatmap Visualization">

### Heatmap & Scatter Plot Visualization:
<img src="https://github.com/user-attachments/assets/a310c9d1-f223-445e-ab8b-e6339feb22fe" style="width: 400px; image-rendering: optimizeSpeed;" alt="Scatter Plot Visualization">

---

## Video Overview
*A short video walkthrough will be provided explaining the app's features and usage.*

