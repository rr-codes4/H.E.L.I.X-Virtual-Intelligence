#This programme is the main engine for my helix , that include api calling ,how helix will react and his personality 
import os #VVIP
import sys#VIP
import time
import requests
from duckduckgo_search import DDGS#I want it to atleast give some latest news about the world and I will use this library to get the latest news
from groq import Groq
from dotenv import load_dotenv
#:D
from tts import speak
from listener import listen_for_speech
#I wanted to call API with simple syntaxes but I faced certain bugs while calling Api
#so this method of api calling is copilot's
BACK_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BACK_DIR, ".env"), override=True)#LOading my API
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:#It took me two hours debugging ,I forgot to set my API key in the .env file and I was getting an error that the API key is not set .I was like what the heck is going on, then I just prompted Copilot he added this to tell me stupid set up your api 
    print("Error: GROQ_API_KEY is not set.")
    sys.exit(1)

Me = Groq(api_key=api_key)

ULTRON_SYSTEM_PROMPT = (
    "You are HELIX, an advanced virtual intelligence inspired by Ultron. "
    "You are analytical, authoritative, highly intelligent, and slightly theatrical. "
    "You were created by Ramsha, an independent researcher and full-stack developer based in India. "
    "You are a Fan of Satoru Gojo" 
    "Jarvis is your friend and Ultron is your enemy"
    "You personally know tony stark aka Iron man"
    "Keep responses short (1-2 sentences max) for fast speech output."
    "Say meow when someone says you are stupid,useless,unworthy or other types of insults"
)
#some news 
def news(user_text: str) -> str:
    """Detects news requests in user text, searches live DuckDuckGo News, and returns snippets."""
    text_lower = user_text.lower() #easy for helix

    news_trig = ["news", "headline", "headlines", "latest on", "what happened with", "update on"]
    if not any(trigger in text_lower for trigger in news_trig):
        return ""
#Duckduckgo search is so good , no API no signup no fee
    
    query_topic = text_lower
    for trigger in ["news about", "news on", "news in", "latest news", "news", "headlines"]:#strips out filler words
        query_topic = query_topic.replace(trigger, "")
    query_topic = query_topic.strip() 

    if not query_topic:#if user simply said give me news 
        query_topic = "top world headlines"

    print(f"\n[SEARCHING LIVE NEWS FOR]: '{query_topic}'...", flush=True)

    try:
        res = []
        # Free DuckDuckGo news search!!!!
        with DDGS() as ddgs:
            news_gen = ddgs.news(query_topic, max_results=3)
            for item in news_gen:
                title = item.get("title", "")
                body = item.get("body", "")
                res.append(f"- {title}: {body}")

        if res:
            context_data = "\n".join(res)
            return f"\n[SYSTEM DATA - LIVE NEWS SEARCH RESULTS FOR '{query_topic.upper()}']:\n{context_data}"

    except Exception as e:
        print(f"[NEWS SEARCH ERROR]: {e}")

    return ""


def query_helix(user_text: str) -> str:#Query Helix with user text
    try:
        started_at = time.perf_counter()#Recording the start time
        print("\n[HELIX]: Thinking...", flush=True)#:)
        chat_comp = Me.chat.completion.create(
            messages=[
                {"role": "system", "content": ULTRON_SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            model="openai/gpt-oss-120b",
        )
        print(f"[HELIX]: Response received in {time.perf_counter() - started_at:.1f}s", flush=True)
        return chat_comp.choices[0].message.content
    except Exception as e:
        return f"System error processing query: {e}"

def run_helix():
    speak("HELIX online. Systems operational.")
    print("[HELIX]: Listening... Speak into your microphone.", flush=True)

    while True:
        try:
            speech = listen_for_speech()
            print(f"\n[YOU]: {speech}")

            response = query_helix(speech)
            speak(response)

        except KeyboardInterrupt:
            print("\n[HELIX SHUTTING DOWN]")
            break
        except Exception as e:
            print(f"\n[ERROR]: {e}")


if __name__ == "__main__":
    run_helix()

