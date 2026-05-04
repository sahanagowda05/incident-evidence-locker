from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.security import sanitize_input 

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.json
    incident = data.get("incident")

    if not incident:
        return jsonify({"error": "Missing incident"}), 400
    clean_incident = sanitize_input(incident)
    if clean_incident is None:
        return jsonify({"error": "Invalid or unsafe input"}), 400
    prompt = f"""
    Analyze the incident below and return ONLY valid JSON.
    Incident: {incident}

    Return strictly in this format:
    {{
        "title": "...",
        "summary": "...",
        "severity": "Low | Medium | High",
        "key_points": ["...", "...", "..."]
    }}
    """

    result = call_groq(prompt)

    return jsonify({
        "generated_at": "now",
        "description": result
    })
