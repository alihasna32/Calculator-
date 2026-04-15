from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ""
    result = ""
    
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        action = request.form.get('action', '')
        
        if action == 'calculate':
            try:
                result = str(eval(expression))
                expression = result  # ফলাফলকে নতুন expression হিসেবে রাখে
            except:
                result = "Error"
        elif action == 'clear':
            expression = ""
        elif action == 'delete':
            expression = expression[:-1]
        else:
            # সংখ্যা বা অপারেটর যোগ করা
            expression += action
    
    return render_template('index.html', expression=expression, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))   # This is important
    app.run(host="0.0.0.0", port=port)