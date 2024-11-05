import unittest
import os
from utils import logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        # Generate path
        self.log_file = "logs/project.log"
        
        # Clear the log file before each test
        if os.path.exists(self.log_file):
            open(self.log_file, 'w').close()

    def test_log_info(self):
        # Log a message and check if it was written to the log file
        logger.log("info", "Test info message")
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn("INFO", logs)
        self.assertIn("Test info message", logs)

    def test_log_warning(self):
        logger.log("warning", "Test warning message")
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn("WARNING", logs)
        self.assertIn("Test warning message", logs)

    def test_log_error(self):
        logger.log("error", "Test error message")
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn("ERROR", logs)
        self.assertIn("Test error message", logs)

    def test_log_debug(self):
        logger.log("debug", "Test debug message")
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn("DEBUG", logs)
        self.assertIn("Test debug message", logs)

if __name__ == "__main__":
    unittest.main()
