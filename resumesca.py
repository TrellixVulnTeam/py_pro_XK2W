def scan_resume(resume):
    from resume_parser import resumeparse
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}:>>{j}")

scan_resume("resume_fajar_trengginas.docx")