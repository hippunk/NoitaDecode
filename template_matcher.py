import cv2

N_template = cv2.imread('Data/Patterns/N.png')
S_template = cv2.imread('Data/Patterns/S.png')
E_template = cv2.imread('Data/Patterns/E.png')
O_template = cv2.imread('Data/Patterns/O.png')
C_template = cv2.imread('Data/Patterns/C.png')

def match_template(eye):
    resized_eye = cv2.resize(eye, (N_template.shape[1], N_template.shape[0]))
    res = {}
    method = cv2.TM_CCOEFF_NORMED
    res["N"] = cv2.matchTemplate(resized_eye, N_template, method)[0][0]
    res["S"] = cv2.matchTemplate(resized_eye, S_template, method)[0][0]
    res["E"] = cv2.matchTemplate(resized_eye, E_template, method)[0][0]
    res["W"] = cv2.matchTemplate(resized_eye, O_template, method)[0][0]
    res["C"] = cv2.matchTemplate(resized_eye, C_template, method)[0][0]

    return max(res, key=res.get)