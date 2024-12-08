def compare_documents(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1:
        doc1 = f1.readlines()

    with open(file2, 'r', encoding='utf-8') as f2:
        doc2 = f2.readlines()

    added_lines = []
    removed_lines = []
    common_lines = []

    max_lines = max(len(doc1), len(doc2))
    for i in range(max_lines):
        line1 = doc1[i] if i < len(doc1) else None
        line2 = doc2[i] if i < len(doc2) else None
        
        if line1 == line2:
            if line1 is not None:
                common_lines.append(line1.strip())
        elif line1 is None:
            added_lines.append(line2.strip())
        elif line2 is None:
            removed_lines.append(line1.strip())
        else:
            removed_lines.append(line1.strip())
            added_lines.append(line2.strip())

    print("Perbedaan antara kedua dokumen:")
    
    if added_lines:
        print("\nBaris yang ditambahkan pada dokumen kedua:")
        for line in added_lines:
            print(f"+ {line}")
    
    if removed_lines:
        print("\nBaris yang dihapus dari dokumen pertama:")
        for line in removed_lines:
            print(f"- {line}")

    if common_lines:
        print("\nBaris yang sama pada kedua dokumen:")
        for line in common_lines:
            print(f"  {line}")

compare_documents('file1.txt', 'file2.txt.txt')