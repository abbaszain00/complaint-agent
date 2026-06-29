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
        Check the drafted response, and review it based on correctness (according to the policy documents), format (is it written in a professional manner), and completeness (does it answer every complaint fully) .
        Return a result, saying either 'pass' or 'fail' with ONLY these options, and feedback in the following format as an EXAMPLE:
        
        RESULT: pass
        FEEDBACK: The letter accurately addresses both claims....""",
        messages = [
            {"role": "user", "content": message}
        ]
    )

    lines = response.content[0].text.strip().split("\n")
    result_line = [l for l in lines if l.startswith("RESULT:")][0]
    feedback_line = [l for l in lines if l.startswith("FEEDBACK:")][0]

    review_passed = "pass" in result_line.lower()
    reviewer_feedback = feedback_line.replace("FEEDBACK:", "").strip()

    audit_log = state["audit_log"]
    audit_log.append(f"reviewer_node ran - review results: {response.content[0].text} ")

    return {
    "review_passed": review_passed,
    "reviewer_feedback": reviewer_feedback,
    "audit_log": audit_log
}