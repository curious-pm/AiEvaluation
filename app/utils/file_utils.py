import pandas as pd

def validate_mcq_csv(file):
    required_columns = ["Question", "Option A", "Option B", "Option C", "Option D"]
    df = pd.read_csv(file)
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing column(s): {', '.join(missing_cols)}")
    return df




