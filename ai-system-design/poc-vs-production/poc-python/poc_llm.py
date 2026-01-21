from openai import OpenAI

client = OpenAI()

def ask_ai(question: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content


print(ask_ai("Explain AI POCs"))

/*

❌ Problems with this code

No timeout

No retry

No logging

No validation

No cost visibility

No protection from abuse

➡️ Works in demo, fails in production

*/
