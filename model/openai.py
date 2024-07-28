import os
import requests
import json
class GPTClient:
    def __init__(self, model, system_prompt, temperature):
        """
        Initializes the GPT-4 client with the given API key.
        """
        api_key = os.getenv('OPENAI_API_KEY')
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.api_key = api_key
        self.model_endpoint = 'https://api.openai.com/v1/chat/completions'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_response(self, prompt):
        """
        Gets a response from the GPT model for the given prompt.
        
        :param prompt: The prompt to send to the GPT-3 model.
        :return: The text response from the model.
        """
        payload = {
                    "model": self.model,
                    "response_format": {"type": "json_object"},
                    "messages": [
                        {
                            "role": "system",
                            "content": self.system_prompt
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False,
                    "temperature": self.temperature,
                }
        
        response_dict = requests.post(self.model_endpoint, headers=self.headers, data=json.dumps(payload))
        response_json = response_dict.json()
        response = json.loads(response_json['choices'][0]['message']['content'])
        print(F"\n\nResponse from OpenAI model: {response}")
        return response