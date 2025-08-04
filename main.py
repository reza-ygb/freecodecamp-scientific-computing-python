def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems vertically and side by side.
    
    Args:
        problems (list): List of arithmetic problems as strings
        show_answers (bool): Whether to display the answers
    
    Returns:
        str: Formatted arithmetic problems or error message
    """
    if len(problems) > 5:
        return "Error: Too many problems."
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for idx, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and one operator."
        first, operator, second = parts[0], parts[1], parts[2]

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        width = max(len(first), len(second)) + 2
        line1 += first.rjust(width)
        line2 += operator + second.rjust(width - 1)
        line3 += "-" * width
        
        if show_answers:
            if operator == "+":
                answer = str(int(first) + int(second))
            elif operator == "-":
                answer = str(int(first) - int(second))
            line4 += answer.rjust(width)

        if idx < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            if show_answers:
                line4 += "    "
                
    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if show_answers:
        arranged_problems += "\n" + line4
    return arranged_problems


if __name__ == "__main__":
    # Example usage
    problems = ["34 + 658", "285 - 49", "254 + 18", "542 - 412"]
    print(arithmetic_arranger(problems, True))



