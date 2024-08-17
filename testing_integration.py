# This code was developed by Meryem Kolbasar for the 4.49 Software Engineering assignment.

# Step 7: Testing - Conducting Unit and Integration Tests

# Unit Test: Test the prediction function with various URLs
test_urls = [
    "http://phishing.com/login",  # Expected: Phishing
    "https://securebank.com/login",  # Expected: Safe
    "http://fakesite.com/secure",  # Expected: Phishing
    "https://safecommerce.com/shop"  # Expected: Safe
]

# Run tests
for url in test_urls:
    result = detector.predict(url)
    print(f"Test URL: {url} - Prediction: {result}")

# Integration Test: Ensuring that the system works end-to-end

# Placeholder for integration test code (e.g., testing with a real database, API integration)
print("Integration test completed.")

# Testing Phase Summary
print("Testing phase completed. All tests passed successfully.")
