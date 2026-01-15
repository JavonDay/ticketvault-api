from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="TicketVault API")

class Ticket(BaseModel):
    id: int
    title: str
    status: str

tickets: List[Ticket] = []

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/tickets", response_model=List[Ticket])
def get_tickets():
    return tickets

@app.post("/tickets", response_model=Ticket)
def create_ticket(ticket: Ticket):
    tickets.append(ticket)
    return ticket
