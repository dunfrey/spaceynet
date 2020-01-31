# CHECKPOINT
CK_SPACEYNET_V1 = 'spaceynet_v1_model.h5'
CK_SPACEYNET_V2 = 'spaceynet_v2_model.h5'
CK_POSENET = 'posenet_model.h5'
CK_CONTEXTUALNET = 'contextualnet_model.h5'

CK_CHOICE = CK_SPACEYNET_V1

IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNEL = 3
EPOCHS = 20
BATCH_SIZE = 65
VALID_SPLIT = 25
LEARNING_RATE = 0.001
DECAY = LEARNING_RATE/100
AMSGRAD = True
