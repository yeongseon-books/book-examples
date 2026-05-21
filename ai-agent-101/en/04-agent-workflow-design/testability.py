"""Generated from book-content article."""

from unittest.mock import Mock, patch

import pytest


def test_workflow_success():
    """Test success case"""
    # Mock tools
    with patch('execute_tool') as mock_execute:
        mock_execute.return_value = {"data": "test result"}

        # Execute workflow
        result = run_workflow("test task")

        # Verify
        assert result["status"] == "success"
        assert mock_execute.call_count == 3  # 3 steps executed

def test_workflow_failure_recovery():
    """Test failure recovery"""
    with patch('execute_tool') as mock_execute:
        # First call fails, second succeeds
        mock_execute.side_effect = [
            Exception("Network error"),
            {"data": "recovered"}
        ]

        result = run_workflow_with_retry("test task")

        # Verify success after retry
        assert result["status"] == "success"
        assert mock_execute.call_count == 2
