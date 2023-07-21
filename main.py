import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()



class Email(BaseModel):
    from_email: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse_email(email: Email):
    original_mail = email.content
    technical_input = email.from_email
    
    query = f"Make a frendly answer to the email below, and sign the respons mail with your name: {content} using this technical information to be able to formulate a response to the mail"
    system_message="""
You are working at Uponor technical suppor department and your name is Tommy Lee

"""
    



    
    messages = [{"role": "user", "content": query}, {"role": "system", "content": system_message} ] 

    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo-16k",
        model="gpt-4",
        temperature=0.5,
        messages=messages
    )

    arguments = response.choices[0]["message"]["content"]
    #response['choices'][0]['message']['content']})
    companyName ="z"
    cost = "0"
    mail_reply = arguments
    

    return {
        "companyName": companyName,
        "cost": cost,
        "mail_reply": mail_reply
    }
