faceInfo = {
    "width": 145,
    "height": 180
}


def calculateRatio(width, height):
    ratio = width / height
    return ratio


def ratioAnalysis(ratio):
    if ratio > 1:
        return "Face is wide"
    else:
        return "Face is long"


ratio = calculateRatio(
    faceInfo["width"],
    faceInfo["height"]
)


print("================= FaceWise =================")
print("Face Width:", faceInfo["width"])
print("Face Height:", faceInfo["height"])
print("Face Ratio:", ratio)
print("Analysis:", ratioAnalysis(ratio))