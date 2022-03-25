from flask import Flask, render_template, request, redirect
app = Flask('app')

todos = [
  {'title': 'Estudar Python'},
  {'title': 'Estudar JavaScript'}  
]

@app.route('/')
def hello_world():
  return render_template(
    'index.html',
    todos=todos
  )
@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  todos.append({'title' : title})
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)