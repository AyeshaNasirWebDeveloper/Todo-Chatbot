from mcp_sdk.tool import Tool, tool_usage
from src.services.flight_parser import parse_flight_query, FlightQuery
from src.services.mock_flight_api import get_mock_flights
from typing import Dict, Any
import json

@tool_usage(name="get_flight_information", description="Get flight information based on a natural language query.")
def get_flight_information(query: str) -> Dict[str, Any]:
    """
    Retrieves flight information by parsing the query and then searching mock data.
    """
    flight_query = parse_flight_query(query)
    if not flight_query:
        return {"status": "error", "message": "Could not parse flight query."}

    flights = get_mock_flights(flight_query)
    if not flights:
        return {"status": "success", "message": f"No flights found for {flight_query.departure_airport} to {flight_query.arrival_airport} on {flight_query.departure_date}."}

    return {"status": "success", "flights": flights}
