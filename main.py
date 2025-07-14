from agents.question_generator import QuestionGenerator
from agents.candidate_simulator import CandidateSimulator
from agents.evaluator import Evaluator

def run_interview(role="React Developer", num_questions=3):
    print(f"[INFO] Running interview for: {role}, Questions: {num_questions}")

    q_agent = QuestionGenerator()
    questions = q_agent.run(role, num_questions)

    c_agent = CandidateSimulator()
    answers = c_agent.run(questions)

    e_agent = Evaluator()
    feedbacks = e_agent.run(answers)

    # Combine question, answer, and feedback
    results = [
        {
            "question": q,
            "answer": a["answer"],
            "feedback": a["feedback"]
        }
        for q, a in zip(questions, feedbacks)
    ]

    return results

if __name__ == "__main__":
    output = run_interview()
    for item in output:
        print("\nQ:", item["question"])
        print("Answer:", item["answer"])
        print("Feedback:", item["feedback"])
