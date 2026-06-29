from anthropic import Anthropic
from state import ComplaintState
from dotenv import load_dotenv

load_dotenv()

def reviewer_node(state: ComplaintState) -> dict:

    client = Anthropic()
    message = f"Draft response:\n{state['draft_response']}\n\nPolicy:\n{state['policy_chunks']}\n\nCustomer claims:\n{state['extracted_claims']}"
    response = client.messages.create(

        model = "claude-sonnet-4-5",
        max_tokens = 500,
        system = """You are a reviewer for a UK bank.
        Check the drafted response based on:
        1. Correctness - does it match the policy?
        2. Format - is it professional?
        3. Completeness - does it address all claims?

        You MUST respond in exactly this format with no other text before or after:
        RESULT: pass
        FEEDBACK: your feedback here

        Or:
        RESULT: fail
        FEEDBACK: your feedback here

        The first line MUST start with RESULT: and the second line MUST start with FEEDBACK:""",
        messages = [
            {"role": "user", "content": message}
        ]
    )

    lines = response.content[0].text.strip().split("\n")
    result_lines = [l for l in lines if l.startswith("RESULT:")]
    feedback_lines = [l for l in lines if l.startswith("FEEDBACK:")]

    if not result_lines or not feedback_lines:
        # fallback if parsing fails
        return {"review_passed": False, "reviewer_feedback": response.content[0].text, "audit_log": audit_log}

    result_line = result_lines[0]
    feedback_line = feedback_lines[0]

    review_passed = "pass" in result_line.lower()
    reviewer_feedback = feedback_line.replace("FEEDBACK:", "").strip()

    audit_log = state["audit_log"]
    audit_log.append(f"reviewer_node ran - review results: {response.content[0].text} ")

    return {
    "review_passed": review_passed,
    "reviewer_feedback": reviewer_feedback,
    "audit_log": audit_log
}