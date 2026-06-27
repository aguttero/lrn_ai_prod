# Genai init stream mode
## sample code for open AI
```python
from fastapi import FastAPI  # type: ignore
from fastapi.responses import StreamingResponse  # type: ignore
from openai import OpenAI  # type: ignore

app = FastAPI()

@app.get("/api")
def idea():
    client = OpenAI()
    prompt = [{"role": "user", "content": "Come up with a new business idea for AI Agents"}]
    stream = client.chat.completions.create(model="gpt-5-nano", messages=prompt, stream=True)

    def event_stream():
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                lines = text.split("\n")
                for line in lines:
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
```


## gemini simple chat (untested)
```python
import os
from google import genai

def stream_chat():
    # 1. Initialize the client (automatically uses GEMINI_API_KEY)
    client = genai.Client()

    # 2. Start the chat session
    chat = client.chats.create(model="gemini-2.5-flash")

    # 3. Send message using the stream method
    user_message = "Write a short poem about debugging at 2 AM."
    response_stream = chat.send_message_stream(user_message)

    # 4. Iterate over chunks as they arrive
    print("Gemini: ", end="", flush=True)
    for chunk in response_stream:
        print(chunk.text, end="", flush=True)
    print() # New line after stream finishes

# Execute the function
stream_chat()
```

## gemini search for genai stream
```python
import os
from google import genai

def stream_chat():
    # 1. Initialize the client (automatically uses GEMINI_API_KEY)
    client = genai.Client()

    # 2. Start the chat session
    chat = client.chats.create(model="gemini-2.5-flash")

    # 3. Send message using the stream method
    user_message = "Write a short poem about debugging at 2 AM."
    response_stream = chat.send_message_stream(user_message)

    # 4. Iterate over chunks as they arrive
    print("Gemini: ", end="", flush=True)
    for chunk in response_stream:
        print(chunk.text, end="", flush=True)
    print() # New line after stream finishes

# Execute the function
stream_chat()
```

### Key Differences to Note

* send_message_stream: This method returns an iterable stream object immediately.
* chunk.text: Inside the for loop, each chunk contains a piece of the generated text.
* end="", flush=True: Standard Python print statements include a newline by default. Setting end="" and flush=True forces the terminal to display the text instantly piece-by-piece.
* History Preservation: Even when streaming, the chat object automatically saves the history of the conversation for subsequent turns.
