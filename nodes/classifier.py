from anthropic import Anthropic
from state import ComplaintState
from dotenv import load_dotenv

load_dotenv()


def classifier_node(state: ComplaintState) -> dict:

    client = Anthropic()
    response = client.messages.create(

        model = "claude-haiku-4-5-20251001",
        max_tokens = 100,
        system = """You are a complaint classifier for a UK bank. 
        Classify the complaint into exactly one of these categories:
        - billing
        - fraud  
        - service_failure
        - account_access
        - other

        Respond with only the category name, nothing else.""",
        messages =  [
            {"role": "user", "content": state["complaint_letter"]}
            ]
        )
    
    audit_log = state["audit_log"]
    audit_log.append(f"classifier_node ran - classification: {response.content[0].text} ")

    return {"classification": response.content[0].text, "audit_log": audit_log }
