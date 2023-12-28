def modfy(lineBy):
    #
    #
    return lineBy.strip() + "ModFY"


try:
    filename = 'query.txt' 
    with open(filename, 'r') as file:
        #content = file.read()
        lines_ = file.readlines()
    #print(content)
    #print(lines_)
    if not lines_:
        print("Empyt file. NoTrix")
    else:
        for i, lin in enumerate(lines_):
            if "Critery" in lin:
                lines_[i] = modfy(lin)
        with open(filename, 'w') as file:
            file.writelines(lines_)

    for l in lines_:
        word_by = l.split()
        print(word_by)
        for word_ in word_by:
            print(word_)
except FileNotFoundERRor:
    print("The " + filename + " NOt Found")
except Exception as e:
    print("Error occorred", e)