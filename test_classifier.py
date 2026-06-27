from nodes.extractor import extractor_node


test_state = {
    "complaint_letter": "I have been charged twice for the same transaction on the 15th June. I want a refund immediately",
    "classification": None,
    "extracted_claims": None,
    "draft_response": None,
    "reviewer_feedback": None,
    "bank_policy": None,
    "audit_log": [],
    "human_review": None
}

result = extractor_node(test_state)
print(result)