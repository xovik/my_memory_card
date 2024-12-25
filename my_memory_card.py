# импорт
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QApplication, QWidget,
  QBoxLayout, QVBoxLayout, QHBoxLayout,
  QGroupBox, QPushButton, QRadioButton,
  QLabel, QButtonGroup,
)
from random import shuffle,randint

# Данные о вопросе удобно «собернуть» в класс Question
class Question:
  def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    # Все строки надо задать при создании объекта, они запоминаются в свойства 
    self.question = question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3
    
# Список с вопросами
questions_list = []

#Добавление экземпляра в список вопросов
questions_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зеленый', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Сколько всего материков на планете земля?', '6', '7', '10', '5'))
questions_list.append(Question('Национальная хижина якутов?', 'Ураса', 'Ырыта', 'Иглу', 'Хата'))
questions_list.append(Question('Столица России?', 'Москва', 'Санкт - Петербугр', 'Тверь', 'Брянск'))

#Создаем приложение
app = QApplication([])

#Создаем кнопку
btn_OK = QPushButton('Ответить') #кнопка ответа
lb_question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
 
#Создаем группу с названием "Варианты ответов"
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами

#Создаем кнопки с переключателями
rbtn_1 = QRadioButton("Вариант 1")
rbtn_2 = QRadioButton("Вариант 2")
rbtn_3 = QRadioButton("Вариант 3")
rbtn_4 = QRadioButton("Вариант 4")

# Групировка переключателей
RadioGroup = QButtonGroup()
# каждую кнопку в группу
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
# линии
layout_ans1 = QHBoxLayout()#горизонтальная
layout_ans2 = QVBoxLayout()#вертикальные
layout_ans3 = QVBoxLayout()
# виджеты кнопки
layout_ans2.addWidget(rbtn_1)#первый столбик
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)#второй
layout_ans3.addWidget(rbtn_4)
# две вертикальные в горизонтальную
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)#столбцы в одной строчке

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('Прав ты или нет?')#правильно или нет
lb_Correct = QLabel('Ответ будет тут')#правильный ответ

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()#вопрос
layout_line2 = QHBoxLayout()#варинаты и результаты
layout_line3 = QHBoxLayout()#кнопка


layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()#скроем панель с ответом

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)#кнопка большая
layout_line3.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)#пробелы
#показ панель ответов
def show_resut():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
#показ панель вопросов
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    #сбросить выбраную радио кнопку
    RadioGroup.setExclusive(False)#снять 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)#вернуть теперь только одна может быть выбрана

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]#список кнопок
#записывает значение вопроса и ответов в виджеты
def ask(q: Question):
    shuffle(answers)#перемешали
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)#вопрос
    lb_Correct.setText(q.right_answer)#ответ
    show_question()#показывать

def show_correct(res):
    lb_Result.setText(res)
    show_resut()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


    
#задает следующий
def next_question():
    cur_question = randint(0, len(questions_list)-1)
    window.total += 1
    #статистика
    print('Статистика \n-Всего вопросов:',window.total,'\n-Правильных ответов:', window.score)
    window.rating = (window.score / window.total)*100
    print('Рейтинг:',window.rating,'%')
    #перемешивание вариантов
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    #перемешивание вопросов
    window.cur_question = randint(0, len(questions_list)-1)
    q = questions_list[window.cur_question]
    
    ask(q)
    
#определяет надо ли следующий вопрос или проверить ответ
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()#проверить
    else:
        next_question()#следуйщий



window = QWidget()#создание окна
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
#задать вопрос и показать окно
next_question()
window.resize(400, 300)
window.show()
app.exec()