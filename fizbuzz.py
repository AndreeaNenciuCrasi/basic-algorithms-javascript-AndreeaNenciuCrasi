"""
Write a program that prints the numbers from 1 to 100. But:
 - for multiples of three print “Fizz” instead of the number and
 - for the multiples of five print “Buzz”.
 - For numbers which are multiples of both three and five print “FizzBuzz”.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    print_list = []
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print_list.append('FIZZ + BUZZ')
        elif (i % 3 == 0) and (i % 5 != 0):
            print_list.append('FIZZ')
        elif (i % 3 != 0) and (i % 5 == 0):
            print_list.append('BUZZ')
        else:
            print_list.append(i)
    return render_template('home.html', print_list=print_list)

if __name__ == '__main__':
    app.run(debug=True)
