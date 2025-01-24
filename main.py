import streamlit as st
import sys
import os
import pandas as pd
import time  # For simulating progress during AI answer generation

# Add the `app` directory to PYTHONPATH dynamically to access custom utility modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Import necessary functions from utility modules
from utils.api_utils import get_gpt4_answer  # Function to get AI-generated answers
from utils.evaluation import evaluate_answers  # Function to evaluate AI-generated answers

# Custom CSS styling for the Streamlit app to enhance UI
st.markdown("""
    <style>
        .css-1d391kg {
            padding-top: 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        .sidebar-text {
            padding: 1rem 0;
            border-bottom: 1px solid #e9ecef;
        }
        .sidebar-link {
            color: #0066cc;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        .sidebar-link:hover {
            color: #004494;
            text-decoration: underline;
        }
        .stProgress > div > div > div > div {
            background-color: #0066cc;
        }
        .stDownloadButton {
            margin-top: 1rem;
        }
        .stAlert {
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

def initialize_sidebar():
    """Initialize the sidebar with navigation and help information."""
    with st.sidebar:
        st.title("📊 Navigation")
        
        # Project Information Section
        st.markdown("---")
        st.markdown("""
            <div class='sidebar-text'>
                <h3>About</h3>
                <p>AI Evaluation Simulator helps assess AI model performance on multiple-choice questions.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Links section with useful resources
        st.markdown("---")
        st.markdown("""
            <div class='sidebar-text'>
                <h3>📝 Quick Links</h3>
                <ul style='list-style-type: none; padding-left: 0;'>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://github.com/curious-pm/EvaluationSimulator-Playground' class='sidebar-link'>
                            📦 GitHub Repository
                        </a>
                    </li>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://github.com/AjinkyaSambare/EvaluationSimulator-Playground/blob/main/TestData/sample_mcqs.csv' class='sidebar-link'>
                            📄 Sample MCQ CSV
                        </a>
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        # Help section with usage guidelines
        st.markdown("---")
        with st.expander("ℹ️ Help"):
            st.markdown("""
                1. Upload your MCQ CSV file (columns: Question, Option A-D)
                2. Wait for AI to generate answers
                3. Upload evaluation CSV (columns: Question, Answer)
                4. Review results and download reports
            """)

def process_mcq_file(uploaded_file):
    """Process the uploaded MCQ file and generate AI answers."""
    try:
        st.write("Loading MCQ file...")
        mcqs_df = pd.read_csv(uploaded_file)

        # Display uploaded file content
        with st.expander("View Uploaded MCQs", expanded=True):
            st.dataframe(mcqs_df, use_container_width=True)

        # Validate required columns
        required_columns = ["Question", "Option A", "Option B", "Option C", "Option D"]
        if not all(col in mcqs_df.columns for col in required_columns):
            st.error("CSV must have 'Question', 'Option A', 'Option B', 'Option C', and 'Option D' columns.")
            return None

        # Generate AI answers
        st.write("Generating answers using GPT-4...")
        progress_bar = st.progress(0)
        total_questions = len(mcqs_df)

        mcqs_df["AI Answer"] = None
        for index, row in mcqs_df.iterrows():
            mcqs_df.at[index, "AI Answer"] = get_gpt4_answer(
                row["Question"], 
                [row["Option A"], row["Option B"], row["Option C"], row["Option D"]]
            )
            progress_bar.progress((index + 1) / total_questions)

        st.success("AI answers generated successfully!")
        with st.expander("View Generated Answers", expanded=True):
            st.dataframe(mcqs_df, use_container_width=True)

        # Provide download option
        st.download_button("Download AI Answers", data=mcqs_df.to_csv(index=False), file_name="ai_answers.csv", mime="text/csv")
        return mcqs_df

    except Exception as e:
        st.error(f"An error occurred while processing the MCQs: {e}")
        return None

def display_evaluation_results(mcqs_df, eval_file):
    """Display evaluation results and performance metrics."""
    try:
        eval_df = pd.read_csv(eval_file)

        # Display uploaded evaluation data
        with st.expander("View Uploaded Evaluation Data", expanded=True):
            st.dataframe(eval_df, use_container_width=True)

        # Validate required columns
        if "Question" not in eval_df.columns or "Answer" not in eval_df.columns:
            st.error("Evaluation CSV must have 'Question' and 'Answer' columns.")
            return

        # Perform evaluation
        accuracy, results_df = evaluate_answers(mcqs_df, eval_df)
        st.success(f"Evaluation completed successfully! Accuracy: {accuracy:.2f}%")

        # Display key metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Questions", len(results_df))
        with col2:
            st.metric("Correct Answers", results_df["Correct"].sum())
        with col3:
            st.metric("Accuracy", f"{accuracy:.2f}%")

        # Allow download of evaluation results
        st.download_button("Download Evaluation Results", data=results_df.to_csv(index=False), file_name="evaluation_results.csv", mime="text/csv")
    except Exception as e:
        st.error(f"An error occurred during evaluation: {e}")

def main():
    """Main application function."""
    st.title("AI Evaluation Simulator")
    initialize_sidebar()

    uploaded_file = st.file_uploader("Upload MCQ CSV", type=["csv"])
    if uploaded_file:
        mcqs_df = process_mcq_file(uploaded_file)
        if mcqs_df is not None:
            eval_file = st.file_uploader("Upload Evaluation CSV", type=["csv"])
            if eval_file:
                display_evaluation_results(mcqs_df, eval_file)

if __name__ == "__main__":
    main()
