def process_exam_scores(csv_file):
    total = {}
    f_students = []
    with open(csv_file, "r") as f:
        for data in f:
            data = data.strip()
            item = data.split(",")
            if len(item) != 4:
                continue
            name, subject, score1, score2 = item
            try:
                score1 = int(score1)
                score2 = int(score2)
            except ValueError:
                print(f"Non numeric score isn`t accepted")
                continue
            both_score = score1 + score2
            if subject in total:
                total[subject] += both_score
            else:
                total[subject] = both_score
            if both_score < 100:
                f_students.append((name, both_score))
    return total, f_students

def save_grade_report(subject_totals, f_students):
    with open("grade_report.txt", "w") as f:
        f.write("SUBJECT TOTAL POINTS\n")
        f.write("--------------------\n")
        for subject, total in subject_totals.items():
            f.write(f"{subject}: {total}\n")
        f.write("\nAT RISK STUDENTS (< 100 pts)\n")
        f.write("----------------------------\n")
        for name, score in f_students:
            f.write(f"{name} ({score} pts)\n")

total, f_students = process_exam_scores("students.csv")
save_grade_report(total, f_students)
