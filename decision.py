import pandas as pd

class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

class Leaf:
    def __init__(self, recommendation):
        self.recommendation = recommendation

def ask_question(question):
    print(question)
    answer = input("Pilih 'ya' atau 'tidak': ").lower()
    return answer == 'ya'

def build_decision_tree():
    question_1 = "Apakah ODO Kilometer kurang dari 10.000 km?"
    true_branch_1 = DecisionNode("Apakah Umur Kendaraan lebih dari 5 tahun?", None, None)
    false_branch_1 = DecisionNode("Apakah Penggunaan Kendaraan anda berintensitas tinggi?", None, None)

    true_branch_1.true_branch = DecisionNode("Apakah Jarak Tempuh Kendaraan lebih dari 50.000 km?", None, None)
    true_branch_1.false_branch = DecisionNode("Apakah Keluhan atau Masalah yang Dialami?", None, None)

    false_branch_1.true_branch = DecisionNode("Apakah Keluhan atau Masalah yang Dialami?", None, None)
    false_branch_1.false_branch = DecisionNode("Apakah Kondisi Kendaraan Saat Ini memerlukan perbaikan besar?", None, None)

    question_2 = "Apakah Batas Waktu Terakhir Layanan lebih dari 1 tahun sejak layanan terakhir?"
    true_branch_2 = DecisionNode("Apakah Budget untuk Layanan sudah ditentukan?", None, None)
    false_branch_2 = DecisionNode("Apakah Waktu Terakhir Pergantian Oli lebih dari 6 bulan?", None, None)

    true_branch_2.true_branch = DecisionNode("Apakah Ketersediaan Suku Cadang tertentu?", None, None)
    true_branch_2.false_branch = DecisionNode("Apakah Lokasi Penggunaan Kendaraan di perkotaan?", None, None)

    false_branch_2.true_branch = DecisionNode("Apakah Pengecekan Kelistrikan diperlukan?", None, None)
    false_branch_2.false_branch = DecisionNode("Apakah Pemeriksaan Sistem Bahan Bakar diperlukan?", None, None)

    question_3 = "Apakah Waktu Terakhir Pergantian Oli lebih dari 6 bulan?"
    true_branch_3 = DecisionNode("Apakah Ketersediaan Suku Cadang tertentu?", None, None)
    false_branch_3 = DecisionNode("Apakah Lokasi Penggunaan Kendaraan di perkotaan?", None, None)

    question_4 = "Apakah Pengecekan Kelistrikan diperlukan?"
    true_branch_4 = DecisionNode("Apakah Pemeriksaan Sistem Bahan Bakar diperlukan?", None, None)
    false_branch_4 = DecisionNode("Apakah Pemeriksaan Sistem Rem diperlukan?", None, None)

    question_5 = "Apakah Pemeriksaan Sistem Bahan Bakar diperlukan?"
    true_branch_5 = DecisionNode("Apakah Pemeriksaan Sistem Rem diperlukan?", None, None)
    false_branch_5 = DecisionNode("Apakah Pemeriksaan Sistem Pendingin diperlukan?", None, None)

    question_6 = "Apakah Pemeriksaan Sistem Rem diperlukan?"
    true_branch_6 = DecisionNode("Apakah Pemeriksaan Sistem Pendingin diperlukan?", None, None)
    false_branch_6 = DecisionNode("Apakah Pemeriksaan Sistem Suspensi diperlukan?", None, None)

    question_7 = "Apakah Pemeriksaan Sistem Pendingin diperlukan?"
    true_branch_7 = DecisionNode("Apakah Pemeriksaan Sistem Suspensi diperlukan?", None, None)
    false_branch_7 = DecisionNode("Apakah Pemeriksaan Sistem Transmisi diperlukan?", None, None)

    question_8 = "Apakah Pemeriksaan Sistem Suspensi diperlukan?"
    true_branch_8 = DecisionNode("Apakah Pemeriksaan Sistem Transmisi diperlukan?", None, None)
    false_branch_8 = DecisionNode("Apakah Pemeriksaan Sistem Knalpot diperlukan?", None, None)

    question_9 = "Apakah Pemeriksaan Sistem Transmisi diperlukan?"
    true_branch_9 = DecisionNode("Apakah Pemeriksaan Sistem Knalpot diperlukan?", None, None)
    false_branch_9 = DecisionNode("Apakah Pemeriksaan Sistem Knalpot diperlukan?", None, None)

    question_10 = "Apakah Pemeriksaan Sistem Knalpot diperlukan?"
    true_branch_10 = DecisionNode("Apakah Pemeriksaan Sistem Kelistrikan diperlukan?", None, None)
    false_branch_10 = DecisionNode("Rekomendasikan layanan ringan", None, None)

    question_11 = "Apakah Pemeriksaan Sistem Kelistrikan diperlukan?"
    true_branch_11 = DecisionNode("Rekomendasikan layanan ringan", None, None)
    false_branch_11 = DecisionNode("Rekomendasikan layanan sedang", None, None)

    return DecisionNode(question_1, true_branch_1, false_branch_1)

def traverse_decision_tree(node):
    if isinstance(node, Leaf):
        print("Rekomendasi:", node.recommendation)
    else:
        answer = ask_question(node.question)
        if answer:
            traverse_decision_tree(node.true_branch)
        else:
            traverse_decision_tree(node.false_branch)

decision_tree = build_decision_tree()

traverse_decision_tree(decision_tree)

