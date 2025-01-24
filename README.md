## Join the Community  
[Join Curious PM Community](https://curious.pm/) to connect, share, and learn with others!

--- 

A Streamlit-based tool to generate AI answers for MCQs and evaluate accuracy against correct responses.

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

## Hosted App  

[View Live App](#) *(Insert hosted link here)*  

---


## Screenshots

### Uploading MCQs:
<img src="https://github.com/user-attachments/assets/b02530ed-5c10-4fd9-9bd3-f1263b4631cc" style="width: 400px; image-rendering: optimizeSpeed;" alt="Uploading MCQs">

### AI Generated Answers:
<img src="https://github.com/user-attachments/assets/7b30006c-bf15-4de8-b2de-e21c82589644" style="width: 400px; image-rendering: optimizeSpeed;" alt="AI Generated Answers">

### Evaluation Results:
<img src="https://github.com/user-attachments/assets/d223bd54-46b8-4b21-ac24-ef1d7f1eb72f" style="width: 400px; image-rendering: optimizeSpeed;" alt="Evaluation Results">

---

## Video Overview
*A short video walkthrough will be provided explaining the app's features and usage.*


## Security Considerations

- **Do not share your API keys.**
- Use environment variables for secure deployment.
- Regularly change API keys for better security.

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

## Security Tips  

- Never share your API keys publicly.  
- Use environment variables to store sensitive information.  
- Regularly rotate your API keys for security.  

