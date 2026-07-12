
from unittest.mock import patch, MagicMock
from app.services import fact_checker


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_returns_summary(mock_get):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "extract": "Artificial Intelligence is the simulation of human intelligence by machines."
    }

    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("Artificial Intelligence")

    assert isinstance(summary, str)
    assert "Artificial Intelligence" in summary


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_no_data(mock_get):

    mock_response = MagicMock()
    mock_response.status_code = 404

    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("Unknown Topic")

    assert summary == "No information found."


@patch("app.services.fact_checker.requests.get")
def test_fact_checker_network_error(mock_get):

    mock_get.side_effect = Exception("Network Error")

    summary = fact_checker.fact_check("Artificial Intelligence")

    assert "error" in summary.lower()