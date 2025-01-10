
# Project Title

A brief description of what this project does and who it's for

# AI Evaluation Simulator - README

## Overview
The **AI Evaluation Simulator** is a Streamlit-based application designed to evaluate the performance of AI models on multiple-choice questions (MCQs). It enables users to assess the accuracy of AI-generated answers by comparing them with a set of correct answers provided by the user. This application is ideal for testing AI models' ability to answer MCQs accurately and evaluating their performance with a detailed report.

## Key Features
1. **Upload MCQs**: Users can upload a CSV file containing MCQs, and the AI will generate answers for each question.
2. **Answer Evaluation**: Upload a second CSV file with correct answers, and the app will evaluate the AI's performance.
3. **Progress Bars**: The app includes progress bars for user-friendly feedback during processing.
4. **Detailed Metrics**:
   - Total number of questions.
   - Number of correct answers.
   - Accuracy percentage.
5. **Data Visualization**: View detailed results in a tabular format within the app.
6. **Download Reports**:
   - AI-generated answers.
   - Evaluation results in CSV format.

## What is AI Evaluation?
AI evaluation refers to the process of assessing the performance of an AI model in specific tasks. In this application, the AI is tasked with answering MCQs. The evaluation involves comparing the AI-generated answers against a set of predefined correct answers to determine:
- How many answers the AI got correct.
- The overall accuracy of the AI model.

### How is it Evaluated?
1. **Input**:
   - **MCQs**: A CSV file containing questions and multiple-choice options.
   - **Correct Answers**: A CSV file with questions and their corresponding correct answers.
2. **Processing**:
   - The AI generates answers based on the provided questions and options.
   - The app compares these answers to the correct answers.
3. **Output**:
   - Accuracy percentage calculated as:
     ```
     Accuracy = (Number of Correct Answers / Total Questions) × 100
     ```
   - Detailed evaluation results, including whether each answer is correct or not.

## Application Workflow
1. **Upload MCQs**:
   - Upload a CSV file with the following required columns:
     - `Question`: The question text.
     - `Option A`, `Option B`, `Option C`, `Option D`: The multiple-choice options.

   - Example:
     ```csv
     Question,Option A,Option B,Option C,Option D
     Who painted the Mona Lisa?,Vincent van Gogh,Leonardo da Vinci,Pablo Picasso,Michelangelo
     In which year did the Titanic sink?,1905,1912,1920,1898
     ```

   - The app processes the file and displays the questions in a table.

2. **Generate AI Answers**:
   - For each question, the AI generates an answer based on logical reasoning.
   - A progress bar indicates the status of the answer generation process.
   - The generated answers are displayed and available for download.

3. **Upload Correct Answers**:
   - Upload a second CSV file with the following required columns:
     - `Question`: The question text (must match the MCQ file).
     - `Answer`: The correct answer (e.g., `Option B`).

   - Example:
     ```csv
     Question,Answer
     Who painted the Mona Lisa?,Option B
     In which year did the Titanic sink?,Option B
     ```

   - The app processes the file and compares the AI's answers to the correct answers.

4. **Evaluate Results**:
   - The app calculates the accuracy of the AI model.
   - A detailed results table is displayed, showing:
     - Each question.
     - Correct answer.
     - AI-generated answer.
     - Whether the AI answer was correct.
   - Users can download the evaluation report.

## Detailed Steps
### Step 1: Upload MCQs
1. Click on the "Upload MCQs" button.
2. Select a CSV file containing the questions and options.
3. View the uploaded data in the app.

### Step 2: Generate AI Answers
1. Once the MCQ file is uploaded, the app generates answers using GPT-4.
2. A progress bar shows the status of the generation process.
3. The answers are displayed in a table, and you can download them as a CSV.

### Step 3: Upload Correct Answers
1. Upload a CSV file containing the correct answers for the MCQs.
2. The app validates the file and displays the uploaded data.

### Step 4: Evaluate Results
1. The app compares the AI's answers to the correct answers.
2. Metrics such as accuracy percentage and the number of correct answers are displayed.
3. Download the evaluation results as a CSV.

## Features in Detail
### Progress Bars
- Real-time progress indicators for:
  - AI answer generation.
  - Evaluation processing.
- Keeps the user informed about task completion status.

### Metrics
- **Total Questions**: The number of questions in the evaluation.
- **Correct Answers**: The number of answers the AI got correct.
- **Accuracy Percentage**: The percentage of correct answers.

### Download Options
- **AI Answers**: Download the AI-generated answers as a CSV.
- **Evaluation Results**: Download the evaluation results, including correctness, as a CSV.

## How It Works
1. **Backend**:
   - Uses GPT-4 for generating answers.
   - Compares answers programmatically with the correct answers.
   - Handles edge cases such as mismatched questions or missing columns.

2. **Frontend**:
   - Built with Streamlit for a simple, interactive UI.
   - Displays data and results in tables with download options.
   - Includes progress bars for user feedback.

3. **Technology Stack**:
   - **Streamlit**: For building the user interface.
   - **Pandas**: For data processing.
   - **Requests**: For API calls to GPT-4.

## Requirements
### Dependencies
- Python 3.8+
- Required Python libraries (install using `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

### File Structure
Ensure the following directory structure:
```
EvaluationSimulator/
├── app/
│   ├── main.py
│   └── utils/
│       ├── api_utils.py
│       ├── evaluation.py
│       ├── file_utils.py
│       └── prompts.py
├── requirements.txt
├── sample_mcqs.csv
├── sample_answers.csv
```

## Usage
### Running the Application
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app/main.py
   ```

## Sample Files
### Sample MCQ File (`sample_mcqs.csv`)
```csv
Question,Option A,Option B,Option C,Option D
Who painted the Mona Lisa?,Vincent van Gogh,Leonardo da Vinci,Pablo Picasso,Michelangelo
In which year did the Titanic sink?,1905,1912,1920,1898
```

### Sample Answer File (`sample_answers.csv`)
```csv
Question,Answer
Who painted the Mona Lisa?,Option B
In which year did the Titanic sink?,Option B
```

## Future Improvements
- Add support for more file formats.
- Integrate additional AI models for evaluation.
- Add charts and graphs for better data visualization.

Feel free to contribute to the project or raise issues on the GitHub repository!