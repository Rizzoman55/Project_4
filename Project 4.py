#!/usr/bin/env python
# coding: utf-8

# In[24]:


import openai

# Set your OpenAI API key here
api_key = 'sk______________________________________'
openai.api_key = api_key

def risk_assessment(transaction_description):
    try:
        # Define the prompt for GPT-3 based on the transaction description
        prompt = f"Assess the risk associated with the following financial transaction:\n{transaction_description}\nRisk assessment:"

        # Use GPT-3 to generate a risk assessment score
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=prompt,
            max_tokens=50,
            temperature=0.5,
            n=1,
            stop=["\n"]
        )

        # Extract the risk assessment score from the GPT-3 response
        completion_text = response['choices'][0]['text']
        risk_score = float(completion_text.strip())

        return risk_score

    except Exception as e:
        print("Error:", e)
        return None

# Testing the function with various transaction descriptions
transaction_1 = "Investing in a highly diversified index fund with a long-term horizon"
transaction_2 = "Purchasing speculative cryptocurrency tokens from an unverified source"
transaction_3 = "Taking out a mortgage to buy a home in a stable housing market"
transaction_4 = "Investing in a Vanguard IRA rolling over a 401k plan with 40,000"
transaction_5 = "Taking out a personal loan to buy a new car with high interest rates"

print("Transaction 1 Risk Assessment Score:", risk_assessment(transaction_1))
print("Transaction 2 Risk Assessment Score:", risk_assessment(transaction_2))
print("Transaction 3 Risk Assessment Score:", risk_assessment(transaction_3))
print("Transaction 4 Risk Assessment Score:", risk_assessment(transaction_4))
print("Transaction 5 Risk Assessment Score:", risk_assessment(transaction_5))

