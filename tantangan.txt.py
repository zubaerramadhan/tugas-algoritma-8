def load_questions(file_path):
    """
    Membaca file dan memuat pertanyaan serta jawaban ke dalam list of dicts.
    """
    questions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split("||")
                if len(parts) == 2:
                    question, answer = parts[0].strip(), parts[1].strip()
                    questions.append({"question": question, "answer": answer})
        return questions
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return []

def check_answers(questions):
    """
    Menampilkan soal kepada pengguna, meminta jawaban, dan memeriksa kebenarannya.
    """
    for i, q in enumerate(questions):
        print(f"{i + 1}. {q['question']}")  # Menampilkan soal
        user_answer = input("Jawab: ").strip()
        
        if user_answer.lower() == q['answer'].lower():
            print("Jawaban benar!\n")
        else:
            print(f"Jawaban salah! Jawaban yang benar adalah: {q['answer']}\n")

def main():
    file_path = input("Masukkan nama file (contoh: tantangan.txt): ").strip()
    questions = load_questions(file_path)
    if questions:
        print("\nSoal berhasil dimuat. Mulai menjawab soal:\n")
        check_answers(questions)
    else:
        print("Tidak ada soal yang tersedia untuk dijawab.")
if __name__ == "__main__":
    main()