from google import genai

client = genai.Client(api_key="AIzaSyCQGs31O9PUl2WcPJ4EV1fmunt3DFKCoQ4")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="what is coding"
)
print(response.text)