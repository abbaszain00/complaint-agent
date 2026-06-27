
policies = [
    {
        "id": "billing_policy",
        "text": """Billing Policy: In the event of a duplicate or incorrect charge, 
        Lloyds Bank will investigate the transaction within 5 working days. 
        If the charge is confirmed as erroneous, a full refund will be processed 
        within 3-5 working days back to the original payment method. 
        Customers should provide the transaction date and amount when reporting 
        billing issues. Repeated billing errors may result in a goodwill payment 
        to the affected customer."""
    },
    {
        "id": "fraud_policy", 
        "text": """Fraud Policy: Lloyds Bank takes all reports of unauthorised 
        transactions seriously. Upon receiving a fraud report, the affected account 
        will be frozen immediately to prevent further unauthorised access. 
        A full investigation will be conducted within 10 working days. 
        Customers are not liable for unauthorised transactions provided they have 
        not acted negligently or shared their credentials. Refunds for confirmed 
        fraudulent transactions will be processed within 5 working days."""
    },
    {
        "id": "service_failure_policy",
        "text": """Service Failure Policy: When Lloyds Bank fails to deliver a 
        service to the expected standard, we are committed to resolving the issue 
        promptly. Customers affected by service failures are entitled to a formal 
        apology and a resolution within 5 working days. In cases where the service 
        failure has caused financial loss, compensation will be assessed on a 
        case-by-case basis. Customers may also escalate unresolved complaints to 
        the Financial Ombudsman Service after 8 weeks."""
    }
]

import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="bank_policies")

collection.add(
    ids=[p["id"] for p in policies],
    documents=[p["text"] for p in policies]
)

print("Database setup complete")
print(f"Stored {collection.count()} documents")