from model.openai import GPTClient

def code_generator(instruction):
    """
    Generates Python code based on the given instruction using the GPT-3 model.
    
    :param instruction: A JSON string representing a dictionary with keys 'code to generate', and 'programming language'.
    :return: The formatted code.
    """
    system_prompt="You are a code generator, you only generate code with no explanation."
    model_instance = GPTClient(
            model="gpt-4o",
            system_prompt=system_prompt,
            temperature=0
        )
    prompt = f"Generate a JSON object for the following instruction:\n{instruction}"
    response = model_instance.get_response(prompt)
    return response
