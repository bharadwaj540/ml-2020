# evaluates an expression using predefined eval()
def eval_exp():
    expr = input("Enter an expression")
    # This try block is used to print error if user enter an invalid expression
    try:
        print("Result:", eval(expr))
        print("-----------------")
    except Exception as e:
        print("Enter a valid expression")
        print("ERROR:", str(e))
