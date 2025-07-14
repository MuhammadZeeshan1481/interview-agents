from utils.hf_llm import hf_llm

class QuestionGenerator:
    def run(self, role="React Developer", num_questions=3):
        prompt = (
            f"Generate exactly {num_questions} technical interview questions "
            f"for the role of a {role}. Return only the questions, numbered 1 to {num_questions}, "
            f"one per line, without answers or explanations."
        )

        output = hf_llm(prompt)

        if output.startswith("[HF ERROR]"):
            return [output]

        questions = []
        for line in output.split("\n"):
            line = line.strip()
            if line and any(c.isalpha() for c in line):
                # Remove "1. ", "2)", etc.
                question = line.split(".", 1)[-1].strip() if "." in line[:3] else line
                questions.append(question)

        return questions[:num_questions]
