from typing import TypedDict

class ComplaintState(TypedDict):
    complaint_letter: str
    classification: str | None
    extracted_claims: list[str] | None
    draft_response: str | None
    reviewer_feedback: str | None
    policy_chunks: list[str] | None
    audit_log: list[str]
    human_review: bool | None
    review_passed: bool | None