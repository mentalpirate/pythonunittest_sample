import unittest
import requests

class TestURLLoading(unittest.TestCase):
    def test_url_loading(self):
        print("Step 1: Sending request to URL...")
        url = "https://atg.world"
        response = requests.get(url)
        print("Step 2: Verifying Loading of website...")
        # Asserting that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200, f"Failed to load URL: {url}")
        print("Step 3: URL loaded successfully.")

if __name__ == '__main__':
    unittest.main()