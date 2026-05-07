import asyncio

from fastapi import Response

from app.main import error, root


def test_root_returns_running_message():
    assert asyncio.run(root()) == {
        "message": "FASTAPI with Prometheus is running",
    }


def test_error_sets_500_status_code():
    response = Response()

    result = asyncio.run(error(response))

    assert response.status_code == 500
    assert result == {"error": "Simulated Internal Server Error"}
