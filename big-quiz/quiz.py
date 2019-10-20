WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box. move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["Qual e a cidade da alemanha que meu pai vai?",
      "Berlin", "Stutgard", "Tubingen", "Jena", 4]

q2 = ["Qual e o aviao favorito de dudu?",
      "cessna 172", "sukhoi superjet", "boeing 737 max 8", "cessna grand caravan", 4]

q3 = ["qual e o planeta mais proximo do sol?",
      "Saturno", "Kepler 62e", "Netuno", "Mercurio", 4]

q4 = ["onde tem piramides?",
      "Na casa do caixa prego", "Marte", "Coco", "Mexico", 4]

q5 = ["qual e a maior estrela do universo?",
      "sol", "uy scuti", "proxima centauri", "mirach", 2]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1
                                    


def game_over():
    global question, time_left
    message = "jogo acabou, você conseguiu acertar %s perguntas corretamente" % str(score)
    question = [message, "-", "-", "-",  "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("Fim das questões")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicou na resposta " + str(index))
            if index == question[5]:
                print("Acertou miseravi")
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
