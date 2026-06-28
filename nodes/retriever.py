import chromadb
from state import ComplaintState
from dotenv import load_dotenv

load_dotenv()

def retriever_node(state: ComplaintState) -> dict:

    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="bank_policies")

    query = " ".join(state["extracted_claims"])

    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    audit_log = state["audit_log"]
    audit_log.append(f"retriever_node ran - retrieved results: {results} ")

    return {"policy_chunks": results["documents"][0], "audit_log": audit_log}