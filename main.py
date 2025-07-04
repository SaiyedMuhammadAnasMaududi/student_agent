



# SAmple 1
# import os
# import asyncio
# from openai import AsyncOpenAI
# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# import streamlit as st
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# set_tracing_disabled(True)

# model = "deepseek/deepseek-r1-0528-qwen3-8b:free"

# # Async handler that accepts input
# async def main(user_input):
#     client = AsyncOpenAI(
#         api_key=os.getenv("OPEN_ROUTER_API_KEY"),
#         base_url=os.getenv("OPEN_ROUTER_API_BASE"),
#     )

#     agent = Agent(
#         name="student-agent",
#         instructions="You will answer academic questions, provide study tips, or summarize small passages based on the selected mode. Only respond to one request at a time.",
#         model=OpenAIChatCompletionsModel(openai_client=client, model=model),
#     )

#     result = await Runner.run(agent, input=user_input)
#     return result.final_output

# # Initialize answers list in session_state
# if "answers" not in st.session_state:
#     st.session_state.answers = []

# st.title("Student Agent 👨‍🎓🎓🎓")

# # -------- Input and Submit Button inside Form --------
# with st.form("user_input_form", clear_on_submit=True):
#     user_input = st.text_input("Enter your question or request:")
#     submitted = st.form_submit_button("Submit")

# # -------- Process Submission --------
# if submitted and user_input.strip():
#     answer = asyncio.run(main(user_input.strip()))
#     st.session_state.answers.append(answer.strip())

# # -------- Show Previous Answers --------
# for idx, answer in enumerate(st.session_state.answers):
#     st.write(f"**Answer {idx + 1}:** {answer}")

# # -------- Optional: Clear Chat History --------
# if st.button("Clear all answers"):
#     st.session_state.answers = []

# SAmple with model selection

# import os
# import asyncio
# from datetime import datetime
# from openai import AsyncOpenAI
# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# import streamlit as st
# from dotenv import load_dotenv

# # ---- Load Environment ----
# load_dotenv()
# set_tracing_disabled(True)

# # ---- Available LLM Models ----
# AVAILABLE_MODELS = [
#     "google/gemma-3n-e4b-it:free",
#     "deepseek/deepseek-r1-0528-qwen3-8b:free",
#     "meta-llama/llama-3-8b-instruct:free",
#     "mistralai/mistral-7b-instruct:free"
# ]

# # ---- Session State ----
# if "answers" not in st.session_state:
#     st.session_state.answers = []

# if "selected_model" not in st.session_state:
#     st.session_state.selected_model = AVAILABLE_MODELS[0]

# # ---- Agent Async Function ----
# async def main(user_input, selected_model):
#     client = AsyncOpenAI(
#         api_key=os.getenv("OPEN_ROUTER_API_KEY"),
#         base_url=os.getenv("OPEN_ROUTER_API_BASE"),
#     )

#     agent = Agent(
#         name="student-agent",
#         instructions="You will answer academic questions, provide study tips, or summarize small passages based on the selected mode. Only respond to one request at a time.",
#         model=OpenAIChatCompletionsModel(openai_client=client, model=selected_model),
#     )

#     result = await Runner.run(agent, input=user_input)
#     return result.final_output

# # ---- Fixed Header Styling ----
# st.markdown("""
# <style>
# #MainMenu, footer {visibility: hidden;}
# header {visibility: hidden;}

# .sticky-header {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100%;
#     z-index: 1000;
#     background: white;
#     padding: 1rem 0.5rem;
#     border-bottom: 1px solid #ccc;
#     text-align: center;
# }

# .sticky-footer {
#     position: fixed;
#     bottom: 0;
#     left: 0;
#     width: 100%;
#     background: white;
#     padding: 10px 16px;
#     border-top: 1px solid #ccc;
# }
# </style>

# <div class="sticky-header">
#     <h2>🎓 Student Agent</h2>
# </div>
# """, unsafe_allow_html=True)

# # Spacing below fixed header
# st.markdown("<br><br><br>", unsafe_allow_html=True)

# # ---- Sidebar ----
# with st.sidebar:
#     st.markdown("## ⚙️ Settings")
#     st.session_state.selected_model = st.selectbox(
#         "🧠 Select Model:",
#         AVAILABLE_MODELS,
#         index=AVAILABLE_MODELS.index(st.session_state.selected_model)
#     )
#     if st.button("🧹 Reset Chat"):
#         st.session_state.answers = []
#         st.rerun()

# # ---- Scrollable Chat Area ----
# chat_box = """
# <div style='height: 430px; overflow-y: auto; border: 1px solid #ccc; border-radius: 10px; padding: 10px; background-color: #f9f9f9; margin-bottom: 60px;'>
# """

# for qa in st.session_state.answers:
#     if isinstance(qa, dict):
#         chat_box += f"""
#         <div style='background-color:#d1e7dd; padding:10px; border-radius:10px; margin-bottom:8px; width:fit-content; max-width: 90%;'>
#             <b>🧑‍🎓 You:</b> {qa['question']}
#             <div style='font-size:12px; color:gray; margin-top:5px;'>{qa['time']}</div>
#         </div>
#         <div style='background-color:#f8d7da; padding:10px; border-radius:10px; margin-bottom:15px; width:fit-content; max-width: 90%;'>
#             <b>🤖 Student Agent:</b> {qa['answer']}
#             <div style='font-size:12px; color:gray; margin-top:5px;'>{qa['time']}</div>
#         </div>
#         """
#     else:
#         chat_box += "<div style='color:red;'>⚠️ Invalid message format. Please reset chat.</div>"

# chat_box += "</div>"

# st.markdown(chat_box, unsafe_allow_html=True)

# # ---- Sticky Bottom Input ----
# with st.container():
#     st.markdown("<div class='sticky-footer'>", unsafe_allow_html=True)
#     with st.form("input_form", clear_on_submit=True):
#         user_input = st.text_input("💬 Type your question and press Enter:")
#         submitted = st.form_submit_button("🚀 Ask")
#     st.markdown("</div>", unsafe_allow_html=True)

# # ---- On Submit Handling ----
# if submitted and user_input.strip():
#     with st.spinner("Thinking... 💭"):
#         answer = asyncio.run(
#             main(user_input.strip(), st.session_state.selected_model)
#         )
#         timestamp = datetime.now().strftime("%I:%M %p")
#         st.session_state.answers.append({
#             "question": user_input.strip(),
#             "answer": answer.strip(),
#             "time": timestamp
#         })
#         st.rerun()


# Sample 2
import asyncio
import streamlit as st
from openai import AsyncOpenAI
from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel

# Set tracing disabled
set_tracing_disabled(True)

# ✅ Get keys using Streamlit Secrets (works both locally and in cloud if secrets.toml is set)
OPEN_ROUTER_API_KEY = st.secrets.get("OPEN_ROUTER_API_KEY")
OPEN_ROUTER_API_BASE = st.secrets.get("OPEN_ROUTER_API_BASE")

if not OPEN_ROUTER_API_KEY or not OPEN_ROUTER_API_BASE:
    st.error("❌ API credentials are missing. Please check your `.streamlit/secrets.toml` or Streamlit Cloud secrets.")
    st.stop()

model = "mistralai/mistral-small-3.2-24b-instruct:free"
st.set_page_config(page_title="🎓 Scholar Assistant", layout="wide")

# Session init
st.session_state.setdefault("answers", [])
st.session_state.setdefault("questions", [])
st.session_state.setdefault("user_name", "")

# Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');
    html, body, .stApp {
        font-family: 'Merriweather', serif;
        background-color: #f6f3e9;
        color: #333;
    }
    .chat-container {
        max-width: 800px;
        margin: auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .message-bubble {
        background-color: #e9f5db;
        padding: 16px;
        border-radius: 10px;
        margin: 12px 0;
        border-left: 4px solid #99bc85;
    }
    .response-bubble {
        background-color: #f5eee6;
        padding: 16px;
        border-radius: 10px;
        margin: 12px 0;
        border-left: 4px solid #cfb997;
    }
    input, .stTextInput input {
        background-color: #fff;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("#### 🧭 Options")
    mode = st.selectbox("Agent Mode", [
        "Answer academic questions",
        "Provide study tips",
        "Summarize small text passages"
    ])
    if st.button("🗑️ Clear Conversation"):
        st.session_state.answers.clear()
        st.session_state.questions.clear()
        st.session_state.user_name = ""
        st.rerun()

# Header
st.markdown("""
<div class='chat-container'>
<h1>🎓 Scholar Assistant</h1>
<p style='margin-top:-10px; font-size:16px;'>An intelligent companion for your academic journey</p>
""", unsafe_allow_html=True)

# Ask for name
if not st.session_state.user_name:
    name = st.text_input("What's your name?")
    if name.strip():
        st.session_state.user_name = name.strip()
        st.rerun()
    st.stop()

# Instruction map
instruction_map = {
    "Answer academic questions": "You are an academic tutor. Answer precisely and clearly.",
    "Provide study tips": "You are a study coach. Provide helpful, practical advice.",
    "Summarize small text passages": "You are a summarizer. Rewrite input clearly and concisely."
}
instruction = instruction_map.get(mode, "")

# Async agent function
async def ask_agent(prompt, instructions, user_name):
    client = AsyncOpenAI(api_key=OPEN_ROUTER_API_KEY, base_url=OPEN_ROUTER_API_BASE)
    agent = Agent(
        name="student-agent",
        instructions=f"{instructions} Always refer to the user as {user_name}.",
        model=OpenAIChatCompletionsModel(openai_client=client, model=model)
    )
    result = await Runner.run(agent, input=prompt)
    return result.final_output

# Input
user_input = st.chat_input(f"What would you like to ask, {st.session_state.user_name}?")
if user_input and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            answer = asyncio.run(ask_agent(user_input.strip(), instruction, st.session_state.user_name))
            st.session_state.questions.append(user_input.strip())
            st.session_state.answers.append(answer.strip())
        except Exception as e:
            st.error(f"⚠️ Error from agent:\n\n`{e}`")

# Chat display
for q, a in zip(st.session_state.questions, st.session_state.answers):
    st.markdown(f"<div class='message-bubble'><strong>{st.session_state.user_name}:</strong> {q}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='response-bubble'><strong>Assistant:</strong> {a}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     asyncio.run(main(user_input.strip(),st.session_state.selected_model))




#SAmple 3
# import os
# import asyncio
# from openai import AsyncOpenAI
# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# import streamlit as st
# from dotenv import load_dotenv

# # -------------------- Configuration --------------------
# load_dotenv()
# set_tracing_disabled(True)

# MODEL_NAME = "deepseek/deepseek-r1-0528-qwen3-8b:free"
# APP_TITLE = "Student Agent"
# APP_ICON = "🎓"
# INSTRUCTIONS = (
#     "You will answer academic questions, provide study tips, or summarize small passages "
#     "based on the selected mode. Only respond to one request at a time."
# )

# # -------------------- OpenRouter Async Function --------------------
# async def generate_response(prompt: str) -> str:
#     client = AsyncOpenAI(
#         api_key=os.getenv("OPEN_ROUTER_API_KEY"),
#         base_url=os.getenv("OPEN_ROUTER_API_BASE")
#     )

#     agent = Agent(
#         name="student-agent",
#         instructions=INSTRUCTIONS,
#         model=OpenAIChatCompletionsModel(openai_client=client, model=MODEL_NAME)
#     )

#     result = await Runner.run(agent, input=prompt)
#     return result.final_output.strip()


# # -------------------- Streamlit Page Setup --------------------
# st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="centered")

# # Apply custom styling
# st.markdown("""
# <style>
#     body { font-family: 'Segoe UI', sans-serif; }
#     .chat-bubble {
#         border-radius: 12px;
#         padding: 1rem;
#         margin: 0.5rem 0;
#         font-size: 1rem;
#         line-height: 1.5;
#     }
#     .user-msg {
#         background-color: #eaf6ff;
#         color: #000;
#     }
#     .agent-msg {
#         background-color: #f0f2f6;
#         color: #111;
#     }
#     .stButton button {
#         background-color: #ff4b4b;
#         color: #fff;
#         border-radius: 8px;
#         padding: 0.5rem 1rem;
#         font-weight: bold;
#     }
# </style>
# """, unsafe_allow_html=True)

# st.title(f"{APP_ICON} {APP_TITLE}")
# st.caption("Your personal academic assistant powered by OpenRouter + DeepSeek")

# # -------------------- Session State --------------------
# if "history" not in st.session_state:
#     st.session_state.history = []  # List of (user_input, agent_response) tuples

# # -------------------- Chat Input & Response --------------------
# user_input = st.chat_input("Ask your academic question...")

# if user_input and user_input.strip():
#     with st.spinner("Thinking..."):
#         try:
#             response = asyncio.run(generate_response(user_input.strip()))
#             st.session_state.history.append((user_input.strip(), response))
#         except Exception as e:
#             st.error(f"❌ Failed to get response: {str(e)}")

# # -------------------- Display Chat --------------------
# for user_msg, agent_msg in st.session_state.history:
#     st.markdown(f"<div class='chat-bubble user-msg'><strong>You:</strong> {user_msg}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='chat-bubble agent-msg'><strong>Student Agent:</strong> {agent_msg}</div>", unsafe_allow_html=True)

# # -------------------- Clear History Button --------------------
# st.divider()
# if st.button("🗑️ Clear Conversation"):
#     st.session_state.history = []
#     st.success("Chat history cleared.")


