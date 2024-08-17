# This code was developed by Meryem Kolbasar for the 4.49 Software Engineering assignment.

# Step 6: Development - Implementing the Phishing Detector

# Creating an instance of the PhishingDetector class
detector = PhishingDetector()

# Loading a simulated model (in practice, this would be a complex ML model)
detector.load_model("path_to_pretrained_model.pkl")

# Testing the model with a sample URL
test_url = "http://phishing.com/login"
prediction = detector.predict(test_url)

print(f"The URL '{test_url}' is likely {prediction}.")
