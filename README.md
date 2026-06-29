# Complaint Agent

A multi-agent complaint triage and response drafting system built with LangGraph,
designed to mirror real agentic AI workflows being deployed in UK financial services
(Lloyds, HSBC, Aviva).

A customer complaint letter goes in. A reviewed, policy-grounded response letter
comes out — with a human approving it before anything is finalised.

## What it does

1. **Classifies** the complaint type (billing, fraud, service failure, etc.)
2. **Extracts** the specific claims the customer is making
3. **Retrieves** the relevant bank policy using RAG (ChromaDB)
4. **Drafts** a professional response letter grounded in that policy
5. **Reviews** the draft against quality criteria — loops back if it fails
6. **Pauses for human approval** before finalising
7. **Logs** every decision made throughout the pipeline

## Architecture

```
complaint_letter
      ↓
classifier_node (Haiku)
      ↓
extractor_node (Haiku)
      ↓
retriever_node (ChromaDB)
      ↓
drafter_node (Sonnet)
      ↓
reviewer_node (Sonnet) ←──────────┐
      ↓ (pass)                    │ (fail)
human_gate ────────────────────────┘
      ↓ (approved)
finaliser_node
```

## Key architectural decisions

**Model routing** — Haiku handles classification and extraction (fast, cheap,
well-scoped tasks). Sonnet handles drafting and review (requires judgment and
quality output).

**Evaluator-optimizer loop** — the reviewer checks the draft against three
criteria: policy accuracy, professional tone, and completeness. If it fails,
the feedback goes back to the drafter automatically.

**Human-in-the-loop** — LangGraph checkpointing pauses the graph after the
reviewer passes the draft. A human reviews and approves or rejects via API
before the response is finalised. If rejected, it loops back to the drafter.

**Audit trail** — every node appends to a running audit log in state, capturing
which model ran, what it decided, and why. Designed for regulated environments
where explainability matters.

## Stack

- LangGraph — graph orchestration and human-in-the-loop checkpointing
- Anthropic API — Claude Haiku and Sonnet
- ChromaDB — vector store for policy document retrieval
- FastAPI — REST API layer
- Python-dotenv — environment variable management

## Setup

```bash
# clone and install
git clone https://github.com/abbaszain00/complaint-agent.git
cd complaint-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# add your API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# populate the policy database
python setup_db.py

# run the API
uvicorn main:api --reload
```

## API

### Submit a complaint

```
POST /complaint?complaint_letter=your complaint text here
```

Returns a `thread_id` and `draft_response`.

### Approve the draft

```
POST /approve?thread_id=your_thread_id
```

Resumes the graph and returns the finalised response.

### Reject the draft

```
POST /reject?thread_id=your_thread_id
```

Sends the draft back to the drafter and returns a revised response.

## Project structure

```
complaint-agent/
├── state.py              # shared state TypedDict
├── graph.py              # LangGraph graph definition
├── main.py               # FastAPI endpoints
├── setup_db.py           # ChromaDB population script
├── nodes/
│   ├── classifier.py
│   ├── extractor.py
│   ├── retriever.py
│   ├── drafter.py
│   ├── reviewer.py
│   ├── human_gate.py
│   └── finaliser.py
└── requirements.txt
```

## Context

Built as a portfolio project to prepare for deployment as a Frontier AI Engineer
at a UK enterprise client. The domain and architecture are based on publicly
documented AI initiatives at Lloyds Banking Group and HSBC (2025-2026).
