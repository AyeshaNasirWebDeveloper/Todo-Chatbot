from typing import List, Dict, Any, Optional
from datetime import date
from src.services.flight_parser import FlightQuery

def get_mock_flights(query: FlightQuery) -> List[Dict[str, Any]]:
    """
    Mocks flight data retrieval based on a FlightQuery.
    In a real application, this would call an external flight API.
    """
    print(f"Mock flight search for: {query}")
    # Simulate some flight data based on query (very basic)
    if query.departure_airport.lower() == "london" and query.arrival_airport.lower() == "paris":
        return [
            {
                "flight_number": "BA234",
                "departure": "London Heathrow (LHR)",
                "arrival": "Paris Charles de Gaulle (CDG)",
                "departure_time": "2026-01-20T10:00:00Z",
                "arrival_time": "2026-01-20T11:30:00Z",
                "price": "£75",
                "currency": "GBP"
            },
            {
                "flight_number": "AF101",
                "departure": "London City (LCY)",
                "arrival": "Paris Orly (ORY)",
                "departure_time": "2026-01-20T12:00:00Z",
                "arrival_time": "2026-01-20T13:15:00Z",
                "price": "€85",
                "currency": "EUR"
            }
        ]
    return []
