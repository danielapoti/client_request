import pytest
import sys
import io
import logging
from unittest.mock import patch
from bigqueryapi.retrieve_buckets import retrieve_buckets  # Assuming this import path


@pytest.fixture
def mock_client():
    with patch("google.cloud.storage.Client") as client:
        yield client


def test_retrieve_buckets(mock_client, monkeypatch):
    # Mock the project ID
    monkeypatch.setenv("project_id", "test-project-id")

    # Mock the storage client to return a list of buckets
    mock_client.return_value.list_buckets.return_value = [
        {"name": "bucket1"},
        {"name": "bucket2"},
    ]

    # Create a capture handler for logging (optional)
    capture_handler = io.StringIO()
    handler = logging.StreamHandler(capture_handler)
    logger = logging.getLogger()
    logger.addHandler(handler)

    # Mock sys.stdout to capture printed output
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    # Call the function
    retrieve_buckets()

    # Remove the capture handler (optional)
    logger.removeHandler(handler)

    # Assert captured log messages (optional)
    captured_logs = capture_handler.getvalue().strip()
    assert "Starting script execution" in captured_logs
    assert "Buckets retrieved successfully!" in captured_logs

    # Assert printed buckets
    assert "Buckets:" in captured_output.getvalue()
    assert "bucket1" in captured_output.getvalue()
    assert "bucket2" in captured_output.getvalue()


# Test error scenario with permission issues
def test_retrieve_buckets_permission_error(mock_client, monkeypatch):
    # Mock the project ID
    monkeypatch.setenv("project_id", "test-project-id")

    # Mock the storage client to raise a permission error
    mock_client.return_value.list_buckets.side_effect = PermissionError("Permission denied")

    # Capture logs using the capture handler (optional)
    capture_handler = io.StringIO()
    handler = logging.StreamHandler(capture_handler)
    logger = logging.getLogger()
    logger.addHandler(handler)

    # Mock sys.stdout (same approach)
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    # Call the function and capture the error
    with pytest.raises(PermissionError):
        retrieve_buckets()

    # Remove the capture handler
    logger.removeHandler(handler)

    # Assert captured log messages (optional)
    captured_logs = capture_handler.getvalue().strip()
    assert "Starting script execution" in captured_logs

    # No need to check for "Buckets:" since the error might prevent it from printing
