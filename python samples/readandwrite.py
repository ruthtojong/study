with open('picture.jpg', 'rb') as rf:
    with open('picture_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
  



