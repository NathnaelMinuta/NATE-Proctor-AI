import google.generativeai as genai
import chainlit as cl
from typing import Optional

# Set up the Google Bard API
genai.configure(api_key='AIzaSyBzegTPc4jhh7lbNVhlI-AXBplVT7huA0o')
model = genai.GenerativeModel('gemini-pro')

@cl.set_chat_profiles
async def chat_profile(current_user: cl.User):
    if current_user.metadata["role"] != "ADMIN":
        return None
    return [
        cl.ChatProfile(
            name="NATE-1.0",
            markdown_description="The underlying LLM model is **NATE-1.0**.",
            icon="https://picsum.photos/200",
        ),
        cl.ChatProfile(
            name="NATE-2.0",
            markdown_description="The underlying LLM model is **NATE-2.0**.",
            icon="https://picsum.photos/250",
        ),
    ]

@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.User]:
    if (username, password) == ("admin", "admin"):
        return cl.User(identifier="admin", metadata={"role": "ADMIN"})
    else:
        return None

@cl.on_chat_start
async def on_chat_start():
    user = cl.user_session.get("user")
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"Hi, I'm Nathnael Minuta's Personal Assistant powered by Google Bard! I have now started a chat with {user.identifier} using the {chat_profile} chat profile. How can I assist you today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content

    immediate_response = "Processing your request..."
    await cl.Message(content=immediate_response).send()

    try:
        # Generate a response using Google Bard
        response = model.generate_content(user_input)
        
        await cl.sleep(2)
        await cl.Message(content=response.text).send()
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await cl.Message(content=error_message).send()