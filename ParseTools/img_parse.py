import cv2
import CONSTANTS


def cropImage(imgData: CONSTANTS.ImageData):
    rec = imgData.getRecBounds()
    itemImg = imgData.getGreyImage()[rec[0][0][1]:rec[2][0][1], rec[0][0][0]:rec[2][0][0]]
    nameImg = imgData.getGreyImage()[CONSTANTS.NAME_LOC[1]:CONSTANTS.NAME_LOC[1] + CONSTANTS.NAME_BOX_SIZE[1],
              CONSTANTS.NAME_LOC[0]:CONSTANTS.NAME_LOC[0] + CONSTANTS.NAME_BOX_SIZE[0]]

    itemImg = simplifyImg(itemImg)
    nameImg = simplifyImg(nameImg)

    # Scaling image x4 because it works better with OCR
    scaling = 4
    itemImg = cv2.resize(itemImg, dsize=(itemImg.shape[1] * scaling, itemImg.shape[0] * scaling),
                         interpolation=cv2.INTER_NEAREST)
    nameImg = cv2.resize(nameImg, dsize=(nameImg.shape[1] * scaling, nameImg.shape[0] * scaling),
                         interpolation=cv2.INTER_NEAREST)

    return nameImg, itemImg


def simplifyImg(img):
    # inverting black and white, because tess works better with dark  text on light background
    tempImg = cv2.bitwise_not(img)
    tempImg[tempImg > 100] = 255  # removed all the noise and shadows
    tempImg[tempImg != 255] = 0   # converts all the pixels that are not white to black

    return tempImg
