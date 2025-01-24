import pandas as pd

def evaluate_answers(mcq_df, answer_df):
    """
    Evaluate the accuracy of AI-generated answers compared to the correct answers.

    Args:
        mcq_df (pd.DataFrame): DataFrame containing AI-generated answers.
        answer_df (pd.DataFrame): DataFrame containing correct answers.

    Returns:
        float: Accuracy percentage.
        pd.DataFrame: Results DataFrame with correctness of answers.
    """
    # Merge AI answers with correct answers based on the 'Question' column
    results_df = answer_df.merge(mcq_df[["Question", "AI Answer"]], on="Question", how="left")
    
    # Extract AI-selected option (A-D) from the AI-generated answer text
    results_df["AI Answer Cleaned"] = results_df["AI Answer"].str.extract(r"(Option [A-D])")
    results_df["AI Answer Option"] = results_df["AI Answer Cleaned"].str.extract(r"Option ([A-D])")
    
    # Extract correct option (A-D) from the provided answer data
    results_df["Correct Answer Option"] = results_df["Answer"].str.extract(r"Option ([A-D])")
    
    # Compare AI-selected option with the correct option to determine correctness
    results_df["Correct"] = results_df["AI Answer Option"] == results_df["Correct Answer Option"]
    
    # Calculate accuracy as the percentage of correct answers
    total_questions = len(results_df)
    correct_answers = results_df["Correct"].sum()
    accuracy = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    return accuracy, results_df
