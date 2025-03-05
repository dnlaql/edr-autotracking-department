import random

def chatbot_response(query, eda_results):
    """
    Rule-based chatbot to explain EDA insights.
    """
    most_affected_department = eda_results.get("most_affected_department", "Unknown")
    most_common_threat = eda_results.get("most_common_threat", "Unknown")
    resolved_threats_count = eda_results.get("resolved_threats_count", 0)
    total_threats_count = eda_results.get("total_threats_count", 0)

    responses = {
        "most affected department": [
            f"The **{most_affected_department}** department has reported the highest number of threats. Immediate security improvements are recommended!",
            f"Our analysis shows that **{most_affected_department}** is the most targeted department. Consider tightening access control measures.",
        ],
        "most common threat": [
            f"The most frequently detected threat is **{most_common_threat}**. Strengthening defenses against this type is crucial.",
            f"Our data reveals that **{most_common_threat}** occurs most often. Be sure to update your security protocols!",
        ],
        "resolved threats": [
            f"So far, **{resolved_threats_count}** threats have been successfully neutralized. Keep up the strong response!",
            f"The system has handled **{resolved_threats_count}** threats effectively, but continued vigilance is needed.",
        ],
        "total threats": [
            f"A total of **{total_threats_count}** threats have been logged in the system. Regular monitoring is essential.",
            f"Our records indicate **{total_threats_count}** threats detected. Keep an eye on any rising trends.",
        ],
        "recommendations": [
            "To reduce threats, implement **firewall restrictions, endpoint protection, and security training for employees**.",
            "Enhance security by **limiting user access, enabling real-time monitoring, and enforcing strict authentication**.",
        ],
    }

    for key in responses:
        if key in query.lower():
            return random.choice(responses[key])

    return "I'm sorry, I couldn't understand your request. Can you specify what insights you need?"
