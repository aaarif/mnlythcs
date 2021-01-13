from flask import Flask, json, render_template, request, redirect, Response, url_for, send_file
import random
import string
import os
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template("index.html", token="Hello World! what are you doing?")


@app.route("/download", methods=['GET', 'POST'])
def download_template():
    print("Downloading txt file", file=sys.stdout)

    path = 'omnifile.txt'
    # app.logger.warning(f'Path : {path}')
    # return send_from_directory(directory, file_name=filename,
    # as_attachment=True)
    return send_file(path, as_attachment=True)


@app.route('/generate')
def generate_random():
    # return 'Hello World!'
    print("API generate called", file=sys.stdout)
    choice = [1, 2, 3, 4]
    filename = 'omnifile.txt'
    f = open(filename, 'w')
    f = open(filename, "a")
    countalnum = 0
    countintgr = 0
    countreal = 0
    countstr = 0
    file_stats = os.stat(filename)
    # print(f"Size of file in Bytes: {file_stats.st_size}")
    sizeMB = file_stats.st_size / (1024 * 1024)
    sizeMB = format(sizeMB, '.8f')
    sizeMB = float(sizeMB)
    # print(f"Size of file in MegaBytes: {sizeMB}")

    while(sizeMB < 2.0):
        kind_to_create = random.choice(choice)

        n = random.randint(5, 20)
        if 1 == kind_to_create:
            string_random = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase)
                                    for _ in range(n))
            f.write(string_random)
            countstr += 1
        if 2 == kind_to_create:
            integer_random = random.randint(5, 909989988)
            f.write(str(integer_random))
            countintgr += 1
        if 3 == kind_to_create:
            real_random = random.uniform(1.5, 9999999.9)
            f.write(str(real_random))
            countreal += 1
        if 4 == kind_to_create:
            alnum_random = ''.join(random.choice(string.ascii_lowercase + string.digits)
                                   for _ in range(n))
            f.write(alnum_random)
            countalnum += 1

        f.write(',')
        file_stats2 = os.stat(filename)
        # print(f"Size of file in Bytes: {file_stats.st_size}")
        sizeMB = file_stats2.st_size / (1024 * 1024)
        sizeMB = format(sizeMB, '.8f')
        sizeMB = float(sizeMB)

    f.close()

    report = {}
    report['alphanum'] = countalnum
    report['intgr'] = countintgr
    report['realnum'] = countreal
    report['strnum'] = countstr
    res = {}
    res['file'] = filename
    res['report'] = report
    return res

if __name__ == '__main__':
    app.run(debug=True)
