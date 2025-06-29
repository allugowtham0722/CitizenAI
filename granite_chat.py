def get_granite_response(prompt):
    prompt = prompt.lower().strip()

    responses = {
        "how do i apply for a government job": "You can apply for a government job through the official state or central portals like https://ncs.gov.in.",
        "what is citizenai": "CitizenAI is an AI-powered platform to help citizens engage with government services easily.",
        "how can i report an issue": "You can report issues through the 'Report Concern' section of our platform.",
        "what services does citizenai provide": "Chat assistant, sentiment analysis, issue reporting, and a citizen dashboard.",
        "who developed citizenai": "This platform was developed as a civic engagement project using Flask and AI."
    }

    return responses.get(prompt, "Sorry, I don't have an answer for that. Please try a different question.")
