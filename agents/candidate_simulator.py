from utils.hf_llm import hf_llm

class CandidateSimulator:
    def run(self, questions):
        results = []
        for q in questions:
            if q.startswith("[HF ERROR]"):
                answer = q
            else:
                prompt = f"Answer the technical interview question: {q}"
                answer = hf_llm(prompt)
            results.append({"question": q, "answer": answer})
        return results
