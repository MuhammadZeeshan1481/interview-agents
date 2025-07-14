from utils.hf_llm import hf_llm

class Evaluator:
    def run(self, qa_pairs):
        results = []
        for pair in qa_pairs:
            q = pair["question"]
            a = pair["answer"]
            if "[HF ERROR]" in a:
                feedback = a
            else:
                prompt = f"Evaluate the candidate's answer to the question.\n\nQuestion: {q}\nAnswer: {a}\n\nGive feedback:"
                feedback = hf_llm(prompt)
                
            results.append({
                "question": q,
                "answer": a,
                "feedback": feedback
            })
        return results