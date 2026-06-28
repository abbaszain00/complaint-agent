from nodes.drafter import drafter_node

test_state = {
    "complaint_letter": "I have been charged twice for the same transaction on 15th June. I want a refund immediately.",
    "classification": "billing",
    "extracted_claims": ["Charged twice for the same transaction on 15th June", "Requests immediate refund"],
    "draft_response": None,
    "reviewer_feedback": None,
    "policy_chunks": ["Billing Policy: In the event of a duplicate or incorrect charge, Lloyds Bank will investigate the transaction within 5 working days. If the charge is confirmed as erroneous, a full refund will be processed within 3-5 working days back to the original payment method."],
    "audit_log": [],
    "human_review": None
}

result = drafter_node(test_state)
print(result)