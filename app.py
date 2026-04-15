from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = request.form.get('expression', '')
    result = ""
    
    if request.method == 'POST':
        action = request.form.get('action', '')
        
        if action == 'calculate':
            try:
                result = str(eval(expression))
                expression = result
            except:
                result = "Error"
        elif action == 'clear':
            expression = ""
        elif action == 'delete':
            expression = expression[:-1]
        else:
            # Add number or operator
            expression += action
    
    return render_template('index.html', expression=expression, result=result)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)