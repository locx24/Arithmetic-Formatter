def arithmetic_arranger(problems):

  top_row = ""
  bottom_row = ""
  dash_line = ""
  result_row = ""  # Displays the result row

  for problem in problems:
    operand1, operator, operand2 = problem.split()
    
    # Format the operands and align them to the right
    operand1 = operand1.rjust(len(operand2) + 2)
    operand2 = operator + " " + operand2.rjust(len(operand2))
    dashes = "-" * max(len(operand1), len(operand2))

    # Accumulate the formatted strings for each row
    top_row += operand1 + "    "
    bottom_row += operand2 + "    "
    dash_line += dashes + "    "
    
    # Display the results
    result = str(eval(problem))  # Evaluate the problem to get the result using eval()
    result_row += result.rjust(len(dashes)) + "    "

    # Join the formatted strings for each row using newline characters
  arranged_problems = "\n".join([top_row, bottom_row, dash_line, result_row])

  return arranged_problems
