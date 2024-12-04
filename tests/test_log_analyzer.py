import unittest
import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.utils.log_analyzer import LogAnalyzer
from unittest.mock import MagicMock

class TestLogAnalyzer(unittest.TestCase):
    
    def setUp(self):
        """
        Initialize test variables and mock the LogAnalyzer client.
        """
        self.project_id = "test-project-id"
        self.log_analyzer = LogAnalyzer(self.project_id)
        
        # Mock the client used by LogAnalyzer to simulate log fetching behavior
        self.log_analyzer.client = MagicMock()

    def test_get_used_permissions(self):
        """
        Test the get_used_permissions method for correct permissions extraction.
        """
        # Mock log entries with specific permissions
        mock_logs = [
            MagicMock(proto_payload={"methodName": "permission1"}),
            MagicMock(proto_payload={"methodName": "permission2"})
        ]
        
        # Mock the 'list_entries' method to return the mock logs
        self.log_analyzer.client.list_entries = MagicMock(return_value=mock_logs)

        # Call the method to get used permissions
        used_permissions = self.log_analyzer.get_used_permissions(90)

        # Assertions to verify that the expected permissions are returned
        self.assertIn("permission1", used_permissions)
        self.assertIn("permission2", used_permissions)
        self.assertEqual(len(used_permissions), 2)

    def test_get_used_permissions_empty(self):
        """
        Test that the method returns an empty list when no permissions are found.
        """
        # Mock the 'list_entries' to return an empty list (no logs)
        self.log_analyzer.client.list_entries = MagicMock(return_value=[])
        
        # Call the method
        used_permissions = self.log_analyzer.get_used_permissions(90)

        # Assertions to check that no permissions are returned
        self.assertEqual(len(used_permissions), 0)

    def test_get_used_permissions_with_invalid_data(self):
        """
        Test the method when log entries do not have the expected 'methodName' field.
        """
        # Mock log entries with invalid data (missing 'methodName')
        mock_logs = [
            MagicMock(proto_payload={}),
            MagicMock(proto_payload={})
        ]
        
        # Mock the 'list_entries' method to return these logs
        self.log_analyzer.client.list_entries = MagicMock(return_value=mock_logs)
        
        # Call the method
        used_permissions = self.log_analyzer.get_used_permissions(90)
        
        # Assertions to ensure that no permissions are extracted
        self.assertEqual(len(used_permissions), 0)

if __name__ == "__main__":
    unittest.main()
