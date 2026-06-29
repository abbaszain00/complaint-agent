from state import ComplaintState

def finaliser_node(state: ComplaintState) -> dict:
    
    audit_log = state["audit_log"]
    audit_log.append(f"finaliser ran - added final audit log entry")
    return {"draft_response": state["draft_response"], "audit_log": audit_log}