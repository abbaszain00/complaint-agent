from graph import app

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

result = app.invoke(initial_state)

print("\n=== FINAL RESULT ===")
print(f"Classification: {result['classification']}")
print(f"Draft Response: {result['draft_response']}")
print(f"Review Passed: {result['review_passed']}")
print(f"Reviewer Feedback: {result['reviewer_feedback']}")
print(f"\nAudit Log:")
for entry in result['audit_log']:
    print(f"  - {entry}")