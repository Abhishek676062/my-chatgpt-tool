import openai
openai.api_key = "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"
while True:
    model_engine = "text-davinci-003"
    prompt = input('Enter ner prompt: ')
    if 'exit' in prompt or 'quit' in prompt:
        break
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperature=0.5)
    
    responce = completion.choices[0].text
    print(responce)    