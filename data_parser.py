import os
import cv2
from natsort import natsorted, ns
from imutils import contours
from template_matcher import *
import shutil


def parse_image(image_path):
    # Load image, grayscale, Otsu's threshold
    image_name_without_ext = os.path.splitext(os.path.basename(image_path))[0]
    out_folder = os.path.join('Out', image_name_without_ext)

    image = cv2.imread(image_path)

    print(image.shape[1])

    scale_factor = 4
    area_size_threshold = 400

    image = cv2.resize(image, (image.shape[1] * (scale_factor), image.shape[0] * (scale_factor + 2)))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    laplacian = cv2.Laplacian(thresh, cv2.CV_8UC1, ksize=3)

    # Replace original image for more readable one
    image = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2RGB)
    # I'm lazy
    thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    # Find contours, sort from left-to-right, then crop
    cnts = cv2.findContours(laplacian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts, _ = contours.sort_contours(cnts, method="left-to-right")

    eyes = []

    for c in cnts:

        area = cv2.contourArea(c)
        if area > area_size_threshold:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            eye = thresh[y:y + h, x:x + w]
            eyes.append(eye)
            res = match_template(eye)
            os.makedirs(out_folder, exist_ok=True)

            tmp_file_name = str(y) + "_" + str(x) + "_" + match_template(eye) + '.png'
            cv2.imwrite(os.path.join(out_folder, tmp_file_name), eye)

    cv2.imwrite(image_name_without_ext + ".png", image)
    # Dirty name parsing because I'm still lazy
    inList = natsorted(os.listdir(out_folder), alg=ns.PATH)
    cpt_x = 0
    cpt_y = 0
    max_x = 0
    last_y = 0

    # correct y offcet
    for filename in inList:
        filename_without_ext = os.path.splitext(filename)[0]
        filename_tokens = filename_without_ext.split('_')
        x = int(filename_tokens[1])
        y = int(filename_tokens[0])
        orientation = filename_tokens[2]
        if (y < last_y + 10) and last_y != 0:
            y = last_y
        file_out_name = str(y) + "_" + str(x) + "_" + orientation + ".png"
        os.rename(os.path.join(out_folder, filename), os.path.join(out_folder, file_out_name))
        last_y = y

    inList = natsorted(os.listdir(out_folder), alg=ns.PATH)
    for filename in inList:
        filename_without_ext = os.path.splitext(filename)[0]
        filename_tokens = filename_without_ext.split('_')
        x = int(filename_tokens[1])
        y = int(filename_tokens[0])
        orientation = filename_tokens[2]
        if x < (max_x):
            cpt_x = 0
            cpt_y += 1

        max_x = x
        file_out_name = str(cpt_y) + "_" + str(cpt_x) + "_" + orientation + ".png"
        os.rename(os.path.join(out_folder, filename), os.path.join(out_folder, file_out_name))
        cpt_x += 1

        pattern_out_folder = os.path.join("Out", "PatternChecker", orientation)
        os.makedirs(pattern_out_folder, exist_ok=True)
        shutil.copyfile(os.path.join(out_folder, file_out_name),
                        os.path.join(pattern_out_folder, image_name_without_ext + "_" + file_out_name))


def parse_all_data():
    parse_image('Data/E1.png')
    parse_image('Data/E2.png')
    parse_image('Data/E3.png')
    parse_image('Data/E4.png')
    parse_image('Data/E5.png')

    parse_image('Data/W1.png')
    parse_image('Data/W2.png')
    parse_image('Data/W3.png')
    parse_image('Data/W4.png')
