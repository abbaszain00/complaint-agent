from anthropic import Anthropic
from state import ComplaintState
from dotenv import load_dotenv

load_dotenv()

def extractor_node(state: ComplaintState) -> dict:

    client = Anthropic()
    response = client.messages.create(

        model = "claude-haiku-4-5-20251001",
        max_tokens = 500,
        system = """You are an claim extractor for a UK bank.
        Extract the specific claims made by the customer in the complaint letter.
        Return each claim on a new line, nothing else. No numbering, no bullets, no explanation.""",
        messages = [
            {"role": "user", "content": state["complaint_letter"]}
        ]
    )

    claims = response.content[0].text.strip().split("\n")
    audit_log = state["audit_log"]
    audit_log.append(f"extractor_node ran - extracted claims: {claims} ")

    return {"extracted_claims": claims, "audit_log": audit_log}