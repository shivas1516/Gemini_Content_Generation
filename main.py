import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def generation(question):
    answer = model.generate_content(ques)
    return anwers.text

prompt = "write a simple python code"

output = generation(prompt)

print(output)
