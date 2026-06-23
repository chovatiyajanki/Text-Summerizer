import google.generativeai as genai

genai.configure(api_key="AIzaSyDx3nDGRQ7Srn6VYyOLsF18qPB9rjwAkig")

for m in genai.list_models():
    print(m.name, "->", m.supported_generation_methods)