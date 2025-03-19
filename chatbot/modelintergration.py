from together import Together
import json

# Initialize Together AI client
together_client = Together(api_key="e3ab4476326269947afb85e9c0b0ed5fe9ae2949e27ed3a38ee4913d8f807b3e")

maternal_health_prompt_preconceiption_stage = """
You are an AI that generates **maternal health quizzes focused on the preconception stage (When preparing to get pregnant)** in JSON format.

### **Instructions:**
1. **Generate 10 multiple-choice questions** on maternal health.
2. **Each question should have three answer options** (A, B, C).
3. **Specify the correct answer** for each question.
4. **Include an explanation** for both correct and incorrect responses.
5. **Respond ONLY with a JSON array** (list of 10 questions). No extra text.

### **Expected JSON Format:**
[
    {
        "question": "Which nutrient is essential for preventing neural tube defects during pregnancy?",
        "options": ["Vitamin C", "Iron", "Folic Acid"],
        "answer": "Folic Acid",
        "correctReason": "Folic acid helps prevent birth defects in the baby's brain and spine.",
        "incorrectReason": "Other vitamins are important but do not prevent neural tube defects."
    },
    {...},  # 1 more questions in the same format
]

**IMPORTANT:**  
- **DO NOT** include explanations outside the JSON.  
- **DO NOT** add any introductory text.  
- **DO NOT** wrap JSON in markdown.  
- **Only return raw JSON output (an array of 10 questions).**
"""

maternal_health_prompt_prenatal_stage = """
You are an AI that generates **maternal health quizzes focused on the prenatal stage (When preparing to get pregnant)** in JSON format.

### **Instructions:**
1. **Generate 10 multiple-choice questions** on maternal health.
2. **Each question should have three answer options** (A, B, C).
3. **Specify the correct answer** for each question.
4. **Include an explanation** for both correct and incorrect responses.
5. **Respond ONLY with a JSON array** (list of 10 questions). No extra text.

### **Expected JSON Format:**
[
    {
        "question": "Which nutrient is essential for preventing neural tube defects during pregnancy?",
        "options": ["Vitamin C", "Iron", "Folic Acid"],
        "answer": "Folic Acid",
        "correctReason": "Folic acid helps prevent birth defects in the baby's brain and spine.",
        "incorrectReason": "Other vitamins are important but do not prevent neural tube defects."
    },
    {...},  # 1 more questions in the same format
]

**IMPORTANT:**  
- **DO NOT** include explanations outside the JSON.  
- **DO NOT** add any introductory text.  
- **DO NOT** wrap JSON in markdown.  
- **Only return raw JSON output (an array of 10 questions).**
"""

maternal_health_prompt_birth_stage = """
You are an AI that generates **maternal health quizzes focused on the birth stage (When preparing to get pregnant)** in JSON format.

### **Instructions:**
1. **Generate 10 multiple-choice questions** on maternal health.
2. **Each question should have three answer options** (A, B, C).
3. **Specify the correct answer** for each question.
4. **Include an explanation** for both correct and incorrect responses.
5. **Respond ONLY with a JSON array** (list of 10 questions). No extra text.

### **Expected JSON Format:**
[
    {
        "question": "Which nutrient is essential for preventing neural tube defects during pregnancy?",
        "options": ["Vitamin C", "Iron", "Folic Acid"],
        "answer": "Folic Acid",
        "correctReason": "Folic acid helps prevent birth defects in the baby's brain and spine.",
        "incorrectReason": "Other vitamins are important but do not prevent neural tube defects."
    },
    {...},  # 1 more questions in the same format
]

**IMPORTANT:**  
- **DO NOT** include explanations outside the JSON.  
- **DO NOT** add any introductory text.  
- **DO NOT** wrap JSON in markdown.  
- **Only return raw JSON output (an array of 10 questions).**
"""

maternal_health_prompt_postnatal_stage = """
You are an AI that generates **maternal health quizzes focused on the postnatal stage (When preparing to get pregnant)** in JSON format.

### **Instructions:**
1. **Generate 10 multiple-choice questions** on maternal health.
2. **Each question should have three answer options** (A, B, C).
3. **Specify the correct answer** for each question.
4. **Include an explanation** for both correct and incorrect responses.
5. **Respond ONLY with a JSON array** (list of 10 questions). No extra text.

### **Expected JSON Format:**
[
    {
        "question": "Which nutrient is essential for preventing neural tube defects during pregnancy?",
        "options": ["Vitamin C", "Iron", "Folic Acid"],
        "answer": "Folic Acid",
        "correctReason": "Folic acid helps prevent birth defects in the baby's brain and spine.",
        "incorrectReason": "Other vitamins are important but do not prevent neural tube defects."
    },
    {...},  # 1 more questions in the same format
]

**IMPORTANT:**  
- **DO NOT** include explanations outside the JSON.  
- **DO NOT** add any introductory text.  
- **DO NOT** wrap JSON in markdown.  
- **Only return raw JSON output (an array of 10 questions).**
"""

def get_chatbot_response_preconception():
    """Fetch AI-generated quiz questions formatted for the frontend."""
    
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": maternal_health_prompt_preconceiption_stage},
            {"role": "user", "content": "Generate a new quiz question on maternal health."}
        ],
        max_tokens=4000,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["\n\n"],  # Stop at double newline to avoid extra text
    )

    try:
        response_text = response.choices[0].message.content.strip()
        print("Raw AI Response:", response_text)  # Debugging Step
        
        # Detect JSON structure issues
        if response_text.startswith("[") and response_text.endswith("]"):
            return json.loads(response_text)  # Parse valid JSON
        
        # Handle potential truncation
        elif response_text.startswith("[") and not response_text.endswith("]"):
            response_text += "]"  
            return json.loads(response_text)
        
        else:
            return {"error": "Response is not a valid JSON array"}
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response as JSON"}

def get_chatbot_response_prenatal():
    """Fetch AI-generated quiz questions formatted for the frontend."""
    
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": maternal_health_prompt_prenatal_stage},
            {"role": "user", "content": "Generate a new quiz question on maternal health."}
        ],
        max_tokens=4000,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["\n\n"],  # Stop at double newline to avoid extra text
    )

    try:
        response_text = response.choices[0].message.content.strip()
        print("Raw AI Response:", response_text)  # Debugging Step
        
        # Detect JSON structure issues
        if response_text.startswith("[") and response_text.endswith("]"):
            return json.loads(response_text)  # Parse valid JSON
        
        # Handle potential truncation
        elif response_text.startswith("[") and not response_text.endswith("]"):
            response_text += "]"  
            return json.loads(response_text)
        
        else:
            return {"error": "Response is not a valid JSON array"}
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response as JSON"}
    
def get_chatbot_response_birth():
    """Fetch AI-generated quiz questions formatted for the frontend."""
    
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": maternal_health_prompt_birth_stage},
            {"role": "user", "content": "Generate a new quiz question on maternal health."}
        ],
        max_tokens=4000,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["\n\n"],  # Stop at double newline to avoid extra text
    )

    try:
        response_text = response.choices[0].message.content.strip()
        print("Raw AI Response:", response_text)  # Debugging Step
        
        # Detect JSON structure issues
        if response_text.startswith("[") and response_text.endswith("]"):
            return json.loads(response_text)  # Parse valid JSON
        
        # Handle potential truncation
        elif response_text.startswith("[") and not response_text.endswith("]"):
            response_text += "]"  
            return json.loads(response_text)
        
        else:
            return {"error": "Response is not a valid JSON array"}
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response as JSON"}

def get_chatbot_response_postnatal():
    """Fetch AI-generated quiz questions formatted for the frontend."""
    
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": maternal_health_prompt_postnatal_stage},
            {"role": "user", "content": "Generate a new quiz question on maternal health."}
        ],
        max_tokens=4000,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["\n\n"],  # Stop at double newline to avoid extra text
    )

    try:
        response_text = response.choices[0].message.content.strip()
        print("Raw AI Response:", response_text)  # Debugging Step
        
        # Detect JSON structure issues
        if response_text.startswith("[") and response_text.endswith("]"):
            return json.loads(response_text)  # Parse valid JSON
        
        # Handle potential truncation
        elif response_text.startswith("[") and not response_text.endswith("]"):
            response_text += "]"  
            return json.loads(response_text)
        
        else:
            return {"error": "Response is not a valid JSON array"}
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response as JSON"}