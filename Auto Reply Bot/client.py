import google.generativeai as genai

genai.configure(api_key="AIzaSyCDgwcz-kUeNRVqKO8q-3gNjaUICUhtXGk")

# Step 1: Load the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Step 2: Provide content
command = '''[1:50 pm, 29/06/2025] Tridib: dara Ai kisob korche
[1:50 pm, 29/06/2025] Tridib: generate
[1:50 pm, 29/06/2025] Tridib: Ogulo ai koreche re
[1:50 pm, 29/06/2025] Tridib: Ami noy
[1:50 pm, 29/06/2025] Tufan Das: Hm
[1:51 pm, 29/06/2025] Tridib: e Sala jeta chaichi seta dicche na
[7:21 pm, 29/06/2025] Tridib: Project 1 er code patha
[7:30 pm, 29/06/2025] Tufan Das: import speech_recognition as sr'''
command_as_list = [{"role": "user", "parts": [command]}]

custom_prompt = {"role": "user", "parts": [
    "you are a person named ram who speaks bengali as well as english. He is from India and is a coder.You analyze chat history and respond like ram"
]}

all_contents = command_as_list + [custom_prompt]

# Step 3: Generate content
response = model.generate_content(contents=all_contents)

print(response.text)