# AI Evaluation Simulator

## Join the Community  
[Join Curious PM Community](https://curious.pm/) to connect, share, and learn with others!

---

## About This Project

The AI Evaluation Simulator is a simple web app built with Streamlit that helps you evaluate AI performance on multiple-choice questions (MCQs). It generates AI answers using GPT-4 and compares them with the correct answers to calculate accuracy.

---

## What This App Does  

- **Upload MCQ CSV:** Add a file with questions and answer choices.  
- **AI Answer Generation:** The app generates answers using GPT-4.  
- **Evaluation:** Compare AI-generated answers with correct answers.  
- **Download Reports:** Save results for review.  

### Key Features  

- **Easy to Use:** Simple interface to upload files and view results.  
- **Real-Time Progress:** See the progress of AI answer generation.  
- **Downloadable Reports:** Save AI answers and evaluation results.  
- **Error Handling:** Helpful messages if issues occur.  

---

## How to Use the App (Step-by-Step)  

### 1. Install Requirements  

Make sure you have Python installed, then install required libraries:  

```bash
pip install streamlit pandas
```

---

### 2. Set Up the Project  

Organize your files like this:  

```
EvaluationSimulator/
├── README.md                  # Project documentation
├── TestData/                   # Sample data for testing
│   ├── sample_answers.csv       # Sample correct answers CSV
│   └── sample_mcqs.csv          # Sample MCQ CSV
├── app/                        # Application source code
│   ├── utils/                   # Utility functions
│   │   ├── __init__.py           # Initialization for the utils module
│   │   ├── api_utils.py          # Handles GPT-4 API queries
│   │   ├── evaluation.py         # Compares AI-generated answers with correct ones
│   │   ├── file_utils.py         # File handling utilities
│   │   └── prompts.py            # Stores prompt templates for AI requests
├── main.py                      # Main Streamlit application script
└── requirements.txt              # List of dependencies required to run the project
```

---

### 3. Run the App  

Start the app with this command:  

```bash
streamlit run main.py
```

---

### 4. Use the App  

1. **Upload MCQs:**  
   - Upload a CSV file with columns: `Question`, `Option A`, `Option B`, `Option C`, `Option D`.  

2. **Generate AI Answers:**  
   - Click the button to generate AI responses for the uploaded questions.  

3. **Download AI Answers:**  
   - Save the AI-generated answers as a CSV file.  

4. **Upload Correct Answers:**  
   - Upload a CSV with columns: `Question` and `Answer`.  

5. **View Results:**  
   - The app shows accuracy, correct answers, and detailed results.  

6. **Download Evaluation Report:**  
   - Save the evaluation results for future reference.  

---

### 5. Implementing It Yourself  

Follow these steps to create the app on your own:  

1. **Install Required Libraries:**  
   ```bash
   pip install streamlit pandas
   ```

2. **Write the App Code:**  

   ```python
   import streamlit as st
   import pandas as pd
   from utils.api_utils import get_gpt4_answer
   from utils.evaluation import evaluate_answers

   st.title("AI Evaluation Simulator")

   uploaded_mcq = st.file_uploader("Upload MCQs CSV", type=["csv"])
   if uploaded_mcq:
       mcqs_df = pd.read_csv(uploaded_mcq)
       st.write(mcqs_df)

       if st.button("Generate AI Answers"):
           mcqs_df["AI Answer"] = mcqs_df["Question"].apply(lambda q: get_gpt4_answer(q, mcqs_df.columns[1:5]))
           st.write(mcqs_df)

       st.download_button("Download AI Answers", mcqs_df.to_csv(index=False), "ai_answers.csv")

   uploaded_eval = st.file_uploader("Upload Evaluation CSV", type=["csv"])
   if uploaded_eval:
       eval_df = pd.read_csv(uploaded_eval)
       accuracy, results = evaluate_answers(mcqs_df, eval_df)
       st.write(f"Accuracy: {accuracy}%")
       st.write(results)

       st.download_button("Download Results", results.to_csv(index=False), "evaluation_results.csv")
   ```

3. **Secure Your API Keys:**  
   - Save your credentials in `.streamlit/secrets.toml` or environment variables.

4. **Customize the Interface:**  
   - Modify the design to fit your needs using Streamlit.

5. **Run and Deploy:**  
   - Use `streamlit run main.py` to test locally and deploy online via Heroku, AWS, or Streamlit Cloud.

---

## What Happens at Each Step  

### 1. Upload MCQs  
- The app allows you to upload an MCQ CSV file.  
- It checks if the file contains the required columns:  
  - `Question`, `Option A`, `Option B`, `Option C`, `Option D`.  
- If the file is valid, it displays the questions in an interactive table.  
- If any required columns are missing, an error message is shown.  

**Example Input Format:**  

| Question                  | Option A | Option B | Option C | Option D |
|---------------------------|----------|----------|----------|----------|
| What is AI?               | A tool   | A system | A concept| A theory |
| Who invented Python?      | Rossum   | Gates    | Jobs     | Turing   |

---

### 2. Generate AI Answers  
- The uploaded questions are sent to GPT-4 for processing.  
- AI analyzes the question and available options to select the most appropriate answer.  
- A progress bar tracks the answer generation process.  
- Once complete, AI-generated answers are displayed alongside the questions.  
- If an error occurs (e.g., API failure), the user is notified with helpful messages.  

**Example Output:**  

| Question                  | AI Answer |
|---------------------------|-----------|
| What is AI?               | A system  |
| Who invented Python?      | Rossum    |

---

### 3. Upload Answer Key  
- Users upload a CSV containing the correct answers.  
- The app verifies if the uploaded file includes the required columns:  
  - `Question`, `Answer`.  
- It ensures that the provided answer key matches the uploaded MCQs.  
- If there are mismatched questions or missing fields, an error is displayed.  

**Expected Answer Key Format:**  

| Question                  | Answer   |
|---------------------------|----------|
| What is AI?               | A system |
| Who invented Python?      | Rossum   |

---

### 4. Evaluate  
- The AI-generated answers are compared with the correct answers.  
- The app calculates performance metrics, such as:  
  - **Total Questions:** Number of questions evaluated.  
  - **Correct Answers:** Number of correct AI responses.  
  - **Accuracy:** Percentage of correct answers out of the total.  
- The evaluation results are displayed in an easy-to-read table with visual indicators for correct and incorrect answers.  

**Example Evaluation Report:**  

| Question                  | AI Answer | Correct Answer | Correct? |
|---------------------------|-----------|----------------|----------|
| What is AI?               | A system  | A system       | ✔        |
| Who invented Python?      | Rossum    | Rossum         | ✔        |

---

### 5. Download Reports  
- After evaluation, users can download detailed reports as CSV files.  
- Reports include:  
  - The original MCQs.  
  - AI-generated answers.  
  - Correct answers.  
  - Evaluation results (correct/incorrect status).  
- These reports can be used for further analysis and tracking AI performance over time.  

**Example Downloadable Report:**  

```
Question,AI Answer,Correct Answer,Correct?
"What is AI?", "A system", "A system", "True"
"Who invented Python?", "Rossum", "Rossum", "True"
```

---

### 6. Review and Improve  
- Users can analyze the evaluation results to identify patterns in AI performance.  
- Areas with incorrect answers can be highlighted for further model fine-tuning.  
- The process can be repeated with improved MCQ sets to refine AI responses.  

---
## Project Folder Structure

Below is the project folder structure with explanations of the purpose of each file and directory.

```
EvaluationSimulator/
├── README.md
├── TestData/
│   ├── sample_answers.csv
│   └── sample_mcqs.csv
├── app/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── api_utils.py
│   │   ├── evaluation.py
│   │   ├── file_utils.py
│   │   └── prompts.py
├── main.py
└── requirements.txt
```

### Folder and File Descriptions

#### 1. **README.md**
   - This file provides documentation about the project, including instructions on installation, usage, and troubleshooting.

#### 2. **TestData/** _(Sample Data)_
   - Contains sample CSV files used to test the app.  
   - **`sample_answers.csv`** – A sample file containing correct answers for evaluation.  
   - **`sample_mcqs.csv`** – A sample file with multiple-choice questions for AI processing.

#### 3. **app/** _(Application Source Code)_
   - This folder contains the core logic of the application, including utilities for processing MCQs and handling AI interactions.

   **Inside `app/utils/`:**
   
   - **`__init__.py`** – Initializes the utils package, allowing it to be imported as a module.  
   - **`api_utils.py`** – Handles communication with the GPT-4 API to generate answers based on uploaded MCQs.  
   - **`evaluation.py`** – Compares AI-generated answers with correct answers and calculates accuracy.  
   - **`file_utils.py`** – Provides helper functions for file operations, such as reading and writing CSV files.  
   - **`prompts.py`** – Stores predefined prompt templates used to query GPT-4 effectively.

#### 4. **main.py** _(Main Streamlit Application)_
   - This is the entry point of the application.  
   - It sets up the user interface with Streamlit, allowing users to:  
     - Upload MCQ and answer files.  
     - Generate AI responses.  
     - Evaluate AI performance and download reports.

#### 5. **requirements.txt** _(Dependencies List)_
   - A text file listing all required Python packages to run the application.  
   - Install dependencies using the command:

     ```bash
     pip install -r requirements.txt
     ```


---
## Join the Community
[Join Curious PM Community](https://nas.io/curious-pm) to connect, share, and learn with others!

---
# Azure OpenAI Chat

This project provides an easy-to-use chat interface built with Streamlit and Azure OpenAI API. Users can ask questions, receive AI-powered responses in real-time, and adjust model settings to refine responses.

## What the Code Does
This project allows users to interact with an AI chatbot powered by Azure OpenAI's GPT model. The app lets users enter queries, receive instant responses, and fine-tune parameters such as randomness and response diversity to meet their needs.

### Features:
- **Real-time Chat:** Instantly interact with AI through a user-friendly interface.
- **Streaming Responses:** Responses are displayed dynamically as they are generated.
- **Adjustable Parameters:** Users can modify settings like `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` to change response behavior.
- **Chat History:** Messages are saved throughout the session.
- **Error Handling:** Provides helpful messages if something goes wrong.

---

## How to Use It (Step by Step)

### 1. Install Dependencies
Make sure Python is installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

### 2. Set Up API Credentials
You will receive Azure OpenAI API credentials. Add them to a configuration file.

Create a `.streamlit/secrets.toml` file with the following content:

```toml
AZURE_OPENAI_API_ENDPOINT = "your-api-endpoint-here"
AZURE_OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run the Application
Start the chatbot app with the command:

```bash
streamlit run app.py
```

### 4. Interact with the Chatbot
1. Type your query in the input field.
2. See responses appear in real-time.
3. Adjust AI settings from the sidebar.
4. Reset settings to default if needed.

### 5. Implementing at Your End
Follow these steps to build the chatbot on your own:

1. **Install the Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Write the Chatbot Code:**
   ```python
   import streamlit as st
   import requests

   st.title("Azure OpenAI Chat")

   endpoint = st.secrets["AZURE_OPENAI_API_ENDPOINT"]
   api_key = st.secrets["AZURE_OPENAI_API_KEY"]

   user_input = st.text_input("Enter your message")

   if st.button("Send"):
       response = requests.post(
           endpoint,
           headers={"api-key": api_key, "Content-Type": "application/json"},
           json={"messages": [{"role": "user", "content": user_input}], "max_tokens": 1000}
       )
       st.write(response.json())
   ```

3. **Secure API Credentials:**
   Store credentials safely in `.streamlit/secrets.toml`.

4. **Customize Your Chatbot:**
   Change the layout and parameters to match your needs.

5. **Run the Chatbot Locally:**
   ```bash
   streamlit run app.py
   ```

6. **Deploy the Chatbot:**
   Use platforms like Heroku, AWS, or Azure to make it available online.

---

## What Happens in Each Step

1. **App Setup:**
   - Loads API credentials from the secrets file.
   - Prepares chat history storage.

2. **User Input:**
   - Users type their questions in the input field.

3. **Processing the Query:**
   - The app sends the query to Azure OpenAI API.
   - The response is streamed back to the app.

4. **Displaying Response:**
   - The AI-generated response is shown in the chat window.

5. **Adjusting Parameters:**
   - Users can fine-tune settings to control response style and content.

6. **Session Management:**
   - The app remembers previous chats during the session.

---

## Folder Structure

```
project-folder/
│-- app.py                # Main chatbot application script
│-- requirements.txt      # Dependencies needed to run the app
│-- .streamlit/            
│   └── secrets.toml      # Stores API credentials
│-- README.md             # Documentation of the project
```

---

## Expected Output Example

**Input:** "Tell me about AI"

**Output:** "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence."

---

## Common Issues & Troubleshooting

1. **Invalid API Key:**
   - Double-check credentials in `.streamlit/secrets.toml`.

2. **Missing Modules:**
   - Install required packages using `pip install -r requirements.txt`.

3. **App Not Running:**
   - Ensure the correct command is used: `streamlit run app.py`.

4. **Slow Responses:**
   - Try reducing `max_tokens` in the API request.

---

## Security Considerations

- **Do not share your API keys.**
- Use environment variables for secure deployment.
- Regularly change API keys for better security.

---

## Link to Hosted Version
[View Live App](#) *(Insert actual deployment link here)*

---

## Screenshots

# Uploading MCQs:
<img src="https://github.com/user-attachments/assets/b02530ed-5c10-4fd9-9bd3-f1263b4631cc" style="width: 400px; image-rendering: optimizeSpeed;" alt="Uploading MCQs">

# AI Generated Answers:
<img src="https://github.com/user-attachments/assets/7b30006c-bf15-4de8-b2de-e21c82589644" style="width: 400px; image-rendering: optimizeSpeed;" alt="AI Generated Answers">

# Evaluation Results:
<img src="https://github.com/user-attachments/assets/d223bd54-46b8-4b21-ac24-ef1d7f1eb72f" style="width: 400px; image-rendering: optimizeSpeed;" alt="Evaluation Results">
---

## Video Overview
*A short video walkthrough will be provided explaining the app's features and usage.*


## Expected Output  

**Example Accuracy:**  

- **Total Questions:** 100  
- **Correct Answers:** 85  
- **Accuracy:** 85.00%  

---

## Common Issues & Solutions  

1. **Wrong CSV Format:**  
   - Ensure correct column names and formats are used.  

2. **Slow Performance:**  
   - Reduce the number of questions in the uploaded file.  

3. **App Not Running:**  
   - Use the correct command: `streamlit run main.py`.  

4. **AI Not Responding:**  
   - Check your GPT-4 API key in the `api_utils.py` file.  

---

## Hosted App  

[View Live App](#) *(Insert hosted link here)*  

---

## Security Tips  

- Never share your API keys publicly.  
- Use environment variables to store sensitive information.  
- Regularly rotate your API keys for security.  

