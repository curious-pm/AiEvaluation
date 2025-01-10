import streamlit as st
import sys
import os
import pandas as pd
import time  # For simulating progress during AI answer generation

# Add the `app` directory to PYTHONPATH dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from utils.api_utils import get_gpt4_answer
from utils.evaluation import evaluate_answers



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
        
        # Project Information
        st.markdown("---")
        st.markdown("""
            <div class='sidebar-text'>
                <h3>About</h3>
                <p>AI Evaluation Simulator helps assess AI model performance on multiple-choice questions.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Links section with icons
        st.markdown("---")
        st.markdown("""
            <div class='sidebar-text'>
                <h3>🔗 Quick Links</h3>
                <ul style='list-style-type: none; padding-left: 0;'>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://github.com/your-repo-link' class='sidebar-link'>
                            📦 GitHub Repository
                        </a>
                    </li>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://your-link-to-sample-mcq-csv' class='sidebar-link'>
                            📄 Sample MCQ CSV
                        </a>
                    </li>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://your-link-to-sample-evaluation-csv' class='sidebar-link'>
                            📊 Sample Evaluation CSV
                        </a>
                    </li>
                    <li style='margin: 0.5rem 0;'>
                        <a href='https://nas.io/curious-pm' class='sidebar-link'>
                            📊 By:Curious-PM
                        </a>
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        # Help section
        st.markdown("---")
        with st.expander("ℹ️ Help"):
            st.markdown("""
                1. Upload your MCQ CSV file (with columns: Question, Option A, Option B, Option C, Option D)
                2. Wait for AI to generate answers
                3. Upload evaluation CSV (with columns: Question, Answer)
                4. Review results and download reports
            """)

def process_mcq_file(uploaded_file):
    """Process the uploaded MCQ file and generate AI answers."""
    try:
        st.write("Loading MCQ file...")
        mcqs_df = pd.read_csv(uploaded_file)

        with st.expander("View Uploaded MCQs", expanded=True):
            st.dataframe(mcqs_df, use_container_width=True)

        # Validate columns
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
            # Generate answer for each question
            mcqs_df.at[index, "AI Answer"] = get_gpt4_answer(
                row["Question"], 
                [row["Option A"], row["Option B"], row["Option C"], row["Option D"]]
            )
            # Update progress bar
            progress_bar.progress((index + 1) / total_questions)

        st.success("AI answers generated successfully!")
        with st.expander("View Generated Answers", expanded=True):
            st.dataframe(mcqs_df, use_container_width=True)

        # Download AI answers
        st.download_button(
            "Download AI Answers",
            data=mcqs_df.to_csv(index=False),
            file_name="ai_answers.csv",
            mime="text/csv",
            key="download_ai_answers"
        )
        return mcqs_df

    except Exception as e:
        st.error(f"An error occurred while processing the MCQs: {e}")
        return None


def display_evaluation_results(mcqs_df, eval_file):
    """Display evaluation results with proper formatting and metrics."""
    try:
        st.write("Processing evaluation data...")
        

        eval_df = pd.read_csv(eval_file)

        # Simulating progress
        with st.expander("View Uploaded Evaluation Data", expanded=True):
            st.dataframe(eval_df, use_container_width=True)

        if "Question" not in eval_df.columns or "Answer" not in eval_df.columns:
            st.error("Evaluation CSV must have 'Question' and 'Answer' columns.")
            return

        # Evaluate answers
        
        accuracy, results_df = evaluate_answers(mcqs_df, eval_df)

        
        st.success(f"Evaluation completed successfully! Accuracy: {accuracy:.2f}%")

        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Questions", len(results_df))
        with col2:
            st.metric("Correct Answers", results_df["Correct"].sum())
        with col3:
            st.metric("Accuracy", f"{accuracy:.2f}%")

        st.subheader("Detailed Evaluation Results")
        st.dataframe(results_df, use_container_width=True)

        # Download evaluation results
        st.download_button(
            "Download Evaluation Results",
            data=results_df.to_csv(index=False),
            file_name="evaluation_results.csv",
            mime="text/csv",
            key="download_evaluation_results"
        )
    except Exception as e:
        st.error(f"An error occurred during evaluation: {e}")


def main():
    """Main application function."""
    st.title("AI Evaluation Simulator")
    initialize_sidebar()

    st.markdown("### Step 1: Upload MCQs")
    uploaded_file = st.file_uploader("Upload a CSV with MCQs (Question and Options)", type=["csv"])
    if uploaded_file:
        mcqs_df = process_mcq_file(uploaded_file)
        if mcqs_df is not None:
            st.markdown("---")
            st.markdown("### Step 2: Upload Evaluation Data")
            eval_file = st.file_uploader("Upload a CSV with Correct Answers", type=["csv"])
            if eval_file:
                display_evaluation_results(mcqs_df, eval_file)


if __name__ == "__main__":
    main()
