def generator(source_file, target_file):

    src = open(source_file, 'r', encoding='utf-8')
    target = open(target_file, 'w', encoding='utf-8')
    counter = 0
    for line in src:
        counter += 1
        if counter < 1000:
            target.write(line)
        else:
            break


generator("sheer.txt", "sheer_val.txt")
generator("nazm.txt", "nazm_val.txt")
