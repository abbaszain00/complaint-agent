from nodes.reviewer import reviewer_node

test_state = {
    "complaint_letter": "I have been charged twice for the same transaction on 15th June. I want a refund immediately.",
    "classification": "billing",
    "extracted_claims": ["Charged twice for the same transaction on 15th June", "Requests immediate refund"],
    "draft_response": "Dear Customer, Thank you for contacting Lloyds Bank. We have received your complaint regarding a duplicate charge on 15th June. We will investigate within 5 working days and process a refund if confirmed. Yours sincerely, Customer Relations.",
    "reviewer_feedback": None,
    "policy_chunks": ["Billing Policy: In the event of a duplicate or incorrect charge, Lloyds Bank will investigate within 5 working days and process a full refund within 3-5 working days."],
    "audit_log": [],
    "human_review": None,
    "review_passed": None
}

result = reviewer_node(test_state)
print(result)