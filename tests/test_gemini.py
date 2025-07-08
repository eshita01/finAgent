import os
import sys
from unittest.mock import patch
import types

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class DummyChunk:
    def __init__(self, text):
        self.text = text


class DummyModel:
    def generate_content(self, prompt, **kwargs):
        if kwargs.get("stream"):
            return [DummyChunk("Hello "), DummyChunk("world")]
        response = types.SimpleNamespace(text="Hello world")
        return response


# Provide a dummy google.generativeai module for import during tests
class _DummyGenAI:
    def configure(self, **kwargs):
        pass

    class GenerativeModel:
        def __init__(self, *args, **kwargs):
            self.instance = DummyModel()

        def generate_content(self, *args, **kwargs):
            return self.instance.generate_content(*args, **kwargs)

sys.modules.setdefault("google", types.ModuleType("google"))
sys.modules["google"].generativeai = _DummyGenAI()
sys.modules.setdefault("google.generativeai", sys.modules["google"].generativeai)
sys.modules.setdefault("dotenv", types.ModuleType("dotenv"))
sys.modules["dotenv"].load_dotenv = lambda *a, **kw: None
import pytest

from agents.llm_wrappers.gemini import GeminiLLM

def make_llm():
    with patch("google.generativeai.configure"), \
         patch("google.generativeai.GenerativeModel", return_value=DummyModel()), \
         patch("config.env_loader.load_env", return_value={"GOOGLE_API_KEY": "dummy"}), \
         patch("agents.llm_wrappers.gemini.load_env", return_value={"GOOGLE_API_KEY": "dummy"}):
        return GeminiLLM()

def test_generate_stream():
    llm = make_llm()
    assert llm.generate("test", stream=True) == "Hello world"


def test_generate_non_stream():
    llm = make_llm()
    assert llm.generate("test") == "Hello world"


