# import datetime
from random import *
from fpdf import FPDF
from flask import *

class QuestionBank:

    EQUAL_SIGN = '= '

    QTYPE_MUL = 1
    QTYPE_DIV = 2
    QTYPE_MIX = 3

    def __init__(self):
        pass

    # qtype = 1: multiplication only
    # qtype = 2: division only
    # qtype = 3: mixed questions (a*b-c)
    def generator(self, qtype: int):
        a = randint(2, 9)
        b = randint(2, 9)
        c = randint(2, 9)
        d = a * b

        invalid = False

        invalid = self.validate(a, c, d, invalid, qtype)

        # rerun generator if Q is invalid
        if invalid:
            return self.generator(qtype)

        a = str(a)
        b = str(b)
        d = str(d)

        if qtype == 1:
            question = a + '*' + b + self.EQUAL_SIGN
        elif qtype == 2:
            question = d + '/' + a + self.EQUAL_SIGN
        else:

            times = bool(getrandbits(1))
            add = bool(getrandbits(1))

            if times:
                question = b + '*' + a
            else:
                question = d + '/' + a

            if add:
                question += '+' + str(3 * c) + self.EQUAL_SIGN
            else:
                question += '-' + str(c) + self.EQUAL_SIGN

        return question

    def validate(self, a, c, d, invalid, qtype):
        if d < 10:
            invalid = True
        if qtype == 3 and d / a - c < 0:
            invalid = True
        return invalid

class Test:

    OUTPUT_TXT_FILE = 'temp.txt'
    OUTPUT_PDF_FILE = 'final.pdf'
    LEN_OF_COL = 10
    LEN_OF_COL_MIX = 12

    def __init__(self):
        pass


    def output_to_text_file(self,qlist, qtype, file):

        END_OF_LINE = '\n'

        if qtype == QuestionBank.QTYPE_MIX:
            columns = 5
            length_of_col = self.LEN_OF_COL_MIX
        else:
            columns = 6
            length_of_col = self.LEN_OF_COL

        no_of_q = len(qlist)
        cursor = 0
        rows = int(no_of_q / columns)
        for i in range(rows):
            for j in range(columns):
                s = qlist[cursor].ljust(length_of_col)
                file.write(s)
                cursor += 1
            file.write(END_OF_LINE)
        file.write(END_OF_LINE)

    def convert_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=15)

        with open(self.OUTPUT_TXT_FILE, 'r') as file:
            for line in file:
                pdf.cell(200, 10, txt=line, ln=1, align='L')

        # t = datetime.datetime.now()
        # date_time = t.strftime("%Y-%m-%d_%H%M")
        # pdf.output(OUTPUT_PDF_FILE+str(date_time)+".pdf")
        pdf.output(self.OUTPUT_PDF_FILE)

    def generate_test(self):
        file = open(self.OUTPUT_TXT_FILE, 'w')

        qgen = QuestionBank()

        # multiplication
        mulQs = []
        for i in range(48):
            q = qgen.generator(QuestionBank.QTYPE_MUL)
            mulQs.append(q)
        self.output_to_text_file(mulQs, QuestionBank.QTYPE_MUL, file)

        # division
        divQs = []
        for i in range(40):
            q = qgen.generator(QuestionBank.QTYPE_DIV)
            divQs.append(q)
        self.output_to_text_file(divQs, QuestionBank.QTYPE_DIV, file)

        # mixed
        mixQs = []
        for i in range(32):
            q = qgen.generator(QuestionBank.QTYPE_MIX)
            mixQs.append(q)
        self.output_to_text_file(mixQs, QuestionBank.QTYPE_MIX, file)

        file.close()

        self.convert_to_pdf()

# to run it locally
# t = Test()
# t.generate_test()


# to run it on a server
app = Flask('main')

@app.route('/')
def pdf():
    t = Test()
    t.generate_test()
    return send_file('final.pdf')

# app.run()
app.run(host='0.0.0.0', port=8001)



