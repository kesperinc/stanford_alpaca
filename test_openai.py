import openai
mykey = "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"


# OpenAI API 키를 설정합니다. (실제 API 키로 교체해주세요)
openai.api_key = mykey

# GPT-4 모델을 사용하여 텍스트를 생성하는 예제입니다.


def generate_text(prompt, model="text-davinci-002", n=1, max_tokens=150, temperature=0.7):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=n,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()


prompt = "Translate the following English text to Korean: 'The weather is beautiful today.'"
result = generate_text(prompt)
print(result)

prompt = "Translate all following questions in Korean and answer in Korea please. 'What is the capital of South Korea?'"
result = generate_text(prompt)
print(result)

prompt = "Summarize the following text: 'Python is a high-level, interpreted, and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.'"
result = generate_text(prompt)
print(result)

prompt = "Write a Python function to calculate the factorial of a number."
result = generate_text(prompt)
print(result)

prompt = "Write the beginning of a science fiction story that starts with the sentence 'It was a dark and stormy night on planet Zog.'"
result = generate_text(prompt)
print(result)
