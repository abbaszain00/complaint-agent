from nodes.retriever import retriever_node

test_state = {
    "complaint_letter": "I have been charged twice for the same transaction on 15th June. I want a refund immediately.",
    "classification": "billing",
    "extracted_claims": ["Charged twice for the same transaction on 15th June", "Requests immediate refund"],
    "draft_response": None,
    "reviewer_feedback": None,
    "policy_chunks": None,
    "audit_log": [],
    "human_review": None
}

result = retriever_node(test_state)
print(result)