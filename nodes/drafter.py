from anthropic import Anthropic
from state import ComplaintState
from dotenv import load_dotenv

load_dotenv()

def drafter_node(state: ComplaintState) -> dict:

    client = Anthropic()

    claims = "\n".join(state["extracted_claims"])
    policy = "\n".join(state["policy_chunks"])

    message = f"Customer claims:\n{claims}\n\nRelevant policy:\n{policy}"

    response = client.messages.create(
        model = "claude-sonnet-4-5",
        max_tokens = 1000,
        system = "You are a professional drafter. Draft A professional, compliant response based on the customer's claims and the bank's policy. Make it in a formal letter format.",
        messages=[{"role": "user", "content": message}]
    )

    audit_log = state["audit_log"]
    audit_log.append(f"drafter_node ran - draft response: {response.content[0].text}")

    return {"draft_response": response.content[0].text, "audit_log": audit_log}