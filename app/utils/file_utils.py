import pandas as pd

def validate_mcq_csv(file):
    """
    Validate the structure of an uploaded MCQ CSV file.

    Args:
        file (str or file-like object): Path to the CSV file or uploaded file object.

    Returns:
        pd.DataFrame: DataFrame containing the validated data.

    Raises:
        ValueError: If required columns are missing from the CSV file.
    """
    # Define the required columns for MCQ file validation
    required_columns = ["Question", "Option A", "Option B", "Option C", "Option D"]
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Identify any missing columns from the required list
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    # Raise an error if any required columns are missing
    if missing_cols:
        raise ValueError(f"Missing column(s): {', '.join(missing_cols)}")
    
    return df