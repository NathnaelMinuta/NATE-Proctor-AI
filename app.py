# import chainlit as cl

# @cl.on_chat_start
# async def start():
#   response = "Hi I am Nathnael Minuta's Personal Assistant!"
#   await cl.Message(content=response).send()

# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content.lower()  # Convert user input to lowercase
#     immediate_response = "Processing your request..."
#     await cl.Message(content=immediate_response).send()
#     if "hello" in user_input or "hi" in user_input:
#         response = "Hello there! How can I assist you today?"
#     elif "weather" in user_input:
#         response = "Unfortunately, I don't have access to real-time weather information. However, I can provide general information about weather and climate if you're interested."
#     elif "thank you" in user_input or "thanks" in user_input:
#         response = "You're welcome! I'm glad I could help."
#     elif "goodbye" in user_input or "bye" in user_input:
#         response = "Goodbye! Have a great day."
#     # elif "upload" in user_input:
#     #     # Handle file upload
#     #     file = None
#     #     while file is None:
#     #         file = cl.ask_for_file(title="Please upload a text file to analyze", accept=["text/plain"])
#     #     text = file.content.decode("utf-8")
#     #     response = f"Sure, here is your analysis: {text}"
#     else:
#         response = "I'm sorry, I didn't understand your request. Could you please rephrase it or provide more details?"
#     await cl.sleep(2)
#     # Send the response back to the user
#     await cl.Message(content=response).send()

import chainlit as cl


@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="GPT-3.5",
            markdown_description="The underlying LLM model is **GPT-3.5**.",
            icon="https://picsum.photos/200",
        ),
        cl.ChatProfile(
            name="GPT-4",
            markdown_description="The underlying LLM model is **GPT-4**.",
            icon="https://picsum.photos/250",
        ),
    ]

@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"starting chat using the {chat_profile} chat profile"
    ).send()
