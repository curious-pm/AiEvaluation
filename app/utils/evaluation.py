import pandas as pd

def evaluate_answers(mcq_df, answer_df):
    """
    Evaluate the accuracy of AI answers compared to the correct answers.

    Args:
        mcq_df (pd.DataFrame): DataFrame with AI-generated answers.
        answer_df (pd.DataFrame): DataFrame with correct answers.

    Returns:
        float: Accuracy percentage.
        pd.DataFrame: Results DataFrame with correctness of answers.
    """
    # Merge the two dataframes on the question
    results_df = answer_df.merge(mcq_df[["Question", "AI Answer"]], on="Question", how="left")
    
    # Clean AI Answer to extract the relevant option
    results_df["AI Answer Cleaned"] = results_df["AI Answer"].str.extract(r"(Option [A-D])")
    results_df["AI Answer Option"] = results_df["AI Answer Cleaned"].str.extract(r"Option ([A-D])")
    results_df["Correct Answer Option"] = results_df["Answer"].str.extract(r"Option ([A-D])")
    
    # Compare the options to determine correctness
    results_df["Correct"] = results_df["AI Answer Option"] == results_df["Correct Answer Option"]
    
    # Calculate accuracy
    total_questions = len(results_df)
    correct_answers = results_df["Correct"].sum()
    accuracy = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    return accuracy, results_df
