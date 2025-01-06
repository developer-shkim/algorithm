import sys


def is_not_p(score):
    return score[1] != 'P'


scores = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

report_inputs = [sys.stdin.readline().strip().split(' ')[1::] for _ in range(20)]
totalGrade = sum(
    scores[report_input[1]] * float(report_input[0]) for report_input in report_inputs if is_not_p(report_input))
totalCredit = sum(
    float(report_input[0]) for report_input in report_inputs if is_not_p(report_input))

print(totalGrade / totalCredit)
