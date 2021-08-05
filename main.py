from PyQt5 import QtWidgets,uic
import random



def gum():
    call.output.clear()
    length = int(call.pass_length.text())
    number_of = int(call.number_of_pass.text())
    
    if call.capitals.isChecked():
        add_capitals = True
    else:
        add_capitals = False

    if call.numbers.isChecked():
        add_numbers = True
    else:
        add_numbers = False
        
    if call.specials.isChecked():   
        add_specials = True
    else:
        add_specials = False

    alpha = ["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    capitals = [each_string.upper() for each_string in alpha]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    specials = ["!","@","#","$","%","^","&","*","(",")","-","+","_","[","]","{","}",".","<",">","~","?"]

    final_list = alpha

    if add_capitals == True:
        final_list += capitals


    if add_numbers == True:
        final_list += numbers

    if add_specials == True:
        final_list += specials
    

    for e in range(number_of):
        password = (''.join(random.sample(final_list, length)))
        call.output.append(password)
   

app = QtWidgets.QApplication([])
call = uic.loadUi("main.ui")

call.generate.clicked.connect(gum)



call.show()
app.exec()
