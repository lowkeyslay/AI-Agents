from model.openai import GPTClient

def code_explainer(code):
    """
    Explains the given code in simple terms as if explaining to a five-year-old.
    
    :param code: A JSON string representing a dictionary with keys 'code to explain', and 'programming language'.
    :return: The simple explanation of the Python code.
    """
    system_prompt="You are a code explainer, you only explain code in simple words like explaining to a five year old"
    model_instance = GPTClient(
            model="gpt-4o",
            system_prompt=system_prompt,
            temperature=0
        )
    prompt=f"Explain the following code as if explaining to a five-year-old:\n{code} and respond in JSON format"
    response = model_instance.get_response(prompt)
    
    return response
