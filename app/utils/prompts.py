def construct_prompt(question, options):
    """
    Construct a formatted prompt for answering a multiple-choice question.

    Args:
        question (str): The MCQ question to be answered.
        options (list): A list of answer choices (e.g., ['Option A', 'Option B', ...]).

    Returns:
        str: A formatted prompt string for AI processing.
    """
    # Start the prompt with a descriptive instruction
    prompt = (
        """You are tasked with answering a multiple-choice question as accurately as possible. "
        "Analyze the question and select the best answer.\n\n"""
    )
    
    # Add the question to the prompt
    prompt += f"Question:\n{question}\n"
    
    # Append each answer option to the prompt in alphabetical order
    for i, option in enumerate(options, start=1):
        prompt += f"Option {chr(64 + i)}: {option}\n"
    
    # Conclude the prompt with instructions to return the correct answer format
    prompt += "Please return the correct option (e.g., Option A, Option B)."
    
    return prompt
