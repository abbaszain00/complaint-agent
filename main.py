from fastapi import FastAPI
from graph import app as graph_app
import uuid

api = FastAPI()




@api.post("/complaint")
def process_complaint(complaint_letter: str):
    initial_state = {
    "complaint_letter": complaint_letter,
    "classification": None,
    "extracted_claims": None,
    "draft_response": None,
    "reviewer_feedback": None,
    "policy_chunks": None,
    "audit_log": [],
    "human_review": None,
    "review_passed": None
    }
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    result = graph_app.invoke(initial_state, config)
    return {
        "thread_id": config["configurable"]["thread_id"],
        "draft_response": result["draft_response"]
    }

@api.post("/approve")
def approve_complaint(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    graph_app.update_state(config, {"human_review": True})
    result = graph_app.invoke(None, config)
    return {
        "status": "approved",
        "final_response": result["draft_response"]
    }
@api.post("/reject")
def reject_complaint(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    graph_app.update_state(config, {"human_review": False})
    result = graph_app.invoke(None, config)
    return {
        "status": "rejected",
        "final_response": result["draft_response"]
    }
