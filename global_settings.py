import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
PAGE_TITLE_ICON = "🦙💬"
USER_ICON = "🧑‍💻"
ROBOT_ICON = "🤖"
