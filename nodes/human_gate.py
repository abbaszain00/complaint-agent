from state import ComplaintState


def human_gate(state: ComplaintState) -> dict:
    # the human's decision is already in state["human_review"]
    # just log it and return
    audit_log = state["audit_log"]
    audit_log.append(f"human_gate ran - human approved: {state['human_review']}")
    return {"audit_log": audit_log}