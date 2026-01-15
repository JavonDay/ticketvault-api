from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="TicketVault API")

class Ticket(BaseModel):
    id: int
    title: str
    status: str = "open"

class TicketCreate(BaseModel):
    title: str

tickets: List[Ticket] = []
ticket_id_counter = 1


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/tickets", response_model=List[Ticket])
def get_tickets():
    return tickets


@app.post("/tickets", response_model=Ticket)
def create_ticket(ticket: TicketCreate):
    global ticket_id_counter

    new_ticket = Ticket(
        id=ticket_id_counter,
        title=ticket.title,
        status="open"
    )

    tickets.append(new_ticket)
    ticket_id_counter += 1

    return new_ticket
