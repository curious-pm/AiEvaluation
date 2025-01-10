def construct_prompt(question, options):
    prompt = f"""You are tasked with answering a multiple-choice question as accurately as possible. Analyze the question and select the best answer.\n\n"""
    prompt += f"Question:\n{question}\n"
    for i, option in enumerate(options, start=1):
        
        prompt += f"Option {chr(64 + i)}: {option}\n"
    prompt += "Please return the correct option (e.g., Option A, Option B)."
    return prompt




