from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import ComplaintState
from nodes.classifier import classifier_node
from nodes.extractor import extractor_node
from nodes.retriever import retriever_node
from nodes.drafter import drafter_node
from nodes.reviewer import reviewer_node
from nodes.human_gate import human_gate
from nodes.finaliser import finaliser_node


def route_after_review(state: ComplaintState) -> str:
    if state["review_passed"]:
        return "human_gate"
    else: 
        return "drafter_node"
    
def route_after_human(state: ComplaintState) -> str:
    if state["human_review"]:
        return "finaliser_node"
    else: 
        return "drafter_node"
    
    
checkpointer = MemorySaver()

graph = StateGraph(ComplaintState)

graph.add_node(classifier_node)
graph.add_node(extractor_node)
graph.add_node(retriever_node)
graph.add_node(drafter_node)
graph.add_node(reviewer_node)
graph.add_node(human_gate)
graph.add_node(finaliser_node)

graph.set_entry_point("classifier_node")
graph.add_edge("classifier_node", "extractor_node")
graph.add_edge("extractor_node", "retriever_node")
graph.add_edge("retriever_node", "drafter_node")
graph.add_edge("drafter_node", "reviewer_node")
graph.add_conditional_edges("reviewer_node", route_after_review)
graph.add_conditional_edges("human_gate", route_after_human)
graph.add_edge("finaliser_node", END)

app = graph.compile(checkpointer=checkpointer, interrupt_before=["human_gate"])
