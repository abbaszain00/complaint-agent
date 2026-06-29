from graph import app

config = {"configurable": {"thread_id": "complaint_001"}}

initial_state = {
    "complaint_letter": "I have been charged twice for the same transaction on 15th June. I want a refund immediately.",
    "classification": None,
    "extracted_claims": None,
    "draft_response": None,
    "reviewer_feedback": None,
    "policy_chunks": None,
    "audit_log": [],
    "human_review": None,
    "review_passed": None
}

# first run - pauses at human_gate
print("=== RUNNING PIPELINE ===")
result = app.invoke(initial_state, config)
print(f"\nPaused for human review.")
print(f"Draft response:\n{result['draft_response']}")

# simulate human approving
print("\n=== HUMAN APPROVING ===")
app.update_state(config, {"human_review": True})
result = app.invoke(None, config)

print("\n=== FINAL RESULT ===")
print(f"Draft Response:\n{result['draft_response']}")
print(f"\nAudit Log:")
for entry in result['audit_log']:
    print(f"  - {entry}")