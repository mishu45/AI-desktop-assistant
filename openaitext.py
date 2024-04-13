import os
import openai
from config import apikey

openai.api_key = os.getenv("ENTER API KEY HERE")


response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = "",
    temperature = 0.7,
    max_token = 256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty =0


)
