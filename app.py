import os 
import sys 
import inquirer

if __name__ == "__main__":

    try:
        import lib.checkArgsAmount
        import lib.connectAPI    
        from lib.searchSO import searchStack
    except ImportError:
        print("There was an error trying to access our libraries.")
        sys.exit(0)

    questions = [
        inquirer.Text('question', message="What is your question?")
    ] 
    answers = inquirer.prompt(questions)
    print( answers['question'])
    #searchStack(answers['question'])